import json
import jmespath
# Read the JSON file
with open('pdp.json', 'r') as file:
    data = json.load(file)

def extract_book_table_link():
    # Navigate through the cards to find the book table link
    # props.pageProps.widgetResponse.success.cards[0].card.card.@type
    element_type=jmespath.search("props.pageProps.widgetResponse.success.cards",data)
    for element in element_type:
        # print(jmespath.search('card.card."@type"',element))
        if jmespath.search('card.card."@type"',element) == "type.googleapis.com/swiggy.dinersone.dineoutdiscovery.webview.v1.TableBookingCTA":
            book_table_link = jmespath.search('card.card.cta.link',element)
            return book_table_link  
    return None

# Extract and print the book table link"
book_table_link = extract_book_table_link()
if book_table_link:
    print(f"Book Table Link: {book_table_link}")
else:
    print("Book table link not found")