# Deploying Your Landing Page to GitHub Pages with Custom Domain

This guide will walk you through the process of deploying your Legal Prejudice Analysis landing page to GitHub Pages and configuring it to use your custom domain `legal-prejudice-analysis.com`.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Setting Up GitHub Repository](#setting-up-github-repository)
3. [Configuring GitHub Pages](#configuring-github-pages)
4. [Setting Up Your Custom Domain](#setting-up-your-custom-domain)
5. [Configuring SSL/TLS](#configuring-ssltls)
6. [Updating Your Landing Page](#updating-your-landing-page)
7. [Troubleshooting](#troubleshooting)

## Prerequisites

Before you begin, make sure you have:

- A GitHub account
- Git installed on your local machine
- Access to your domain registrar's DNS settings for `legal-prejudice-analysis.com`
- The landing page files we've created

## Setting Up GitHub Repository

### Step 1: Create a New Repository (if not already done)

1. Go to GitHub and sign in to your account
2. Click the "+" icon in the top-right corner and select "New repository"
3. Name your repository `legal-prejudice-analysis` (or any name you prefer)
4. Add a description: "Landing page for Legal Prejudice Analysis"
5. Choose "Public" visibility (recommended for GitHub Pages)
6. Initialize with a README
7. Click "Create repository"

### Step 2: Clone the Repository Locally

```bash
git clone https://github.com/yourusername/legal-prejudice-analysis.git
cd legal-prejudice-analysis
```

### Step 3: Add Landing Page Files

1. Copy all files from the `landing-page` directory to your repository:

```bash
# Assuming you're in the repository directory
cp -r /path/to/landing-page/* .
```

2. Commit and push the files:

```bash
git add .
git commit -m "Add landing page files"
git push origin main
```

## Configuring GitHub Pages

### Step 1: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click on "Settings" (tab near the top)
3. Scroll down to the "GitHub Pages" section
4. Under "Source", select "main" branch
5. Click "Save"

GitHub will provide you with a URL where your site is published (usually `https://yourusername.github.io/legal-prejudice-analysis/`).

### Step 2: Choose a Publishing Source

For a simple landing page like this, publishing from the root of the main branch is recommended. However, if you want to keep your landing page separate from other repository content, you can:

1. Create a `docs` folder in your repository
2. Move all landing page files into that folder
3. In GitHub Pages settings, select "main" branch and "/docs" folder as the source

## Setting Up Your Custom Domain

### Step 1: Add a CNAME File to Your Repository

1. Create a file named `CNAME` (no file extension) in the root of your repository (or in the `docs` folder if you're publishing from there)
2. Add your domain name to this file:

```
legal-prejudice-analysis.com
```

3. Commit and push this file:

```bash
git add CNAME
git commit -m "Add CNAME file for custom domain"
git push origin main
```

### Step 2: Configure DNS Settings

You need to configure your domain's DNS settings to point to GitHub Pages. Log in to your domain registrar's website and add the following records:

#### Option 1: Apex Domain (legal-prejudice-analysis.com)

Add these A records pointing to GitHub Pages' IP addresses:

```
A    @    185.199.108.153
A    @    185.199.109.153
A    @    185.199.110.153
A    @    185.199.111.153
```

#### Option 2: www Subdomain (www.legal-prejudice-analysis.com)

Add a CNAME record:

```
CNAME    www    yourusername.github.io.
```

#### Option 3: Both Apex and www (recommended)

Add both the A records for the apex domain AND the CNAME record for the www subdomain. Then, in your GitHub repository settings, you can choose whether the www or non-www version is the primary domain.

### Step 3: Configure Custom Domain in GitHub

1. Go to your repository settings
2. Scroll down to the "GitHub Pages" section
3. In the "Custom domain" field, enter `legal-prejudice-analysis.com`
4. Click "Save"
5. Check "Enforce HTTPS" once the certificate is provisioned (may take up to 24 hours)

## Configuring SSL/TLS

GitHub Pages automatically provisions and manages SSL certificates for custom domains. To enable HTTPS:

1. After adding your custom domain, wait for GitHub to provision a certificate (up to 24 hours)
2. Once the certificate is ready, check the "Enforce HTTPS" option in the GitHub Pages settings

This ensures your site is always served over a secure connection.

## Updating Your Landing Page

To update your landing page in the future:

1. Make changes to the files locally
2. Test the changes locally if possible
3. Commit and push the changes:

```bash
git add .
git commit -m "Update landing page"
git push origin main
```

GitHub Pages will automatically rebuild and deploy your site, usually within a minute or two.

## Troubleshooting

### Custom Domain Not Working

1. **DNS Propagation**: DNS changes can take up to 48 hours to propagate. Wait at least 24 hours before troubleshooting further.
2. **Verify DNS Records**: Double-check your DNS records at your domain registrar.
3. **Check CNAME File**: Ensure your CNAME file contains only your domain name with no additional text or whitespace.
4. **GitHub Pages Status**: Check if GitHub Pages is experiencing any issues at [GitHub Status](https://www.githubstatus.com/).

### HTTPS Not Available

1. **Wait Longer**: It can take up to 24 hours for GitHub to provision an SSL certificate.
2. **DNS Configuration**: Ensure your DNS is correctly configured.
3. **Contact GitHub Support**: If HTTPS is still not available after 24 hours, contact GitHub support.

### Page Not Updating

1. **Check Build Status**: Look for any error messages in the "GitHub Pages" section of your repository settings.
2. **Clear Cache**: Try clearing your browser cache or viewing the site in an incognito/private window.
3. **Wait a Few Minutes**: GitHub Pages can take a few minutes to rebuild and deploy your site.

## Additional Resources

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Managing a Custom Domain for GitHub Pages](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)
- [Troubleshooting Custom Domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/troubleshooting-custom-domains-and-github-pages)