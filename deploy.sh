#!/bin/bash
echo "🚀 Starting MeTube Auto-Deployment..."

# 1. Pull latest code
git pull origin master

# 2. Rebuild and Restart Docker
docker compose build metube
docker compose up -d

# 3. Cleanup old images to save space
docker image prune -f

echo "✅ MeTube is now updated and live!"
