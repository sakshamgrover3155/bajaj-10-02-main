#!/bin/bash

# Quick Start Script for Flask API
# This script sets up and runs the Flask application

echo "🚀 Flask API - Quick Start Script"
echo "=================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.11 or higher."
    exit 1
fi

echo "✅ Python found: $(python3 --version)"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Check for .env file
if [ ! -f ".env" ]; then
    echo "⚠️  .env file not found!"
    echo "📝 Creating .env from .env.example..."
    cp .env.example .env
    echo ""
    echo "⚠️  IMPORTANT: Edit .env file and add your GEMINI_API_KEY"
    echo "   Get your API key from: https://makersuite.google.com/app/apikey"
    echo ""
    read -p "Press Enter to continue after adding your API key..."
fi

# Check if GEMINI_API_KEY is set
if [ -f ".env" ]; then
    export $(cat .env | grep -v '^#' | xargs)
fi

if [ -z "$GEMINI_API_KEY" ]; then
    echo "⚠️  Warning: GEMINI_API_KEY is not set!"
    echo "   AI endpoint will not work without it."
    echo ""
fi

# Run the application
echo ""
echo "🎉 Starting Flask application..."
echo "📍 API will be available at: http://localhost:5000"
echo "📍 Health check: http://localhost:5000/health"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python app.py
