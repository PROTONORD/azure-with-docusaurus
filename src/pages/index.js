import React from 'react';
import ProtoNordHome from '@site/src/components/ProtoNordHome';
import Layout from '@theme/Layout';

export default function HomePage() {
  return (
    <Layout
      title="ProtoNord - Azure Static Web Apps Demo"
      description="Docusaurus website demonstrating automatic deployment to Azure Static Web Apps with GitHub Actions">
      <ProtoNordHome />
    </Layout>
  );
}