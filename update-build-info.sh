#!/bin/bash
# Stamps the current commit into build-info.json, which the footer reads.
# Run this before committing a deploy.
set -euo pipefail

cd "$(dirname "$0")"

COMMIT_HASH=$(git rev-parse HEAD)
BUILD_DATE=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

cat > build-info.json <<JSON
{
    "commitHash": "${COMMIT_HASH}",
    "buildDate": "${BUILD_DATE}"
}
JSON

echo "build-info.json -> ${COMMIT_HASH:0:7} ${BUILD_DATE}"
