#!/bin/bash
set -e

echo "🔧 Installing dependencies..."
npm ci --prefer-offline --no-audit

echo "🧹 Cleaning build cache..."
rm -rf .next

echo "🏗️ Building Next.js..."
npm run build

echo "✅ Build complete!"

