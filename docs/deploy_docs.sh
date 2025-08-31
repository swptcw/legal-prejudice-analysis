#!/bin/bash

# Legal Prejudice Analysis Documentation Hub Deployment Script
# This script deploys the documentation hub to GitHub Pages

# Exit on error
set -e

# Configuration
REPO_URL="https://github.com/swptcw/legal-prejudice-analysis.git"
BRANCH="gh-pages"
DOCS_DIR="docs_new"
TEMP_DIR="temp_deploy"

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${YELLOW}=== Legal Prejudice Analysis Documentation Hub Deployment ===${NC}"

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo -e "${RED}Error: git is not installed. Please install git and try again.${NC}"
    exit 1
fi

# Create temporary directory
echo -e "${GREEN}Creating temporary directory...${NC}"
mkdir -p $TEMP_DIR
cd $TEMP_DIR

# Clone the repository
echo -e "${GREEN}Cloning repository...${NC}"
git clone $REPO_URL .
if [ $? -ne 0 ]; then
    echo -e "${RED}Error: Failed to clone repository. Please check the URL and your permissions.${NC}"
    cd ..
    rm -rf $TEMP_DIR
    exit 1
fi

# Check if gh-pages branch exists
if git show-ref --verify --quiet refs/remotes/origin/$BRANCH; then
    echo -e "${GREEN}Checking out existing $BRANCH branch...${NC}"
    git checkout $BRANCH
else
    echo -e "${GREEN}Creating new $BRANCH branch...${NC}"
    git checkout --orphan $BRANCH
    git rm -rf .
    echo "# Legal Prejudice Analysis Documentation" > README.md
    git add README.md
    git commit -m "Initial commit for GitHub Pages"
fi

# Copy documentation files
echo -e "${GREEN}Copying documentation files...${NC}"
cd ..
cp -r $DOCS_DIR/* $TEMP_DIR/
cd $TEMP_DIR

# Add all files to git
echo -e "${GREEN}Adding files to git...${NC}"
git add .

# Check if there are changes to commit
if git diff-index --quiet HEAD --; then
    echo -e "${YELLOW}No changes to commit. Exiting.${NC}"
    cd ..
    rm -rf $TEMP_DIR
    exit 0
fi

# Commit changes
echo -e "${GREEN}Committing changes...${NC}"
git commit -m "Update documentation hub $(date)"

# Push changes
echo -e "${GREEN}Pushing changes to GitHub...${NC}"
git push origin $BRANCH
if [ $? -ne 0 ]; then
    echo -e "${RED}Error: Failed to push changes. Please check your permissions.${NC}"
    cd ..
    rm -rf $TEMP_DIR
    exit 1
fi

# Clean up
echo -e "${GREEN}Cleaning up...${NC}"
cd ..
rm -rf $TEMP_DIR

echo -e "${GREEN}Deployment complete!${NC}"
echo -e "${YELLOW}Please check the following URLs after DNS propagation:${NC}"
echo -e "- Main documentation: https://docs.legal-prejudice-analysis.org"
echo -e "- Demo site: https://demo.legal-prejudice-analysis.org"
echo -e "- API documentation: https://api.legal-prejudice-analysis.org"
echo -e "- Downloads portal: https://downloads.legal-prejudice-analysis.org"
echo -e "- Community forum: https://forum.legal-prejudice-analysis.org"

echo -e "${YELLOW}Note: It may take up to 24 hours for DNS changes to propagate.${NC}"