# Shopify API Konfigurasjon

## Oppgitt kredittinformasjon

Følgende Shopify API-kreditter er oppgitt for integrasjon:

- **Store URL**: `protonord.myshopify.com`
- **Admin API Access Token**: `shpat_[REDACTED_FOR_SECURITY]`
- **API Key**: `[REDACTED_FOR_SECURITY]`
- **Secret API Key**: `[REDACTED_FOR_SECURITY]`

## Tilgangsnivå

Dette er en read-only API-tilgang som gir følgende muligheter:

- Lese produktdata (produkter, varianter, priser)
- Lese lagerinformasjon
- Lese ordre (hvis tilgjengelig)
- Lese kundedata (hvis tilgjengelig)

**Produktfiltrering**: Systemet henter kun aktive og publiserte produkter. Arkiverte produkter og utkast blir automatisk filtrert bort.

## GitHub Secrets Konfigurasjon

For å konfigurere disse kredentialene i GitHub Secrets:

1. Gå til ditt GitHub repository
2. Klikk på **Settings** > **Secrets and variables** > **Actions**
3. Legg til følgende secrets:

| Secret Navn | Verdi |
|-------------|-------|
| `SHOPIFY_STORE_URL` | `protonord.myshopify.com` |
| `SHOPIFY_ACCESS_TOKEN` | `shpat_[DIN_ACCESS_TOKEN]` |
| `SHOPIFY_API_VERSION` | `2024-07` |

**Merk**: API Key og Secret API Key er ikke nødvendig for Admin API Access Token autentisering.

## Testing av Shopify-integrasjon

Du kan teste Shopify-integrasjonen lokalt ved å:

1. Opprette en `.env` fil i prosjektets root:

```bash
SHOPIFY_STORE_URL=protonord.myshopify.com
SHOPIFY_ACCESS_TOKEN=shpat_[DIN_ACCESS_TOKEN]
SHOPIFY_API_VERSION=2024-07
```

1. Kjøre test-scriptet:

```bash
python3 scripts/shopify_sync.py
```

## Sikkerhet

- Disse kredentialene er kun for lesing og kan ikke modifisere data
- Access token er tidsbegrenset og kan utløpe
- Hold kredentialene konfidensielle og del de aldri offentlig
- Overvåk API-bruk for uvanlig aktivitet

## API-begrensninger

Shopify Admin API har rate limits:

- Standard: 2 requests per sekund
- Plus: 4 requests per sekund
- Shopify Plus: 40 requests per sekund

Vårt script implementerer automatisk rate limiting for å unngå overskridelse.

## Feilsøking

Hvis du får autentiseringsfeil:

1. Sjekk at store URL er korrekt (uten https://)
2. Verifiser at access token ikke har utløpt
3. Kontroller at API-versjonen støttes (2024-07)
4. Sjekk at secret navn i GitHub matches konfigurasjonen

For mer hjelp, se [Shopify Admin API dokumentasjon](https://shopify.dev/docs/api/admin-rest).