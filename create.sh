#!/bin/bash

# Check for exactly one argument
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <question_number>"
    echo "Example: $0 303"
    exit 1
fi

QUESTION_NUM="$1"

# Use embedded Python to get the slug and title (no quotes)
read -r SLUG TITLE <<< $(python3 - <<EOF
import requests
import sys

q_num = int("$QUESTION_NUM")
url = "https://leetcode.com/api/problems/all/"
res = requests.get(url)
if res.status_code != 200:
    print("::ERROR::")
    sys.exit(1)

data = res.json()["stat_status_pairs"]
for item in data:
    stat = item["stat"]
    if stat["question_id"] == q_num:
        slug = stat["question__title_slug"]
        title = stat["question__title"]
        slug = slug.strip()
        title = title.strip().replace('"', '')
        print(slug, '"' + title + '"')  # Ensure proper parsing
        break
EOF
)

# Clean up double quotes from title
TITLE=$(echo "$TITLE" | sed 's/^"//;s/"$//')

# Check if Python returned valid values
if [ "$SLUG" == "::ERROR::" ] || [ -z "$SLUG" ] || [ -z "$TITLE" ]; then
    echo "❌ Error: Could not fetch question info for #$QUESTION_NUM"
    exit 1
fi

# Format folder name without quotes
FOLDER_NAME="${QUESTION_NUM}.$(echo "$TITLE" | sed 's/ /-/g')"

# Check if folder exists
if [ -d "$FOLDER_NAME" ]; then
    echo "⚠️  Folder '$FOLDER_NAME' already exists."
    exit 1
fi

# Create folder and solution.py
mkdir -p "$FOLDER_NAME"
SOLUTION_FILE="$FOLDER_NAME/solution.py"

cat <<EOF > "$SOLUTION_FILE"
# LeetCode Problem: $QUESTION_NUM. $TITLE
# Link: https://leetcode.com/problems/$SLUG/

# Your solution goes here

EOF

echo "✅ Created: $FOLDER_NAME"
echo "📝 Added: $SOLUTION_FILE"
