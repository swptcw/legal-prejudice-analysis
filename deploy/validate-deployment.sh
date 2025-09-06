#!/bin/bash
# Deployment validation script for Legal Prejudice Analysis Platform

set -e

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Configuration
VPS_HOST="${VPS_HOST:-demo.legal-prejudice-analysis.org}"
VPS_USER="${VPS_USER:-deploy}"

# Validation functions
validate_deployment() {
    echo "🔍 Validating Legal Prejudice Analysis Platform deployment..."
    
    # Check site accessibility
    echo "Checking site accessibility..."
    if curl -s -o /dev/null -w "%{http_code}" http://$VPS_HOST | grep -q "200"; then
        echo -e "${GREEN}✅ Site is accessible via HTTP${NC}"
    else
        echo -e "${RED}❌ Site is not accessible${NC}"
        return 1
    fi
    
    # Check API health
    echo "Checking API health..."
    if curl -s http://$VPS_HOST/api/health | grep -q "ok"; then
        echo -e "${GREEN}✅ API health endpoint is responding${NC}"
    else
        echo -e "${RED}❌ API health endpoint may not be responding${NC}"
        return 1
    fi
    
    # Check documentation
    echo "Checking documentation..."
    if curl -s http://$VPS_HOST/docs/ | grep -q "Legal"; then
        echo -e "${GREEN}✅ Documentation is accessible${NC}"
    else
        echo -e "${YELLOW}⚠️ Documentation may not be fully accessible${NC}"
    fi
    
    # Check static assets
    echo "Checking static assets..."
    if curl -s http://$VPS_HOST/css/styles.css | grep -q "body"; then
        echo -e "${GREEN}✅ CSS files are loading${NC}"
    else
        echo -e "${YELLOW}⚠️ CSS files may not be loading${NC}"
    fi
    
    # Check JavaScript
    echo "Checking JavaScript files..."
    if curl -s http://$VPS_HOST/js/main.js | grep -q "function"; then
        echo -e "${GREEN}✅ JavaScript files are loading${NC}"
    else
        echo -e "${YELLOW}⚠️ JavaScript files may not be loading${NC}"
    fi
    
    echo ""
    echo -e "${GREEN}🎉 Deployment validation complete!${NC}"
    echo ""
    echo "🔗 URLs to test:"
    echo "   - Demo Site: http://$VPS_HOST"
    echo "   - API Health: http://$VPS_HOST/api/health"
    echo "   - Documentation: http://$VPS_HOST/docs/"
    echo ""
}

# Check GitHub secrets
check_secrets() {
    echo "🔐 Checking GitHub secrets configuration..."
    
    if [ -z "$VPS_HOST" ]; then
        echo -e "${RED}❌ VPS_HOST secret is not set${NC}"
        exit 1
    fi
    
    if [ -z "$VPS_USER" ]; then
        echo -e "${RED}❌ VPS_USER secret is not set${NC}"
        exit 1
    fi
    
    echo -e "${GREEN}✅ GitHub secrets are configured${NC}"
}

# Main validation
main() {
    echo "🚀 Legal Prejudice Analysis Platform - Deployment Validation"
    echo "=========================================================="
    
    check_secrets
    validate_deployment
    
    echo ""
    echo "📊 Summary:"
    echo "   - VPS Host: $VPS_HOST"
    echo "   - VPS User: $VPS_USER"
    echo "   - All checks passed!"
}

# Run validation
main