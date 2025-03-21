import os
import re
import argparse
from pathlib import Path

def copy_mapped_pages(source_dir, target_dir, verbose=False):
    """
    Copy ONLY the mapped_pages section from files in target_dir to matching files in source_dir.
    """
    source_dir = Path(source_dir)
    target_dir = Path(target_dir)
    
    # Ensure directories exist
    if not source_dir.is_dir():
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return
    if not target_dir.is_dir():
        print(f"Error: Target directory '{target_dir}' does not exist.")
        return
    
    # Process files in source directory
    source_files = list(source_dir.glob('*.md'))
    if not source_files:
        source_files = list(source_dir.glob('*'))  # Try without extension if no md files
    
    if verbose:
        print(f"Found {len(source_files)} files to process.")
    
    files_updated = 0
    files_skipped = 0
    
    for source_file in source_files:
        target_file = target_dir / source_file.name
        
        # Skip if no matching target file
        if not target_file.exists():
            files_skipped += 1
            if verbose:
                print(f"Skipped: No matching file for {source_file.name}")
            continue
        
        # Read files
        with open(source_file, 'r', encoding='utf-8') as f:
            source_content = f.read()
        with open(target_file, 'r', encoding='utf-8') as f:
            target_content = f.read()
        
        # Extract mapped_pages from target file
        target_mapped_pattern = re.search(r'(mapped_pages:\s*(?:[ \t]*-.*\n)*)', target_content)
        if not target_mapped_pattern:
            files_skipped += 1
            if verbose:
                print(f"Skipped: No mapped_pages in target file {source_file.name}")
            continue
        
        target_mapped_pages = target_mapped_pattern.group(1).rstrip()
        
        # Extract frontmatter and content
        fm_match = re.match(r'^---\s*\n(.*?)\n---', source_content, re.DOTALL)
        if not fm_match:
            files_skipped += 1
            if verbose:
                print(f"Skipped: No frontmatter in source file {source_file.name}")
            continue
        
        # Get existing frontmatter
        fm_content = fm_match.group(1)
        
        # Find where the real content starts (after the first ---)
        fm_end_pos = source_content.find('---', 3) + 3
        main_content = source_content[fm_end_pos:]
        
        # Clean up any additional frontmatter sections in the main content
        main_content = re.sub(r'^---.*?---\s*', '', main_content, flags=re.DOTALL)
        
        # Update frontmatter with mapped_pages
        if re.search(r'mapped_pages:', fm_content):
            # Replace existing mapped_pages
            new_fm = re.sub(
                r'mapped_pages:\s*(?:[ \t]*-.*\n)*',
                target_mapped_pages + '\n',
                fm_content
            )
        else:
            # Add mapped_pages to frontmatter
            new_fm = fm_content.rstrip() + '\n' + target_mapped_pages
        
        # Carefully rebuild the file content
        updated_content = f"---\n{new_fm}\n---{main_content}"
        
        # Only write if content changed
        if updated_content != source_content:
            with open(source_file, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            files_updated += 1
            print(f"Updated: {source_file.name}")
        else:
            if verbose:
                print(f"Skipped: No changes needed for {source_file.name}")
            files_skipped += 1
    
    print(f"\nSummary:")
    print(f"  Files updated: {files_updated}")
    print(f"  Files skipped: {files_skipped}")
    print(f"  Total files: {len(source_files)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Copy ONLY mapped_pages from files in target directory to matching files in source directory.'
    )
    parser.add_argument('source_dir', help='Directory containing files to be updated')
    parser.add_argument('target_dir', help='Directory containing files with mapped_pages to copy')
    parser.add_argument('-v', '--verbose', action='store_true', help='Show detailed progress information')
    
    args = parser.parse_args()
    copy_mapped_pages(args.source_dir, args.target_dir, args.verbose)
