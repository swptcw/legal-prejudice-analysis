#!/bin/bash

# FTP Deployment Script for Legal Prejudice Analysis Project
# This script uploads the project files to the FTP server

# FTP credentials
FTP_USER="tim@legal-prejudice-analysis.com"
FTP_PASS="U$$ff10902525"
FTP_HOST="ftp.legal-prejudice-analysis.com"

# LFTP command with SSL verification disabled
./ftp -u &quot;$FTP_USER,$FTP_PASS&quot; $FTP_HOST -e &quot;set ssl:verify-certificate no;"

# Upload main documentation files
./echo "Uploading main documentation files..."
./put README.md; put LICENSE; put CODE_OF_CONDUCT.md; put CONTRIBUTING.md; exit&quot;"

# Upload docs directory
./echo "Uploading docs directory..."
./mirror -R docs docs; exit&quot;"

# Upload landing page
./echo "Uploading landing page..."
./mirror -R landing-page landing-page; exit&quot;"

# Upload enhanced calculator
./echo "Uploading enhanced calculator..."
./mirror -R enhanced-calculator enhanced-calculator; exit&quot;"

# Upload prejudice risk calculator
./echo "Uploading prejudice risk calculator..."
./mirror -R prejudice_risk_calculator prejudice_risk_calculator; exit&quot;"

# Upload markdown files
./echo "Uploading markdown documentation files..."
./cd /; mput legal_prejudice_*.md; exit&quot;"

./echo "Deployment completed successfully!"