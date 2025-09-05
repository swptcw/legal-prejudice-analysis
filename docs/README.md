# Legal Prejudice Analysis Documentation Hub

This directory contains the complete documentation hub for the Legal Prejudice Analysis project, including the main documentation site and placeholder pages for specialized subdomains.

## Directory Structure

```
docs_new/                           # Main documentation directory
├── CNAME                           # CNAME file for docs.legal-prejudice-analysis.org
├── README.md                       # This file
├── api/                            # API documentation subdomain
│   ├── CNAME                       # CNAME file for api.legal-prejudice-analysis.org
│   └── index.html                  # API documentation placeholder page
├── assets/                         # Shared assets for all documentation
│   ├── css/                        # CSS stylesheets
│   ├── favicon.png                 # Favicon
│   ├── images/                     # Images and graphics
│   └── js/                         # JavaScript files
├── case-studies/                   # Case studies section
│   └── index.html                  # Case studies documentation
├── demo/                           # Interactive demo subdomain
│   ├── CNAME                       # CNAME file for demo.legal-prejudice-analysis.org
│   └── index.html                  # Demo placeholder page
├── downloads/                      # Downloads portal subdomain
│   ├── CNAME                       # CNAME file for downloads.legal-prejudice-analysis.org
│   └── index.html                  # Downloads placeholder page
├── forum/                          # Community forum subdomain
│   ├── CNAME                       # CNAME file for forum.legal-prejudice-analysis.org
│   └── index.html                  # Forum placeholder page
├── framework/                      # Framework documentation section
│   └── index.html                  # Framework documentation
├── index.html                      # Main documentation homepage
├── practical-guide/                # Practical guide section
│   └── index.html                  # Practical guide documentation
└── risk-analysis/                  # Risk analysis section
    └── index.html                  # Risk analysis documentation
```

## Deployment

This documentation hub is designed to be deployed to GitHub Pages with custom domain support. Each subdomain has its own CNAME file for proper DNS configuration.

### DNS Configuration

The following DNS records should be configured for the documentation hub:

| Type | Name | Value | TTL |
|------|------|-------|-----|
| A | @ | 185.199.108.153 | 3600 |
| A | @ | 185.199.109.153 | 3600 |
| A | @ | 185.199.110.153 | 3600 |
| A | @ | 185.199.111.153 | 3600 |
| CNAME | www | legal-prejudice-analysis.org. | 3600 |
| CNAME | docs | swptcw.github.io. | 3600 |
| CNAME | demo | swptcw.github.io. | 3600 |
| CNAME | api | swptcw.github.io. | 3600 |
| CNAME | downloads | swptcw.github.io. | 3600 |
| CNAME | forum | swptcw.github.io. | 3600 |

### GitHub Pages Configuration

1. Deploy the contents of this directory to the GitHub Pages branch
2. Enable GitHub Pages in the repository settings
3. Configure GitHub Pages to use the custom domain
4. Ensure HTTPS is enforced

## Development

To make changes to the documentation:

1. Edit the HTML files in the respective directories
2. Update the CSS styles in the assets/css directory
3. Modify the JavaScript functionality in the assets/js directory
4. Test the changes locally before deployment

## Future Enhancements

The following enhancements are planned for future implementation:

1. Interactive risk calculator on the demo subdomain
2. API documentation with interactive examples
3. Downloads portal with templates and resources
4. Community forum for discussion and support

## Contact

For questions or issues related to the documentation hub, please open an issue on the GitHub repository or contact the project maintainers.