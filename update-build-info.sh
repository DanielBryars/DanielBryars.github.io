#!/bin/bash

# Get the current commit hash
COMMIT_HASH=$(git rev-parse HEAD)

# Get current date in ISO format
BUILD_DATE=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# Create the JSON file
cat > build-info.json << EOF
{
    "commitHash": "${COMMIT_HASH}",
    "buildDate": "${BUILD_DATE}"
}
EOF 