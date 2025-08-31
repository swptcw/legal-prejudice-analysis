# Quick Start Guide: Docker Deployment

This guide provides simple, step-by-step instructions for downloading and deploying the Legal Prejudice Analysis system using Docker.

## Prerequisites

Before you begin, ensure you have:

- [Docker](https://docs.docker.com/get-docker/) (version 20.10.0 or higher)
- [Docker Compose](https://docs.docker.com/compose/install/) (version 2.0.0 or higher)
- At least 2GB of available RAM
- At least 1GB of free disk space
- A terminal or command prompt with Git installed

## Option 1: Download from GitHub (Recommended)

### Step 1: Clone the Repository

```bash
# Clone only the docker directory using sparse checkout
mkdir legal-prejudice-docker
cd legal-prejudice-docker
git init
git remote add origin https://github.com/yourusername/legal-prejudice-analysis.git
git config core.sparseCheckout true
echo "docker/" >> .git/info/sparse-checkout
git pull origin main

# Move files to the current directory
mv docker/* .
rm -rf docker
```

### Step 2: Run the Deployment Script

```bash
# Make the script executable
chmod +x deploy.sh

# Run the deployment script
./deploy.sh
```

### Step 3: Access the System

Once deployment is complete, access the system at:
- Web Interface: http://localhost:8080
- API Documentation: http://localhost:8080/api/docs

## Option 2: Manual Download and Setup

### Step 1: Download the Docker Files

1. Visit the GitHub repository: https://github.com/yourusername/legal-prejudice-analysis
2. Navigate to the `docker` directory
3. Download each file individually or use a tool like [DownGit](https://minhaskamal.github.io/DownGit/#/home) to download the entire directory

### Step 2: Configure the Environment

```bash
# Copy the example environment file
cp .env.example .env

# Edit the .env file with your preferred settings
nano .env  # or use any text editor
```

### Step 3: Start the Services

```bash
# Start all services
docker-compose up -d
```

### Step 4: Access the System

Once deployment is complete, access the system at:
- Web Interface: http://localhost:8080 (or the port you configured)
- API Documentation: http://localhost:8080/api/docs

## Option 3: Download from Releases Page

### Step 1: Download the Release Package

1. Visit the GitHub repository releases page: https://github.com/yourusername/legal-prejudice-analysis/releases
2. Find the latest release
3. Download the `legal-prejudice-docker.zip` file
4. Extract the ZIP file to your preferred location

### Step 2: Run the Deployment Script

```bash
# Navigate to the extracted directory
cd path/to/extracted/files

# Make the script executable
chmod +x deploy.sh

# Run the deployment script
./deploy.sh
```

### Step 3: Access the System

Once deployment is complete, access the system at:
- Web Interface: http://localhost:8080
- API Documentation: http://localhost:8080/api/docs

## Common Operations

### Checking System Status

```bash
# View all running containers
docker-compose ps

# Check container logs
docker-compose logs

# Follow logs in real-time
docker-compose logs -f
```

### Stopping the System

```bash
# Stop all services
docker-compose down

# Stop and remove volumes (will delete all data)
docker-compose down -v
```

### Updating the System

```bash
# Pull latest changes
git pull  # if using Git

# Or download the latest files manually

# Restart the services
docker-compose down
docker-compose up -d
```

### Backing Up Data

```bash
# Create a backup of the database
docker-compose exec db pg_dump -U postgres legal_prejudice > backup.sql

# Back up all volumes
docker run --rm -v legal_prejudice_db_data:/source -v $(pwd):/backup alpine tar -czf /backup/db_data_backup.tar.gz /source
docker run --rm -v legal_prejudice_uploads:/source -v $(pwd):/backup alpine tar -czf /backup/uploads_backup.tar.gz /source
```

## Troubleshooting

### Services Fail to Start

**Problem**: One or more services fail to start after running `docker-compose up -d`

**Solution**:
1. Check the logs: `docker-compose logs`
2. Verify your `.env` file has all required values
3. Ensure ports are not already in use: `netstat -tuln | grep 8080`
4. Check for sufficient disk space and memory

### Cannot Connect to Web Interface

**Problem**: The web interface is not accessible at http://localhost:8080

**Solution**:
1. Verify containers are running: `docker-compose ps`
2. Check Nginx logs: `docker-compose logs nginx`
3. Verify the port mapping in `docker-compose.yml`
4. Try accessing with the IP address instead of localhost

### Database Connection Issues

**Problem**: API server cannot connect to the database

**Solution**:
1. Check database logs: `docker-compose logs db`
2. Verify database credentials in `.env` file
3. Ensure the database container is healthy: `docker-compose ps`
4. Try restarting the services: `docker-compose restart`

## Getting Help

If you encounter issues not covered in this guide:

1. Check the [full documentation](https://github.com/yourusername/legal-prejudice-analysis/tree/main/docs)
2. Open an issue on the [GitHub repository](https://github.com/yourusername/legal-prejudice-analysis/issues)
3. Contact support at support@legalprejudice.example.com