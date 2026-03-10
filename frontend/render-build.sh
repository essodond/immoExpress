#!/bin/bash
set -e

echo "🔧 Installing dependencies..."
npm ci --prefer-offline --no-audit

echo "🧹 Cleaning build cache..."
rm -rf .next out

echo "🏗️ Building Next.js application..."
npm run build

echo "✅ Build complete!"

