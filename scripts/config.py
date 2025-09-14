#!/usr/bin/env python3
"""
Konfigurasjon for ProtoNord Azure Docusaurus deployment
Håndterer miljøvariabler og secrets på en sikker måte
"""

import os
import base64
import tempfile
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv

# Last .env fil hvis den finnes
load_dotenv()

class Config:
    """Sentral konfigurasjonshåndtering"""
    
    def __init__(self):
        # Shopify konfigurasjon
        self.SHOPIFY_STORE_URL = os.getenv('SHOPIFY_STORE_URL')
        self.SHOPIFY_ACCESS_TOKEN = os.getenv('SHOPIFY_ACCESS_TOKEN')
        self.SHOPIFY_API_VERSION = os.getenv('SHOPIFY_API_VERSION', '2024-07')
        
        # Cloud storage credentials
        self.GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
        self.GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
        self.GOOGLE_REFRESH_TOKEN = os.getenv('GOOGLE_REFRESH_TOKEN')
        
        self.JOTTACLOUD_USERNAME = os.getenv('JOTTACLOUD_USERNAME')
        self.JOTTACLOUD_PASSWORD = os.getenv('JOTTACLOUD_PASSWORD')
        
        # rclone konfigurasjon (base64-kodet)
        self.RCLONE_CONFIG = os.getenv('RCLONE_CONFIG')
        
        self.temp_files = []

    def has_shopify_config(self) -> bool:
        """Sjekk om Shopify-konfigurasjon er tilgjengelig"""
        return all([
            self.SHOPIFY_STORE_URL,
            self.SHOPIFY_ACCESS_TOKEN
        ])

    def has_cloud_config(self) -> bool:
        """Sjekk om cloud storage-konfigurasjon er tilgjengelig"""
        return all([
            self.GOOGLE_CLIENT_ID,
            self.GOOGLE_CLIENT_SECRET,
            self.GOOGLE_REFRESH_TOKEN,
            self.JOTTACLOUD_USERNAME,
            self.JOTTACLOUD_PASSWORD,
            self.RCLONE_CONFIG
        ])

    def setup_rclone_config(self) -> Optional[str]:
        """Dekoder og setter opp rclone-konfigurasjon"""
        if not self.RCLONE_CONFIG:
            return None
            
        try:
            # Dekod base64-kodet konfigurasjon
            decoded_config = base64.b64decode(self.RCLONE_CONFIG).decode('utf-8')
            
            # Opprett midlertidig konfigurasjonsfil
            temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.conf')
            temp_file.write(decoded_config)
            temp_file.close()
            
            self.temp_files.append(temp_file.name)
            return temp_file.name
            
        except Exception as e:
            print(f"❌ Feil ved oppsett av rclone-konfigurasjon: {e}")
            return None

    def validate_credentials(self) -> bool:
        """Valider at nødvendige kredentialer er tilgjengelige"""
        missing = []
        
        # Sjekk Shopify
        if not self.SHOPIFY_STORE_URL:
            missing.append('SHOPIFY_STORE_URL')
        if not self.SHOPIFY_ACCESS_TOKEN:
            missing.append('SHOPIFY_ACCESS_TOKEN')
            
        # Sjekk cloud storage
        if not self.GOOGLE_CLIENT_ID:
            missing.append('GOOGLE_CLIENT_ID')
        if not self.GOOGLE_CLIENT_SECRET:
            missing.append('GOOGLE_CLIENT_SECRET')
        if not self.GOOGLE_REFRESH_TOKEN:
            missing.append('GOOGLE_REFRESH_TOKEN')
        if not self.JOTTACLOUD_USERNAME:
            missing.append('JOTTACLOUD_USERNAME')
        if not self.JOTTACLOUD_PASSWORD:
            missing.append('JOTTACLOUD_PASSWORD')
        if not self.RCLONE_CONFIG:
            missing.append('RCLONE_CONFIG')
            
        if missing:
            print(f"❌ Mangler miljøvariabler: {', '.join(missing)}")
            return False
            
        return True

    def cleanup_temp_files(self):
        """Rydd opp midlertidige filer"""
        for temp_file in self.temp_files:
            try:
                if os.path.exists(temp_file):
                    os.unlink(temp_file)
            except Exception as e:
                print(f"⚠️ Kunne ikke slette midlertidig fil {temp_file}: {e}")
        self.temp_files.clear()

    def __del__(self):
        """Destructor - rydd opp automatisk"""
        self.cleanup_temp_files()

# Global konfigurasjon-instans
config = Config()

def main():
    """Test-funksjon for konfigurasjon"""
    print("🔧 ProtoNord Azure Configuration")
    print("=" * 32)
    
    if config.validate_credentials():
        print("✅ Konfigurasjon gyldig")
        
        if config.has_shopify_config():
            print("✅ Shopify credentials tilgjengelig")
        else:
            print("❌ Shopify credentials mangler")
            
        if config.has_cloud_config():
            print("✅ Cloud storage credentials tilgjengelig")
        else:
            print("❌ Cloud storage credentials mangler")
    else:
        print("❌ Konfigurasjon ugyldig - sjekk miljøvariabler")
        return 1
        
    return 0

if __name__ == "__main__":
    exit(main())