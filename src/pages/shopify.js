import React from 'react';
import Layout from '@theme/Layout';

export default function Shopify() {
  return (
    <Layout title="Shopify Dashboard" description="Shopify integration and dashboard">
      <div style={{ padding: '2rem' }}>
        <h1>🛍️ Shopify Dashboard</h1>
        <p>Her vil Shopify dashboard være tilgjengelig når det er implementert.</p>
        <div style={{ 
          padding: '2rem', 
          backgroundColor: 'var(--ifm-color-emphasis-100)', 
          borderRadius: '8px',
          margin: '2rem 0'
        }}>
          <h3>Kommende funksjoner:</h3>
          <ul>
            <li>Produktoversikt og statistikk</li>
            <li>Bestillingsovervåking</li>
            <li>Lagerstatistikk</li>
            <li>Shopify API integrasjon</li>
            <li>Real-time data synkronisering</li>
          </ul>
        </div>
        <p>Dashboard vil vise:</p>
        <ul>
          <li><strong>Produkter:</strong> Oversikt over alle produkter i Shopify</li>
          <li><strong>Bestillinger:</strong> Statistikk og trender</li>
          <li><strong>Lagerstatus:</strong> Real-time oversikt</li>
          <li><strong>Integrasjon:</strong> Kobling mellom filserver og Shopify-produkter</li>
        </ul>
      </div>
    </Layout>
  );
}