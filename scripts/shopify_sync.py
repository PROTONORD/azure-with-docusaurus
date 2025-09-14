#!/usr/bin/env python3
"""
Shopify Product Sync for ProtoNord Azure Docusaurus
Synkroniserer produktdata fra Shopify API (kun aktive og publiserte produkter)
"""

import json
import requests
import os
import sys
from datetime import datetime
from pathlib import Path
import logging

# Legg til scripts-mappen til Python-path
sys.path.append(str(Path(__file__).parent))

from config import config

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ShopifySync:
    def __init__(self):
        self.store_url = config.SHOPIFY_STORE_URL
        self.access_token = config.SHOPIFY_ACCESS_TOKEN
        self.api_version = config.SHOPIFY_API_VERSION
        self.base_url = f"https://{self.store_url}/admin/api/{self.api_version}"
        self.headers = {
            "X-Shopify-Access-Token": self.access_token,
            "Content-Type": "application/json"
        }
        self.timestamp = datetime.now().isoformat()
        
        # Opprett output-mappe
        self.output_dir = Path(__file__).parent / "static" / "data"
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Også kopier til static/data for Docusaurus
        self.docusaurus_dir = Path(__file__).parent.parent / "static" / "data"
        self.docusaurus_dir.mkdir(parents=True, exist_ok=True)

    def make_request(self, endpoint: str) -> dict:
        """Gjør API-forespørsel til Shopify"""
        url = f"{self.base_url}/{endpoint}"
        
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"API-feil: {e}")
            return {}

    def get_all_products(self) -> list:
        """Hent alle produkter med paginering"""
        products = []
        page_info = None
        
        while True:
            if page_info:
                endpoint = f"products.json?limit=250&page_info={page_info}"
            else:
                endpoint = "products.json?limit=250"
                
            response = self.make_request(endpoint)
            
            if not response or 'products' not in response:
                break
                
            batch_products = response['products']
            products.extend(batch_products)
            
            logger.info(f"Hentet {len(batch_products)} produkter (totalt: {len(products)})")
            
            # Sjekk om det er flere sider
            link_header = None  # Shopify bruker Link header for paginering
            if len(batch_products) < 250:
                break
                
        return products

    def process_product_data(self, products: list) -> dict:
        """
        Prosesser produktdata til strukturert format
        
        Filtrerer automatisk bort:
        - Arkiverte produkter (status != 'active')
        - Upubliserte produkter (published_at er null)
        - Utkast (draft status)
        
        Dette sikrer at kun produkter som er synlige i butikken publiseres på websiden.
        """
        logger.info("🔄 Prosesserer produktdata...")
        
        # Filtrer bare aktive og publiserte produkter
        active_products = [
            product for product in products 
            if product.get("status") == "active" and product.get("published_at")
        ]
        
        logger.info(f"📊 Filtrerte {len(products)} produkter ned til {len(active_products)} aktive og publiserte")
        
        processed = {
            "sync_timestamp": self.timestamp,
            "total_products": len(active_products),
            "products": [],
            "categories": {},
            "vendors": {},
            "product_types": {}
        }
        
        for product in active_products:
            # Basis produktinfo
            product_data = {
                "id": product.get("id"),
                "title": product.get("title"),
                "handle": product.get("handle"),
                "vendor": product.get("vendor"),
                "product_type": product.get("product_type"),
                "status": product.get("status"),
                "created_at": product.get("created_at"),
                "updated_at": product.get("updated_at"),
                "published_at": product.get("published_at"),
                "tags": product.get("tags", "").split(", ") if product.get("tags") else [],
                "variants": len(product.get("variants", [])),
                "images": len(product.get("images", [])),
                "description": product.get("body_html", "")[:200] + "..." if len(product.get("body_html", "")) > 200 else product.get("body_html", "")
            }
            
            processed["products"].append(product_data)
            
            # Statistikk per kategori
            product_type = product.get("product_type", "Ukjent")
            if product_type not in processed["product_types"]:
                processed["product_types"][product_type] = 0
            processed["product_types"][product_type] += 1
            
            # Statistikk per leverandør
            vendor = product.get("vendor", "Ukjent")
            if vendor not in processed["vendors"]:
                processed["vendors"][vendor] = 0
            processed["vendors"][vendor] += 1
            
            # Kategoristatistikk basert på tags
            for tag in product_data["tags"]:
                if tag not in processed["categories"]:
                    processed["categories"][tag] = 0
                processed["categories"][tag] += 1
        
        logger.info(f"✅ Prosessert {len(processed['products'])} produkter")
        return processed

    def save_shopify_data(self, data: dict):
        """Lagre Shopify data til JSON fil"""
        output_file = self.output_dir / "shopify-products.json"
        
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            logger.info(f"✅ Shopify data lagret til {output_file}")
            
            # Kopier også til Docusaurus static directory
            docusaurus_file = self.docusaurus_dir / "shopify-products.json"
            with open(docusaurus_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
        except Exception as e:
            logger.error(f"❌ Feil ved lagring av Shopify data: {e}")

    def save_summary(self, data: dict):
        """Lagre sammendrag av Shopify data"""
        summary = {
            "sync_timestamp": data["sync_timestamp"],
            "total_products": data["total_products"],
            "categories": data["categories"],
            "vendors": data["vendors"], 
            "product_types": data["product_types"]
        }
        
        # Lagre i scripts/static/data
        output_file = self.output_dir / "shopify-summary.json"
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(summary, f, indent=2, ensure_ascii=False)
            logger.info(f"✅ Shopify sammendrag lagret til {output_file}")
        except Exception as e:
            logger.error(f"❌ Feil ved lagring av sammendrag: {e}")
            
        # Lagre i static/data for Docusaurus
        docusaurus_file = self.docusaurus_dir / "shopify-summary.json"
        try:
            with open(docusaurus_file, 'w', encoding='utf-8') as f:
                json.dump(summary, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error(f"❌ Feil ved lagring av Docusaurus sammendrag: {e}")

    def sync(self):
        """Hovedfunksjon for synkronisering"""
        if not config.has_shopify_config():
            print("❌ Shopify credentials ikke konfigurert")
            return False
            
        logger.info("🛍️ Starter Shopify produktsynkronisering...")
        
        # Hent produkter
        logger.info("📦 Henter produkter fra Shopify...")
        products = self.get_all_products()
        
        if not products:
            logger.error("❌ Ingen produkter hentet")
            return False
            
        logger.info(f"✅ Totalt hentet {len(products)} produkter")
        
        # Prosesser data
        processed_data = self.process_product_data(products)
        
        # Lagre data
        self.save_shopify_data(processed_data)
        self.save_summary(processed_data)
        
        logger.info("✅ Shopify synkronisering fullført!")
        return True

def main():
    """Hovedfunksjon"""
    print("🛍️ ProtoNord Shopify Sync")
    print("=" * 40)
    
    sync = ShopifySync()
    success = sync.sync()
    
    if success:
        print("✅ Shopify synkronisering fullført!")
        return 0
    else:
        print("❌ Shopify synkronisering feilet!")
        return 1

if __name__ == "__main__":
    exit(main())