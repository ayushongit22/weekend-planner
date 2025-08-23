import json

# Read the JSON file
with open('pdp.json', 'r') as file:
    data = json.load(file)

# Extract the offers object
offers = data['props']['pageProps']['widgetResponse']['success']['cards'][2]['card']['card']['offers']

# Function to extract offer details
def extract_offer_details(offer):
    return {
        'title': offer.get('title', ''),
        'subtitle': offer.get('subtitle', ''),
        'offerDetails': {
            'title': offer.get('offerDetails', {}).get('title', ''),
            'subtitle': offer.get('offerDetails', {}).get('subtitle', '')
        }
    }

# Extract details from all types of offers
all_offers = []

# Extract from vendor offer
if 'vendorOffer' in offers:
    all_offers.append(extract_offer_details(offers['vendorOffer']))

# Extract from deal offer
if 'dealOffer' in offers:
    all_offers.append(extract_offer_details(offers['dealOffer']))

# Extract from deal offers array
if 'dealOffers' in offers:
    for deal in offers['dealOffers']:
        all_offers.append(extract_offer_details(deal))

# Print the extracted offers
print(json.dumps(all_offers, indent=2))