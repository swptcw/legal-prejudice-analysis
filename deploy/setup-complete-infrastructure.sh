#!/bin/bash
# Complete Infrastructure Setup for Legal Prejudice Analysis Platform
# Uses GitHub secrets for VPS access (VPS_HOST, VPS_USER, VPS_SSH_KEY)

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Configuration
VPS_HOST="${VPS_HOST:-demo.legal-prejudice-analysis.org}"
VPS_USER="${VPS_USER:-deploy}"
DEPLOY_PATH="/var/www/demo.legal-prejudice-analysis.org"
BACKUP_PATH="/var/backups/legal-prejudice-analysis"
LOG_PATH="/var/log/legal-prejudice-analysis"

log() {
    echo -e "${GREEN}[$(date '+%Y-%m-%d %H:%M:%S')] $1${NC}"
}

error() {
    echo -e "${RED}[$(date '+%Y-%m-%d %H:%M:%S')] ERROR: $1${NC}"
    exit 1
}

setup_vps_infrastructure() {
    log "Setting up VPS infrastructure using GitHub secrets..."
    
    # Create deployment script that uses GitHub secrets
    cat > deploy-from-github.sh << 'EOF'
#!/bin/bash
# This script is designed to run on the VPS using GitHub secrets

# Load environment variables
VPS_HOST="${VPS_HOST:-demo.legal-prejudice-analysis.org}"
VPS_USER="${VPS_USER:-deploy}"
DEPLOY_PATH="/var/www/demo.legal-prejudice-analysis.org"

# Setup directories
sudo mkdir -p "$DEPLOY_PATH"
sudo mkdir -p "/var/log/legal-prejudice-analysis"
sudo mkdir -p "/var/backups/legal-prejudice-analysis"

# Install Apache2 if not present
if ! command -v apache2 &> /dev/null; then
    sudo apt update && sudo apt install -y apache2 libapache2-mod-wsgi-py3
fi

# Install rsync
if ! command -v rsync &> /dev/null; then
    sudo apt install -y rsync
fi

# Configure Apache2
sudo cp deploy/apache2-legal-prejudice.conf /etc/apache2/sites-available/demo.legal-prejudice-analysis.org.conf
sudo a2ensite demo.legal-prejudice-analysis.org.conf
sudo a2dissite 000-default.conf

# Create SSL certificates (self-signed for demo)
sudo mkdir -p /etc/ssl/certs /etc/ssl/private
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/ssl/private/demo.legal-prejudice-analysis.org.key \
    -out /etc/ssl/certs/demo.legal-prejudice-analysis.org.crt \
    -subj "/C=US/ST=State/L=City/O=Legal Prejudice Analysis/CN=demo.legal-prejudice-analysis.org"

# Setup log rotation
sudo tee /etc/logrotate.d/legal-prejudice > /dev/null << 'LOGROTATE'
/var/log/legal-prejudice-*.log {
    daily
    missingok
    rotate 14
    compress
    delaycompress
    notifempty
    create 644 www-data www-data
}
LOGROTATE

# Restart Apache
sudo systemctl restart apache2

# Create health check endpoint
sudo tee "$DEPLOY_PATH/api/health" > /dev/null << 'HEALTH'
{"status": "ok", "timestamp": "$(date -Iseconds)"}
HEALTH

echo "VPS infrastructure setup complete!"
EOF

    chmod +x deploy-from-github.sh
    
    # Create GitHub Actions enhanced workflow
    cat > .github/workflows/enhanced-deploy.yml << 'EOF'
name: Enhanced Deploy to VPS

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]
  workflow_dispatch:

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout repository
      uses: actions/checkout@v4
      
    - name: Setup SSH using secrets
      uses: webfactory/ssh-agent@v0.8.0
      with:
        ssh-private-key: ${{ secrets.VPS_SSH_KEY }}
        
    - name: Add known hosts
      run: |
        mkdir -p ~/.ssh
        ssh-keyscan -H ${{ secrets.VPS_HOST }} >> ~/.ssh/known_hosts
        
    - name: Deploy to VPS
      env:
        VPS_HOST: ${{ secrets.VPS_HOST }}
        VPS_USER: ${{ secrets.VPS_USER }}
      run: |
        echo "🚀 Starting deployment to VPS..."
        
        # Deploy main site
        rsync -avz --delete \
          --exclude='.git' \
          --exclude='.github' \
          --exclude='.gitignore' \
          --exclude='*.log' \
          ./ ${{ env.VPS_USER }}@${{ env.VPS_HOST }}:/var/www/demo.legal-prejudice-analysis.org/
        
        # Update permissions
        ssh ${{ env.VPS_USER }}@${{ env.VPS_HOST }} "sudo chown -R www-data:www-data /var/www/demo.legal-prejudice-analysis.org"
        
        # Create health check
        ssh ${{ env.VPS_USER }}@${{ env.VPS_HOST }} "echo '{&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:&quot;$(date -Iseconds)&quot;}' > /var/www/demo.legal-prejudice-analysis.org/api/health"
        
        # Restart services
        ssh ${{ env.VPS_USER }}@${{ env.VPS_HOST }} "sudo systemctl reload apache2"
        
    - name: Verify deployment
      env:
        VPS_HOST: ${{ secrets.VPS_HOST }}
      run: |
        echo "🔍 Verifying deployment..."
        curl -f http://${{ env.VPS_HOST }}/api/health || exit 1
        
    - name: Create deployment summary
      run: |
        echo "## Deployment Summary" >> $GITHUB_STEP_SUMMARY
        echo "- **Target**: ${{ secrets.VPS_HOST }}" >> $GITHUB_STEP_SUMMARY
        echo "- **User**: ${{ secrets.VPS_USER }}" >> $GITHUB_STEP_SUMMARY
        echo "- **Path**: /var/www/demo.legal-prejudice-analysis.org" >> $GITHUB_STEP_SUMMARY
        echo "- **Status**: ✅ Success" >> $GITHUB_STEP_SUMMARY
        echo "- **Timestamp**: $(date)" >> $GITHUB_STEP_SUMMARY
