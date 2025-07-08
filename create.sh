#!/bin/bash

# Check if at least two arguments are passed
if [ "$#" -lt 2 ]; then
    echo "Usage: $0 <question_number> <question_name>"
    echo "Example: $0 303 'Range Sum Query Immutable'"
    exit 1
fi

# Extract arguments
QUESTION_NUM=$1
shift
QUESTION_NAME="$*"

# Format folder name (replace spaces with hyphens)
FORMATTED_NAME=$(echo "$QUESTION_NAME" | sed 's/ /-/g')
FOLDER_NAME="${QUESTION_NUM}.${FORMATTED_NAME}"

# Check if folder already exists
if [ -d "$FOLDER_NAME" ]; then
    echo "Error: Folder '$FOLDER_NAME' already exists."
    exit 1
fi

# Create folder and solution.py
mkdir -p "$FOLDER_NAME"
SOLUTION_FILE="$FOLDER_NAME/solution.py"
touch "$SOLUTION_FILE"

# Add a comment header to solution.py
cat << EOF > "$SOLUTION_FILE"
# LeetCode Problem: $QUESTION_NUM. $QUESTION_NAME
# Link: https://leetcode.com/problems/$(echo "$FORMATTED_NAME" | tr 'A-Z' 'a-z')

# Your solution goes here

EOF

echo "Created folder: $FOLDER_NAME"
echo "Created file with header: $SOLUTION_FILE"
