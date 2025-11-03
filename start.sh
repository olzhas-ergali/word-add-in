#!/bin/bash

# Start script for development

echo "🚀 Starting Printable Forms Word Add-in..."
echo ""

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "⚠️  .env file not found!"
    echo "Creating .env from .env.example..."
    cp .env.example .env
    echo "✅ .env created. Please edit it with your credentials."
    exit 1
fi

# Check Docker
if ! command -v docker &> /dev/null; then
    echo "❌ Docker not found. Please install Docker first."
    exit 1
fi

# Start with Docker Compose
echo "📦 Starting backend with Docker..."
docker-compose up -d

# Wait for backend to be ready
echo "⏳ Waiting for backend to start..."
sleep 3

# Check backend health
if curl -s http://localhost:8000/health > /dev/null; then
    echo "✅ Backend is running at http://localhost:8000"
    echo "📖 API docs: http://localhost:8000/docs"
else
    echo "❌ Backend failed to start. Check logs with: docker-compose logs"
    exit 1
fi

echo ""
echo "🎉 Backend started successfully!"
echo ""
echo "Next steps:"
echo "1. cd frontend"
echo "2. npm install (if not done yet)"
echo "3. npm run serve"
echo "4. Load manifest.xml in Word"
echo ""

