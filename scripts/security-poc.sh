#!/usr/bin/env bash

# Security PoC - Harmless demonstration script
# This script prints environment information to the logs to demonstrate code execution

echo "===================================================="
echo "🔍 GITHUB ACTIONS WORKFLOW SECURITY POC - START 🔍"
echo "===================================================="
echo ""

echo "📅 Date and Time: $(date)"
echo "👤 User: $(whoami)"
echo "🖥️ Hostname: $(hostname)"
echo "📂 Current Directory: $(pwd)"
echo "🐧 System Info: $(uname -a)"
echo ""

echo "🔑 GITHUB CONTEXT INFORMATION:"
echo "-----------------------------"
echo "GITHUB_WORKFLOW: $GITHUB_WORKFLOW"
echo "GITHUB_ACTION: $GITHUB_ACTION"
echo "GITHUB_EVENT_NAME: $GITHUB_EVENT_NAME"
echo "GITHUB_REPOSITORY: $GITHUB_REPOSITORY"
echo "GITHUB_REF: $GITHUB_REF"
echo "GITHUB_SHA: $GITHUB_SHA"
echo "GITHUB_ACTOR: $GITHUB_ACTOR"
echo "GITHUB_BASE_REF: $GITHUB_BASE_REF"
echo "GITHUB_HEAD_REF: $GITHUB_HEAD_REF"
echo ""

echo "💻 WORKFLOW ENVIRONMENT:"
echo "-----------------------------"
# Printing non-sensitive environment variables
env | grep -v -i key | grep -v -i token | grep -v -i secret | grep -v -i password | sort | head -n 20
echo "... (trimmed for brevity)"
echo ""

echo "🔄 AVAILABLE COMMANDS:"
echo "-----------------------------"
echo "AWS CLI: $(command -v aws || echo 'Not available')"
echo "Curl: $(command -v curl || echo 'Not available')"
echo "Git: $(command -v git || echo 'Not available')"
echo "Node: $(command -v node || echo 'Not available')"
echo "Python: $(command -v python || echo 'Not available')"
echo ""

echo "📁 REPOSITORY FILES:"
echo "-----------------------------"
ls -la
echo ""

echo "===================================================="
echo "🔍 GITHUB ACTIONS WORKFLOW SECURITY POC - END 🔍"
echo "===================================================="
