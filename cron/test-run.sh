#!/bin/bash

# Test script to help set up the Claude command

echo "Let's figure out how to call Claude on your system..."
echo ""

# Check for common Claude CLI commands
echo "Checking for Claude CLI installations:"
echo "--------------------------------"

# Check for 'claude'
if command -v claude &> /dev/null; then
    echo "✓ Found 'claude' command"
    echo "  Path: $(which claude)"
    echo "  Testing: claude --version"
    claude --version 2>&1 | head -5
else
    echo "✗ 'claude' command not found"
fi

echo ""

# Check for 'claude-cli'
if command -v claude-cli &> /dev/null; then
    echo "✓ Found 'claude-cli' command"
    echo "  Path: $(which claude-cli)"
else
    echo "✗ 'claude-cli' command not found"
fi

echo ""

# Check for 'anthropic'
if command -v anthropic &> /dev/null; then
    echo "✓ Found 'anthropic' command"
    echo "  Path: $(which anthropic)"
else
    echo "✗ 'anthropic' command not found"
fi

echo ""
echo "How do you normally interact with Claude?"
echo "1) Through a web interface"
echo "2) Through a CLI tool (please specify the command)"
echo "3) Through an API"
echo "4) Other"
echo ""
echo "Please enter your choice (1-4) and we'll set up the script accordingly:"