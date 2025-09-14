import React from 'react';
import Layout from '@theme/Layout';

export default function CloudFiles() {
  return (
    <Layout title="Cloud Files" description="Cloud file management and storage">
      <div style={{ padding: '2rem' }}>
        <h1>☁️ Cloud Files</h1>
        <p>Her vil cloud fil-oversikten være tilgjengelig når den er implementert.</p>
        <div style={{ 
          padding: '2rem', 
          backgroundColor: 'var(--ifm-color-emphasis-100)', 
          borderRadius: '8px',
          margin: '2rem 0'
        }}>
          <h3>Kommende funksjoner:</h3>
          <ul>
            <li>Filutforsker for cloud storage</li>
            <li>Sync med Google Drive og Jottacloud</li>
            <li>Automatisk katalogisering</li>
            <li>rclone integrasjon</li>
          </ul>
        </div>
        <p>Se <a href="/docs/cloud-storage">dokumentasjonen</a> for mer informasjon om cloud storage setup.</p>
      </div>
    </Layout>
  );
}