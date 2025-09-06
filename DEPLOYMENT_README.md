# Legal Prejudice Analysis Platform - Complete Deployment Guide

## Overview
Complete deployment setup using GitHub secrets for VPS access to demo.legal-prejudice-analysis.org.

## GitHub Secrets Configuration
Your repository must have these secrets configured:

### Required Secrets
- `VPS_HOST`: demo.legal-prejudice-analysis.org
- `VPS_USER`: deploy (or your VPS username)
- `VPS_SSH_KEY`: Private SSH key for deployment

### Setting Up Secrets
1. Go to Repository Settings → Secrets and variables → Actions
2. Add the following secrets:
   - VPS_HOST: demo.legal-prejudice-analysis.org
   - VPS_USER: your-vps-username
   - VPS_SSH_KEY: your-private-ssh-key

## Deployment Architecture
- **Web Server**: Apache2 with mod_wsgi
- **Deployment**: Automated via GitHub Actions + rsync
- **SSL**: HTTPS support with SSL certificates
- **Monitoring**: Automated health checks

## Quick Start

### 1. VPS Setup (One-time)
```bash
# Run on VPS to prepare environment
sudo apt update && sudo apt install -y apache2 libapache2-mod-wsgi-py3 rsync
```

### 2. GitHub Actions (Automatic)
- **Trigger**: Push to main/develop branches
- **Process**: Rsync files to VPS using secrets
- **Verification**: Health checks and deployment validation

### 3. Manual Deployment
```bash
# Using GitHub secrets
VPS_HOST=demo.legal-prejudice-analysis.org
VPS_USER=deploy
rsync -avz --delete ./ $VPS_USER@$VPS_HOST:/var/www/demo.legal-prejudice-analysis.org/
```

## URLs
- **Demo Site**: http://demo.legal-prejudice-analysis.org
- **API Health**: http://demo.legal-prejudice-analysis.org/api/health
- **Documentation**: http://demo.legal-prejudice-analysis.org/docs/

## Directory Structure
```
/var/www/demo.legal-prejudice-analysis.org/
├── index.html          # Main demo page
├── docs/              # Documentation
├── api/               # API endpoints
├── assets/            # Static assets
├── css/               # Stylesheets
├── js/                # JavaScript files
└── deploy/            # Deployment scripts
```

## Deployment Process
1. **GitHub Actions** triggers on push
2. **SSH** connection using secrets
3. **Rsync** synchronizes files
4. **Apache2** serves the application
5. **Health checks** verify success

## Monitoring
- **Health Checks**: http://demo.legal-prejudice-analysis.org/api/health
- **Logs**: /var/log/apache2/
- **Backup**: Automatic before each deployment

## Troubleshooting
### Common Issues
1. **Permission Denied**: Check SSH key in secrets
2. **Connection Failed**: Verify VPS_HOST and VPS_USER
3. **Apache Errors**: Check Apache logs

### Debug Commands
```bash
# Test deployment
curl -f http://demo.legal-prejudice-analysis.org/api/health

# Check logs
ssh $VPS_USER@$VPS_HOST "tail -f /var/log/apache2/error.log"

# Verify deployment
rsync -avz --dry-run ./ $VPS_USER@$VPS_HOST:/var/www/demo.legal-prejudice-analysis.org/
```

## Security
- **SSH Keys**: Use dedicated deployment keys
- **Secrets**: Never commit secrets to repository
- **Permissions**: Restrict file access appropriately

## Support
For issues or questions:
1. Check GitHub Actions logs
2. Verify VPS connectivity
3. Review Apache error logs
4. Test API endpoints

## Development Workflow
1. Make changes locally
2. Push to GitHub
3. GitHub Actions deploys automatically
4. Verify deployment success
5. Monitor via health endpoints