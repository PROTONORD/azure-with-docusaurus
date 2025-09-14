---
sidebar_position: 3
---

# Azure Static Web Apps Deployment

Guide for automatisk deployment av Docusaurus til Azure Static Web Apps med GitHub Actions.

## 🚀 Oppsett av Azure Static Web Apps

### 1. Opprett Azure Static Web App

1. Logg inn på [Azure Portal](https://portal.azure.com)
2. Søk etter "Static Web Apps" og klikk "Create"
3. Fyll ut:
   - **Subscription**: Velg din subscription
   - **Resource Group**: Opprett ny eller velg eksisterende
   - **Name**: `azure-with-docusaurus` (eller ønsket navn)
   - **Plan type**: Free (for utvikling/test)
   - **Region**: Velg nærmeste region (f.eks. West Europe)

### 2. GitHub Integration

1. Under "Deployment details":
   - **Source**: GitHub
   - **GitHub account**: Koble til din GitHub-konto
   - **Organization**: PROTONORD
   - **Repository**: azure-with-docusaurus
   - **Branch**: main (eller din standard branch)

### 3. Build Configuration

Konfigurer build-innstillinger:
- **App location**: `/` (rot av repository)
- **Api location**: (la stå tom for statisk side)
- **Output location**: `build` (hvor Docusaurus bygger filene)

## 📁 GitHub Actions Workflow

Azure oppretter automatisk en GitHub Actions workflow-fil i `.github/workflows/`. 
Her er eksempel på hvordan filen skal se ut:

```yaml
name: Azure Static Web Apps CI/CD

on:
  push:
    branches:
      - main
  pull_request:
    types: [opened, synchronize, reopened, closed]
    branches:
      - main

jobs:
  build_and_deploy_job:
    if: github.event_name == 'push' || (github.event_name == 'pull_request' && github.event.action != 'closed')
    runs-on: ubuntu-latest
    name: Build and Deploy Job
    steps:
      - uses: actions/checkout@v3
        with:
          submodules: true

      - name: Build And Deploy
        id: builddeploy
        uses: Azure/static-web-apps-deploy@v1
        with:
          azure_static_web_apps_api_token: ${{ secrets.AZURE_STATIC_WEB_APPS_API_TOKEN }}
          repo_token: ${{ secrets.GITHUB_TOKEN }}
          action: "upload"
          app_location: "/" # App source code path
          api_location: "" # Api source code path - optional
          output_location: "build" # Built app content directory

  close_pull_request_job:
    if: github.event_name == 'pull_request' && github.event.action == 'closed'
    runs-on: ubuntu-latest
    name: Close Pull Request Job
    steps:
      - name: Close Pull Request
        id: closepullrequest
        uses: Azure/static-web-apps-deploy@v1
        with:
          azure_static_web_apps_api_token: ${{ secrets.AZURE_STATIC_WEB_APPS_API_TOKEN }}
          action: "close"
```

## ⚙️ Build Process

### Docusaurus Build Kommandoer

Azure Static Web Apps bruker disse standardkommandoene:

1. **Install**: `npm install`
2. **Build**: `npm run build`

Docusaurus bygger til `build/` mappen, som matcher `output_location: "build"`.

### Custom Build Script (hvis nødvendig)

Hvis du trenger tilpasset build-prosess, kan du legge til en `build.sh` fil:

```bash
#!/bin/bash
echo "Starting custom build process..."

# Install dependencies
npm install

# Run Docusaurus build
npm run build

echo "Build completed successfully!"
```

## 🔧 Miljøvariabler og Secrets

### Påkrevde Secrets

GitHub repository trenger denne secret-en (Azure setter den automatisk):
- `AZURE_STATIC_WEB_APPS_API_TOKEN`: API token for deployment

### Custom Environment Variables

Hvis du trenger miljøvariabler i build-prosessen, legg dem til i Azure Portal:

1. Gå til din Static Web App i Azure Portal
2. Velg "Configuration" i venstre meny
3. Legg til under "Application settings":
   - `NODE_ENV=production`
   - Andre miljøvariabler etter behov

## 🌐 Custom Domain (valgfritt)

### Sett opp eget domene

1. I Azure Portal, gå til din Static Web App
2. Velg "Custom domains" i venstre meny
3. Klikk "Add" og følg veiviseren
4. Oppdater DNS-innstillinger hos domeneleverandør

### SSL Certificate

Azure Static Web Apps gir automatisk SSL-sertifikat for custom domains.

## 📊 Monitoring og Logging

### Build Logs

Se build-logger i:
1. **GitHub Actions**: Repository → Actions → Velg workflow run
2. **Azure Portal**: Static Web App → "Functions" → "Application Insights"

### Performance Monitoring

Azure gir innebygd monitoring for:
- Response times
- Error rates  
- Geographic distribution
- Resource usage

## 🔍 Feilsøking

### Vanlige build-feil

#### Node.js versjon
```yaml
# Legg til i workflow for å spesifisere Node.js versjon
- name: Setup Node.js
  uses: actions/setup-node@v3
  with:
    node-version: '18'
```

#### Cache for raskere bygg
```yaml
- name: Cache dependencies
  uses: actions/cache@v3
  with:
    path: ~/.npm
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-node-
```

#### Build minne-problemer
```yaml
- name: Increase memory limit
  run: export NODE_OPTIONS="--max-old-space-size=4096"
```

### Debugging Tips

1. **Sjekk build logs** i GitHub Actions
2. **Test lokalt** med `npm run build`
3. **Verifiser** at `build/` mappen inneholder statiske filer
4. **Kontroller** at alle dependencies er i `package.json`

## 🚀 Best Practices

### Optimization

1. **Minifiser bilder** før deploy
2. **Bruk CDN** for store assets
3. **Aktiver caching** for statiske ressurser
4. **Komprimer output** med gzip

### Security

1. **Ikke commit secrets** til Git
2. **Bruk miljøvariabler** for sensitive data
3. **Konfigurer Content Security Policy**
4. **Aktiver HTTPS redirect**

### Performance

1. **Code splitting** med Docusaurus
2. **Lazy loading** av komponenter
3. **Optimiser font loading**
4. **Minimer CSS og JavaScript**

## 📈 Kostnader

### Free Tier Limits

Azure Static Web Apps Free tier inkluderer:
- **Bandwidth**: 100 GB/måned
- **Storage**: 0.5 GB
- **Custom domains**: Ubegrenset
- **SSL certificates**: Gratis
- **Build minutes**: 500/måned

### Overvåking av bruk

Sjekk bruk i Azure Portal under "Metrics" for å unngå overforbruk.