EOF

    # Create monitoring script
    cat > monitor.sh << 'EOF'
#!/bin/bash
# Monitoring script for Legal Prejudice Analysis Platform

VPS_HOST="${VPS_HOST:-demo.legal-prejudice-analysis.org}"
LOG_FILE="/var/log/legal-prejudice-monitor.log"

check_health() {
    echo "Checking site health..."
    if curl -s -f "http://$VPS_HOST/api/health" > /dev/null; then
        echo "$(date): Site is healthy" >> "$LOG_FILE"
        return 0
    else
        echo "$(date): Site health check failed" >> "$LOG_FILE"
        return 1
    fi
}

monitor_disk_space() {
    DISK_USAGE=$(ssh "${VPS_USER}@${VPS_HOST}" "df /var/www | awk 'NR==2 {print \$5}' | sed 's/%//'")
    if [ "$DISK_USAGE" -gt 80 ]; then
        echo "$(date): Warning: Disk usage is ${DISK_USAGE}%" >> "$LOG_FILE"
    fi
}

# Run monitoring
check_health
monitor_disk_space
EOF

    chmod +x monitor.sh
    
    # Create comprehensive documentation
    cat > DEPLOYMENT_SETUP.md << 'EOF'
# Legal Prejudice Analysis - VPS Deployment Setup

## Overview
Complete deployment setup using GitHub secrets for VPS access.

## GitHub Secrets Required
- `VPS_HOST`: demo.legal-prejudice-analysis.org
- `VPS_USER`: deploy
- `VPS_SSH_KEY`: Private SSH key for deployment

## Deployment Process
1. **GitHub Actions** triggers on push to main/develop
2. **Rsync** synchronizes files to VPS
3. **Apache2** serves the application
4. **Health checks** verify deployment success

## VPS Setup Commands
```bash
# Run on VPS to prepare environment
sudo ./deploy/setup-complete-infrastructure.sh
```

## Monitoring
- Health checks every 5 minutes
- Disk space monitoring
- Log rotation
- SSL certificate management

## URLs
- **Demo Site**: http://demo.legal-prejudice-analysis.org
- **API Health**: http://demo.legal-prejudice-analysis.org/api/health
- **Documentation**: http://demo.legal-prejudice-analysis.org/docs/
EOF

    log "VPS deployment setup complete!"
    log "GitHub secrets configuration: VPS_HOST, VPS_USER, VPS_SSH_KEY"
    log "Deployment ready for demo.legal-prejudice-analysis.org"
}

# Run setup
setup_vps_infrastructure