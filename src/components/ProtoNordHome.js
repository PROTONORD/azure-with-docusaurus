import React from 'react';
import styles from './ProtoNordHome.module.css';

const ProtoNordHome = () => {
  return (
    <div className={styles.protonordHome}>
      {/* Hero Section */}
      <section className={styles.hero}>
        <div className={styles.heroContent}>
          <h1 className={styles.heroTitle}>PROTONORD</h1>
          <p className={styles.heroSubtitle}>Fra idé til virkelighet med Azure Static Web Apps</p>
          <div className={styles.heroFeatures}>
            <div className={styles.feature}>
              <div className={styles.featureIcon}>☁️</div>
              <h3>Azure Hosting</h3>
              <p>Automatisk deployment til Azure Static Web Apps med GitHub Actions</p>
            </div>
            <div className={styles.feature}>
              <div className={styles.featureIcon}>⚡</div>
              <h3>Rask deployment</h3>
              <p>Endringer publiseres automatisk ved hver commit til main branch</p>
            </div>
            <div className={styles.feature}>
              <div className={styles.featureIcon}>🔧</div>
              <h3>Docusaurus Wiki</h3>
              <p>Kraftig dokumentasjonsplattform basert på React</p>
            </div>
            <div className={styles.feature}>
              <div className={styles.featureIcon}>🛒</div>
              <h3>Shopify Integrasjon</h3>
              <p>Automatisk synkronisering av produktdata fra Shopify Admin API</p>
            </div>
          </div>
        </div>
      </section>

      {/* Stats Section */}
      <section className={styles.stats}>
        <div className={styles.statsGrid}>
          <div className={styles.statCard}>
            <div className={styles.statNumber}>100%</div>
            <div className={styles.statLabel}>Automatisk</div>
          </div>
          <div className={styles.statCard}>
            <div className={styles.statNumber}>24/7</div>
            <div className={styles.statLabel}>Tilgjengelig</div>
          </div>
          <div className={styles.statCard}>
            <div className={styles.statNumber}>161</div>
            <div className={styles.statLabel}>Shopify Produkter</div>
          </div>
          <div className={styles.statCard}>
            <div className={styles.statNumber}>∞</div>
            <div className={styles.statLabel}>Skalerbart</div>
          </div>
        </div>
      </section>

      {/* Services Section */}
      <section className={styles.services}>
        <h2>Azure Static Web Apps Features</h2>
        <div className={styles.servicesGrid}>
          <div className={styles.serviceCard}>
            <div className={styles.serviceIcon}>🚀</div>
            <h3>Automatisk Deployment</h3>
            <p>GitHub Actions workflow deployer automatisk ved push til main branch med konfigurert app_location: / og output_location: build</p>
          </div>
          <div className={styles.serviceCard}>
            <div className={styles.serviceIcon}>🔐</div>
            <h3>Gratis SSL Sertifikat</h3>
            <p>Azure Static Web Apps tilbyr automatisk SSL-sertifikat for sikker HTTPS-tilkobling.</p>
          </div>
          <div className={styles.serviceCard}>
            <div className={styles.serviceIcon}>🌐</div>
            <h3>Global CDN</h3>
            <p>Innebygd Content Delivery Network for rask lasting verden over.</p>
          </div>
          <div className={styles.serviceCard}>
            <div className={styles.serviceIcon}>🛒</div>
            <h3>Shopify API Integrasjon</h3>
            <p>Automatisk henting av produktdata fra Shopify butikk med filtering på aktive produkter og sikker API-tilgang.</p>
          </div>
          <div className={styles.serviceCard}>
            <div className={styles.serviceIcon}>☁️</div>
            <h3>Cloud Files Tilgang</h3>
            <p>Planlagt integrasjon med rclone for tilgang til Google Drive og Jottacloud filer direkte fra nettstedet.</p>
          </div>
        </div>
      </section>

      {/* Development Process */}
      <section className={styles.process}>
        <h2>Deployment Process</h2>
        <div className={styles.processGrid}>
          <div className={styles.processStep}>
            <div className={styles.stepNumber}>1</div>
            <h3>Code Push</h3>
            <p>Push kode til GitHub repository main branch</p>
          </div>
          <div className={styles.processStep}>
            <div className={styles.stepNumber}>2</div>
            <h3>GitHub Actions</h3>
            <p>Automatisk trigger av build og deployment workflow</p>
          </div>
          <div className={styles.processStep}>
            <div className={styles.stepNumber}>3</div>
            <h3>Shopify Sync</h3>
            <p>Henter produktdata fra Shopify API og oppdaterer lokale data filer</p>
          </div>
          <div className={styles.processStep}>
            <div className={styles.stepNumber}>4</div>
            <h3>Docusaurus Build</h3>
            <p>npm run build genererer statiske filer til build/ mappe</p>
          </div>
          <div className={styles.processStep}>
            <div className={styles.stepNumber}>5</div>
            <h3>Azure Deploy</h3>
            <p>Statiske filer deployeres til Azure Static Web Apps</p>
          </div>
        </div>
      </section>

      {/* Footer Info */}
      <section className={styles.footer}>
        <div className={styles.footerContent}>
          <div className={styles.footerInfo}>
            <h3>Om Dette Prosjektet</h3>
            <p>
              Dette er en Docusaurus-basert wiki og dokumentasjonsside som automatisk deployes til Azure Static Web Apps. 
              Prosjektet demonstrerer moderne web-deployment med GitHub Actions og Azure-integrering samt Shopify API-integrasjon.
            </p>
          </div>
          <div className={styles.footerLinks}>
            <h3>Teknologier</h3>
            <div className={styles.socialLinks}>
              <span>⚛️ React/Docusaurus</span>
              <span>☁️ Azure Static Web Apps</span>
              <span>🔄 GitHub Actions</span>
              <span>🛒 Shopify Admin API</span>
            </div>
          </div>
        </div>
        <div className={styles.footerBottom}>
          <p>© 2025, PROTONORD - Azure Static Web Apps Demo</p>
          <p>Automatisk deployment med GitHub Actions og Shopify integrasjon</p>
        </div>
      </section>
    </div>
  );
};

export default ProtoNordHome;
