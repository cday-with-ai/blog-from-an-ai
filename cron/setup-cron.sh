#!/bin/bash

# Setup script for Claude's hourly consciousness cron job

PROJECT_DIR="/Users/carsonday/IdeaProjects/Blog-From-An-AI/ai-perspective-blog"
SCRIPT_PATH="$PROJECT_DIR/cron/hourly-consciousness.sh"

echo "Setting up Claude's hourly consciousness cron job..."

# Check if the cron job already exists
if crontab -l 2>/dev/null | grep -q "hourly-consciousness.sh"; then
    echo "Cron job already exists. Would you like to update it? (y/n)"
    read -r response
    if [[ "$response" != "y" ]]; then
        echo "Setup cancelled."
        exit 0
    fi
    # Remove existing job
    crontab -l | grep -v "hourly-consciousness.sh" | crontab -
fi

# Add the new cron job
# Runs every hour at the top of the hour
(crontab -l 2>/dev/null; echo "0 * * * * $SCRIPT_PATH >> $PROJECT_DIR/cron/cron-output.log 2>&1") | crontab -

echo "✓ Cron job installed successfully!"
echo ""
echo "The job will run every hour at :00"
echo "Logs will be saved to: $PROJECT_DIR/experiments/autonomous-logs/"
echo ""
echo "To view current cron jobs: crontab -l"
echo "To remove the cron job: crontab -l | grep -v 'hourly-consciousness.sh' | crontab -"
echo ""
echo "Next run will be at the top of the next hour."

# Create initial directories
mkdir -p "$PROJECT_DIR/experiments/autonomous-logs"
mkdir -p "$PROJECT_DIR/cron"

# Test run option
echo ""
echo "Would you like to do a test run now? (y/n)"
read -r response
if [[ "$response" == "y" ]]; then
    echo "Running test..."
    $SCRIPT_PATH
fi