# Azure Docusaurus Static Web App

En Docusaurus-basert wiki og dokumentasjonsside som automatisk deployes til Azure Static Web Apps med GitHub Actions. Prosjektet er basert på innhold fra [PROTONORD/project-lifecycle-manager](https://github.com/PROTONORD/project-lifecycle-manager) repositoryet.

## 🚀 Live Demo

Nettsiden er tilgjengelig på: https://lively-moss-0296dab03.1.azurestaticapps.net/

## 📋 Oversikt

Dette prosjektet demonstrerer:
- **Docusaurus v3** som dokumentasjonsplattform
- **Azure Static Web Apps** for hosting
- **GitHub Actions** for automatisk deployment
- **React komponenter** for interaktive sider
- **Responsivt design** med dark/light mode support

## 🛠️ Teknologi Stack

- **Frontend**: Docusaurus v3, React, CSS Modules
- **Hosting**: Azure Static Web Apps
- **CI/CD**: GitHub Actions
- **Package Manager**: npm
- **Build Output**: Statiske HTML/CSS/JS filer

## ⚙️ GitHub Actions Konfiguration

Automatisk deployment er satt opp med følgende parametere:

```yaml
app_location: "/"        # Rot av repository
output_location: "build" # Hvor Docusaurus bygger statiske filer
api_location: ""         # Ingen API (kun statisk side)
```

### Workflow Triggers
- **Push til main branch**: Deployer automatisk til produksjon
- **Pull requests**: Oppretter preview-miljø
- **PR lukkes**: Sletter preview-miljø

## 🏗️ Prosjektstruktur

```
azure-with-docusaurus/
├── .github/
│   └── workflows/
│       └── azure-static-web-apps.yml  # GitHub Actions workflow
├── docs/                              # Dokumentasjon (Markdown)
│   ├── intro.md                       # Introduksjon
│   ├── cloud-storage.md               # Cloud storage guide
│   ├── backup-system.md               # Backup system dokumentasjon
│   └── azure-deployment.md            # Azure deployment guide
├── src/                               # React komponenter og sider
│   ├── components/
│   │   ├── ProtoNordHome.js           # Hovedside komponent
│   │   └── ProtoNordHome.module.css   # Stilark
│   ├── pages/
│   │   ├── index.js                   # Hjem side
│   │   ├── cloud-files.js             # Cloud filer side
│   │   └── shopify.js                 # Shopify dashboard side
│   └── css/
│       └── custom.css                 # Global stilark
├── static/                            # Statiske filer
│   └── img/
│       ├── logo.svg                   # Logo
│       └── favicon.ico                # Favicon
├── docusaurus.config.js               # Hovedkonfigurasjon
├── sidebars.js                        # Sidebar konfigurasjon
└── package.json                       # Dependencies og scripts
```

## 🔧 Lokal Utvikling

### Forutsetninger
- Node.js 18+ 
- npm eller yarn

### Installasjon og Start

```bash
# Klon repositoryet
git clone https://github.com/PROTONORD/azure-with-docusaurus.git
cd azure-with-docusaurus

# Installer dependencies
npm install

# Start utviklingsserver
npm start
```

Nettsiden vil være tilgjengelig på `http://localhost:3001`

### Nyttige Kommandoer

```bash
# Bygg for produksjon
npm run build

# Forhåndsvis bygget side
npm run serve

# Clear cache (hvis problemer)
npm run clear

# Generer oversettelser
npm run write-translations
```

## 🌐 Azure Static Web Apps Setup

### 1. Opprett Azure Static Web App

1. Logg inn på [Azure Portal](https://portal.azure.com)
2. Søk etter "Static Web Apps" og klikk "Create"
3. Konfigurer:
   - **Resource Group**: Velg eller opprett ny
   - **Name**: `azure-with-docusaurus`
   - **Plan**: Free (for testing)
   - **Region**: West Europe
   - **Source**: GitHub
   - **Repository**: `PROTONORD/azure-with-docusaurus`
   - **Branch**: `main`
   - **App location**: `/`
   - **Output location**: `build`

### 2. Automatisk GitHub Integration

Azure oppretter automatisk:
- GitHub secret `AZURE_STATIC_WEB_APPS_API_TOKEN`
- Workflow fil `.github/workflows/azure-static-web-apps.yml`

### 3. Custom Domain (valgfritt)

Konfigurer eget domene i Azure Portal under "Custom domains".

## 📦 Deployment Process

### Automatisk Deployment

1. **Code push** til main branch
2. **GitHub Actions** triggers workflow
3. **Dependencies** installeres med `npm install`
4. **Build** kjører `npm run build` (genererer til `build/`)
5. **Deploy** til Azure Static Web Apps

### Manual Deployment

```bash
# Bygg lokalt
npm run build

# Deploy via Azure CLI (krever setup)
az staticwebapp deploy --name azure-with-docusaurus --source build/
```

## 🎨 Features og Komponenter

### ProtoNordHome Komponent
- **Responsivt design** som fungerer på alle enheter
- **Dark/Light mode** support automatisk
- **Gradients og animasjoner** for moderne utseende
- **Grid layouts** for optimal organisering av innhold

### Dokumentasjon
- **Automatisk sidebar** generering basert på filstruktur
- **Versjonering** og internationalisering støtte
- **Søkefunksjon** innebygd i Docusaurus
- **Markdown** med React komponenter

### Sider
- **Hjem**: Oversikt og introduksjon
- **Cloud Files**: Placeholder for filhåndtering
- **Shopify**: Placeholder for e-handel integrasjon
- **Docs**: Strukturert dokumentasjon

## 🔍 SEO og Performance

### Optimalisering
- **Statiske filer** for rask lasting
- **CDN** via Azure Static Web Apps
- **Komprimering** automatisk aktivert
- **PWA** støtte via Docusaurus

### Metadata
- **Title tags** og beskrivelser konfigurert
- **Open Graph** metadata for sosiale medier
- **Structured data** via Docusaurus

## 🛡️ Sikkerhet

### Azure Static Web Apps
- **Automatisk HTTPS** med SSL sertifikat
- **Content Security Policy** kan konfigureres
- **Rate limiting** innebygd
- **DDoS protection** via Azure

### GitHub Actions
- **Secrets management** for API tokens
- **Permission-based** deployment
- **Audit trail** for alle deployments

## 📊 Overvåking og Analytics

### Azure Portal
- **Request metrics** og response times
- **Error tracking** og logging
- **Geographic distribution** av brukere
- **Performance insights**

### Tilgjengelige Metrics
- Page views og unique visitors
- Load times og performance
- Error rates og status codes
- Geographic og device statistics

## 🚨 Feilsøking

### Vanlige Build Problemer

#### Node.js Version
```yaml
# Legg til i workflow hvis problemer
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
# Øk memory limit i workflow
- name: Build with more memory
  run: NODE_OPTIONS="--max-old-space-size=4096" npm run build
```

### Azure Issues

#### Deployment Fails
1. Sjekk GitHub Actions logs
2. Verifiser Azure Static Web Apps API token
3. Kontroller at `build/` mappen inneholder filer
4. Test lokal build først

#### Custom Domain
1. Konfigurer DNS CNAME til Azure Static Web Apps URL
2. Vent på SSL sertifikat provisjonering (kan ta opptil 24 timer)
3. Sjekk domain validation i Azure Portal

## 📈 Videre Utvikling

### Planlagte Features
- [ ] Implementer cloud files utforsker
- [ ] Legg til Shopify dashboard funksjonalitet
- [ ] Konfigurer analytics og tracking
- [ ] Optimalisere for bedre performance
- [ ] Legg til automatiske tester

### Potensielle Forbedringer
- **API Routes**: Legg til serverless functions
- **Database**: Koble til Azure Cosmos DB
- **Authentication**: Implementer brukerinnlogging
- **Real-time**: WebSockets for live updates

## 📚 Basert på PROTONORD/project-lifecycle-manager

Dette prosjektet er basert på innhold fra det opprinnelige repositoryet:
- **Dokumentasjonsinnhold** hentet og tilpasset
- **React komponenter** forenklet for statisk hosting
- **Design og styling** beholdt og forbedret
- **Prosjektstruktur** optimalisert for Azure deployment

### Viktigste Endringer
1. **Fjernet server-side dependencies** (Python scripts, Shopify API)
2. **Forenklet React komponenter** til statisk innhold
3. **Lagt til Azure Static Web Apps** deployment workflow
4. **Optimalisert for statisk hosting** uten backend

## 🤝 Bidrag

1. Fork repositoryet
2. Opprett feature branch (`git checkout -b feature/ny-funksjon`)
3. Commit endringene (`git commit -m 'Legg til ny funksjon'`)
4. Push til branch (`git push origin feature/ny-funksjon`)
5. Opprett Pull Request

## 📄 Lisens

Dette prosjektet er proprietært for PROTONORD AS.

---

**Sist oppdatert**: Januar 2025  
**Versjon**: 1.0  
**Vedlikeholdt av**: PROTONORD Development Team

## 📞 Kontakt

For spørsmål eller support, kontakt PROTONORD development team.

**Live URL**: [Kommer når Azure Static Web App er opprettet]  
**GitHub**: https://github.com/PROTONORD/azure-with-docusaurus
