#!/bin/bash
# Deployment script for Legal Prejudice Analysis Project

set -e

# Display banner
echo "=================================================="
echo "  Legal Prejudice Analysis Project Deployment"
echo "=================================================="
echo ""

# Check for Docker and Docker Compose
echo "Checking prerequisites..."
if ! command -v docker &> /dev/null; then
    echo "Error: Docker is not installed. Please install Docker first."
    echo "Visit https://docs.docker.com/get-docker/ for installation instructions."
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo "Error: Docker Compose is not installed. Please install Docker Compose first."
    echo "Visit https://docs.docker.com/compose/install/ for installation instructions."
    exit 1
fi

echo "Docker and Docker Compose are installed."
echo ""

# Check for .env file
if [ ! -f .env ]; then
    echo "Environment file (.env) not found. Creating from example..."
    if [ -f .env.example ]; then
        cp .env.example .env
        echo "Created .env file from example. Please edit it with your configuration."
        echo "You should at least change the following values:"
        echo "  - DB_PASSWORD"
        echo "  - API_SECRET_KEY"
        echo "  - JWT_SECRET (if using authentication)"
    else
        echo "Error: .env.example file not found. Please create a .env file manually."
        exit 1
    fi
fi

# Prompt for configuration
echo "Do you want to edit the .env file now? (y/n)"
read -r edit_env
if [[ "$edit_env" =~ ^[Yy]$ ]]; then
    if command -v nano &> /dev/null; then
        nano .env
    elif command -v vim &> /dev/null; then
        vim .env
    else
        echo "No editor found. Please edit the .env file manually before continuing."
        echo "Press Enter to continue once you've edited the file..."
        read -r
    fi
fi

# Create necessary directories
echo "Creating necessary directories..."
mkdir -p nginx/certs

# Check if SSL certificates exist
if [ ! -f nginx/certs/server.crt ] || [ ! -f nginx/certs/server.key ]; then
    echo "SSL certificates not found. Do you want to:"
    echo "1) Generate self-signed certificates (for testing only)"
    echo "2) Skip SSL setup (HTTP only)"
    echo "3) Exit to add your own certificates"
    read -r ssl_option
    
    case $ssl_option in
        1)
            echo "Generating self-signed certificates..."
            openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
                -keyout nginx/certs/server.key \
                -out nginx/certs/server.crt \
                -subj "/CN=localhost"
            echo "Self-signed certificates generated. Note: These are for testing only."
            
            # Uncomment SSL configuration in nginx config
            sed -i 's/# server {/server {/' nginx/conf.d/default.conf
            sed -i 's/# }/}/' nginx/conf.d/default.conf
            sed -i 's/#     /    /' nginx/conf.d/default.conf
            ;;
        2)
            echo "Skipping SSL setup. The system will be available over HTTP only."
            ;;
        3)
            echo "Exiting. Please add your SSL certificates to nginx/certs/ and run this script again."
            exit 0
            ;;
        *)
            echo "Invalid option. Skipping SSL setup."
            ;;
    esac
fi

# Pull or build Docker images
echo "Building Docker images..."
docker-compose build

# Start the services
echo "Starting services..."
docker-compose up -d

# Check if services are running
echo "Checking if services are running..."
sleep 5
if docker-compose ps | grep -q "Exit"; then
    echo "Error: Some services failed to start. Check the logs with 'docker-compose logs'."
    exit 1
fi

# Get the public URL
HOST_IP=$(hostname -I | awk '{print $1}')
PORT=$(grep EXTERNAL_PORT .env | cut -d= -f2 || echo 8080)

echo ""
echo "=================================================="
echo "  Deployment Complete!"
echo "=================================================="
echo ""
echo "Your Legal Prejudice Analysis system is now running."
echo ""
echo "Access the system at:"
echo "  - Web Interface: http://$HOST_IP:$PORT"
echo "  - API Documentation: http://$HOST_IP:$PORT/api/docs"
echo ""
echo "To view logs:"
echo "  docker-compose logs"
echo ""
echo "To stop the system:"
echo "  docker-compose down"
echo ""
echo "To update the system:"
echo "  git pull"
echo "  docker-compose down"
echo "  docker-compose build"
echo "  docker-compose up -d"
echo ""
echo "For more information, see the documentation in the README.md file."
echo "=================================================="