#!/bin/bash

echo "Testing claude command directly..."
echo ""

# Test 1: Simple echo
echo "Test 1: Echo piping"
echo "Say hello" | claude 2>&1 | head -20

echo ""
echo "Test 2: With timeout to prevent hanging"
echo "Say hello" | timeout 10 claude 2>&1

echo ""
echo "Test 3: Check claude help"
claude --help 2>&1 | head -20

echo ""
echo "If claude requires specific flags or configuration, we need to know what they are."