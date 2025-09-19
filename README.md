# Azure Docusaurus Static Web App

A Docusaurus-based wiki and documentation site that automatically deploys to Azure Static Web Apps using GitHub Actions. The project is based on content from the [PROTONORD/project-lifecycle-manager](https://github.com/PROTONORD/project-lifecycle-manager) repository.

## 🚀 Live Demo

The website is available at: [https://lively-moss-0296dab03.1.azurestaticapps.net/](https://lively-moss-0296dab03.1.azurestaticapps.net/)

## 📋 Overview

This project demonstrates:

  - **Docusaurus v3** as a documentation platform
  - **Azure Static Web Apps** for hosting
  - **GitHub Actions** for automatic deployment
  - **React components** for interactive pages
  - **Responsive design** with dark/light mode support

## 🛠️ Technology Stack

  - **Frontend**: Docusaurus v3, React, CSS Modules
  - **Hosting**: Azure Static Web Apps
  - **CI/CD**: GitHub Actions
  - **Package Manager**: npm
  - **Build Output**: Static HTML/CSS/JS files

## ⚙️ GitHub Actions Configuration

Automatic deployment is set up with the following parameters:

```yaml
app_location: "/"      # Root of the repository
output_location: "build" # Where Docusaurus builds static files
api_location: ""       # No API (static site only)
```

### Workflow Triggers

  - **Push to main branch**: Deploys automatically to production
  - **Pull requests**: Creates a preview environment
  - **PR closed**: Deletes the preview environment

## 🏗️ Project Structure

```
azure-with-docusaurus/
├── .github/
│   └── workflows/
│       └── azure-static-web-apps.yml  # GitHub Actions workflow
├── docs/                             # Documentation (Markdown)
│   ├── intro.md                      # Introduction
│   ├── cloud-storage.md              # Cloud storage guide
│   ├── backup-system.md              # Backup system documentation
│   └── azure-deployment.md           # Azure deployment guide
├── src/                              # React components and pages
│   ├── components/
│   │   ├── ProtoNordHome.js          # Main page component
│   │   └── ProtoNordHome.module.css  # Stylesheet
│   ├── pages/
│   │   ├── index.js                  # Home page
│   │   ├── cloud-files.js            # Cloud files page
│   │   └── shopify.js                # Shopify dashboard page
│   └── css/
│       └── custom.css                # Global stylesheet
├── static/                           # Static files
│   └── img/
│       ├── logo.svg                  # Logo
│       └── favicon.ico               # Favicon
├── docusaurus.config.js              # Main configuration
├── sidebars.js                       # Sidebar configuration
└── package.json                      # Dependencies and scripts
```

## 🔧 Local Development

### Prerequisites

  - Node.js 18+
  - npm or yarn

### Installation and Startup

```bash
# Clone the repository
git clone https://github.com/PROTONORD/azure-with-docusaurus.git
cd azure-with-docusaurus

# Install dependencies
npm install

# Start the development server
npm start
```

The website will be available at `http://localhost:3001`

### Useful Commands

```bash
# Build for production
npm run build

# Preview the built site
npm run serve

# Clear cache (if issues arise)
npm run clear

# Generate translations
npm run write-translations
```

## 🌐 Azure Static Web Apps Setup

### 1\. Create Azure Static Web App

1.  Log in to the [Azure Portal](https://portal.azure.com)
2.  Search for "Static Web Apps" and click "Create"
3.  Configure:
      - **Resource Group**: Select or create a new one
      - **Name**: `azure-with-docusaurus`
      - **Plan**: Free (for testing)
      - **Region**: West Europe
      - **Source**: GitHub
      - **Repository**: `PROTONORD/azure-with-docusaurus`
      - **Branch**: `main`
      - **App location**: `/`
      - **Output location**: `build`

### 2\. Automatic GitHub Integration

Azure automatically creates:

  - A GitHub secret `AZURE_STATIC_WEB_APPS_API_TOKEN`
  - A workflow file `.github/workflows/azure-static-web-apps.yml`

### 3\. Custom Domain (optional)

Configure your own domain in the Azure Portal under "Custom domains".

## 📦 Deployment Process

### Automatic Deployment

1.  **Code push** to the main branch
2.  **GitHub Actions** triggers the workflow
3.  **Dependencies** are installed with `npm install`
4.  **Build** runs `npm run build` (generates to `build/`)
5.  **Deploy** to Azure Static Web Apps

### Manual Deployment

```bash
# Build locally
npm run build

# Deploy via Azure CLI (requires setup)
az staticwebapp deploy --name azure-with-docusaurus --source build/
```

## 🎨 Features and Components

### ProtoNordHome Component

  - **Responsive design** that works on all devices
  - **Dark/Light mode** support automatically
  - **Gradients and animations** for a modern look
  - **Grid layouts** for optimal content organization

### Documentation

  - **Automatic sidebar** generation based on file structure
  - **Versioning** and internationalization support
  - **Search functionality** built into Docusaurus
  - **Markdown** with React components

### Pages

  - **Home**: Overview and introduction
  - **Cloud Files**: Placeholder for file management
  - **Shopify**: Placeholder for e-commerce integration
  - **Docs**: Structured documentation

## 🔍 SEO and Performance

### Optimization

  - **Static files** for fast loading
  - **CDN** via Azure Static Web Apps
  - **Compression** automatically enabled
  - **PWA** support via Docusaurus

### Metadata

  - **Title tags** and descriptions configured
  - **Open Graph** metadata for social media
  - **Structured data** via Docusaurus

## 🛡️ Security

### Azure Static Web Apps

  - **Automatic HTTPS** with SSL certificate
  - **Content Security Policy** can be configured
  - **Rate limiting** built-in
  - **DDoS protection** via Azure

### GitHub Actions

  - **Secrets management** for API tokens
  - **Permission-based** deployment
  - **Audit trail** for all deployments

## 📊 Monitoring and Analytics

### Azure Portal

  - **Request metrics** and response times
  - **Error tracking** and logging
  - **Geographic distribution** of users
  - **Performance insights**

### Available Metrics

  - Page views and unique visitors
  - Load times and performance
  - Error rates and status codes
  - Geographic and device statistics

## 🚨 Troubleshooting

### Common Build Issues

#### Node.js Version

```yaml
# Add to workflow if issues occur
- name: Setup Node.js
  uses: actions/setup-node@v3
  with:
    node-version: '18'
```

#### Cache Issues

```bash
# Clear all caches
npm run clear
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

#### Build Memory Issues

```yaml
# Increase memory limit in workflow
- name: Build with more memory
  run: NODE_OPTIONS="--max-old-space-size=4096" npm run build
```

### Azure Issues

#### Deployment Fails

1.  Check the GitHub Actions logs
2.  Verify the Azure Static Web Apps API token
3.  Ensure the `build/` folder contains files
4.  Test the local build first

#### Custom Domain

1.  Configure DNS CNAME to the Azure Static Web Apps URL
2.  Wait for SSL certificate provisioning (can take up to 24 hours)
3.  Check domain validation in the Azure Portal

## 📈 Future Development

### Planned Features

  - [ ] Implement a cloud files explorer
  - [ ] Add Shopify dashboard functionality
  - [ ] Configure analytics and tracking
  - [ ] Optimize for better performance
  - [ ] Add automated tests

### Potential Improvements

  - **API Routes**: Add serverless functions
  - **Database**: Connect to Azure Cosmos DB
  - **Authentication**: Implement user login
  - **Real-time**: WebSockets for live updates

## 📚 Based on PROTONORD/project-lifecycle-manager

This project is based on content from the original repository:

  - **Documentation content** has been sourced and adapted
  - **React components** have been simplified for static hosting
  - **Design and styling** have been retained and improved
  - **Project structure** has been optimized for Azure deployment

### Key Changes

1.  **Removed server-side dependencies** (Python scripts, Shopify API)
2.  **Simplified React components** to static content
3.  **Added Azure Static Web Apps** deployment workflow
4.  **Optimized for static hosting** without a backend

## 🤝 Contributing

1.  Fork the repository
2.  Create a feature branch (`git checkout -b feature/new-feature`)
3.  Commit your changes (`git commit -m 'Add new feature'`)
4.  Push to the branch (`git push origin feature/new-feature`)
5.  Create a Pull Request

## 📄 License

This project is proprietary to PROTONORD AS.

-----

**Last updated**: January 2025
**Version**: 1.0
**Maintained by**: PROTONORD Development Team

## 📞 Contact

For questions or support, contact the PROTONORD development team.

**Live URL**: [https://lively-moss-0296dab03.1.azurestaticapps.net/](https://lively-moss-0296dab03.1.azurestaticapps.net/)
**GitHub**: [https://github.com/PROTONORD/azure-with-docusaurus](https://github.com/PROTONORD/azure-with-docusaurus)
