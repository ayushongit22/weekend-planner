import json

def load_cuisines():
    with open('pdp.json', 'r') as file:
        data = json.load(file)
        
    # Navigate to the cuisine facet list
    cards = data['data']['success']['cards']
    for card in cards:
        if '@type' in card['card']['card'] and 'type.googleapis.com/swiggy.gandalf.widgets.v2.InlineViewFilterSortWidget' in card['card']['card']['@type']:
            facet_list = card['card']['card']['facetList']
            for facet in facet_list:
                if facet['id'] == 'catalog_cuisines':
                    return facet['facetInfo']
    return []

def display_cuisine_menu():
    cuisines = load_cuisines()
    if not cuisines:
        print("No cuisines found in the data")
        return None
    
    print("\nAvailable Cuisines:")
    print("------------------")
    for idx, cuisine in enumerate(cuisines, 1):
        print(f"{idx}. {cuisine['label']}")
    
    while True:
        try:
            choice = int(input("\nEnter the number of your chosen cuisine (0 to exit): "))
            if choice == 0:
                return None
            if 1 <= choice <= len(cuisines):
                selected_cuisine = cuisines[choice-1]
                return {
                    'label': selected_cuisine['label'],
                    'id': selected_cuisine['id']
                }
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    selected = display_cuisine_menu()
    if selected:
        print(f"\nYou selected: {selected['label']}")
        print(f"Cuisine ID: {selected['id']}")