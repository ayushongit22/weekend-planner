import urllib.parse
import json
from curl_cffi import requests
import jmespath
from parsel import Selector

def load_cuisines(add,lat,lng):
    
    cookies = {
    '_device_id': '6878b61d-3d72-6ade-4964-99f19869737c',
    '__SW': 'Q9VW4sjmKgs-U3YfZLdLEQfox5iXiQl1',
    '_gcl_au': '1.1.285494118.1746211374',
    '_gid': 'GA1.2.1030471882.1746211375',
    'fontsLoaded': '1',
    '_guest_tid': '6143549f-1f6e-46bd-8587-3e2344c1440e',
    'userLocation': add,
    '_gat_0': '1',
    '_ga': 'GA1.1.215497375.1746211374',
    '_ga_YE38MFJRBZ': 'GS1.1.1746298290.5.1.1746299410.0.0.0',
    '_ga_34JYJ0BCRN': 'GS2.1.s1746298290$o5$g1$t1746299411$j0$l0$h0',
}

    headers = {
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    'latitude': str(lat),
    'longitude': str(lng),
    'origin': 'https://www.swiggy.com',
    'priority': 'u=1, i',
    'referer': 'https://www.swiggy.com/city/ahmedabad',
    'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    # 'cookie': '_device_id=6878b61d-3d72-6ade-4964-99f19869737c; __SW=Q9VW4sjmKgs-U3YfZLdLEQfox5iXiQl1; _gcl_au=1.1.285494118.1746211374; _gid=GA1.2.1030471882.1746211375; fontsLoaded=1; _guest_tid=6143549f-1f6e-46bd-8587-3e2344c1440e; userLocation=%7B%22lat%22%3A23.0120338%2C%22lng%22%3A72.51075399999999%2C%22address%22%3A%22Prahlad%20Nagar%2C%20Ahmedabad%2C%20Gujarat%20380015%2C%20India%22%2C%22area%22%3A%22ahmedabad%22%7D; _gat_0=1; _ga=GA1.1.215497375.1746211374; _ga_YE38MFJRBZ=GS1.1.1746298290.5.1.1746299410.0.0.0; _ga_34JYJ0BCRN=GS2.1.s1746298290$o5$g1$t1746299411$j0$l0$h0',
}


    params = {
        'lat': lat,
        'lng': lng,
        'apiV2': 'true',
    }

    json_data = {
        'tags': 'layout_dineout_seo',
        'isFiltered': False,
        'sortAttribute': '',
        'queryId': 'seo-data-d999b5d9-b552-4773-9680-8f81e98023db',
        'metaMap': {
            'locality': '',
            'ambienceTag': '',
            'restaurantCategory': '',
            'allCuisines': '',
            'landmarkName': '',
            'brandId': '',
            'dinersoneTag': '',
        },
        'seoParams': {
            'apiName': 'DOCollectionApi',
            'brandId': '',
            'seoUrl': 'www.swiggy.com/city/ahmedabad',
            'pageType': 'DO_CITY_PAGE',
            'businessLine': 'DINEOUT',
        },
        'facets': {},
    }

    response = requests.post(
        'https://www.swiggy.com/api/seo/getListing',
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
        impersonate='chrome110',
    )
    if response.status_code == 200:
        with open('pdp.json', 'w') as file:
            json.dump(response.json(), file, indent=4)
        data=response.json()
        cards = data['data']['success']['cards']
        for card in cards:
            if '@type' in card['card']['card'] and 'type.googleapis.com/swiggy.gandalf.widgets.v2.InlineViewFilterSortWidget' in card['card']['card']['@type']:
                facet_list = card['card']['card']['facetList']
                for facet in facet_list:
                    if facet['id'] == 'catalog_cuisines':
                        return facet['facetInfo']
        return []
    else:
        return None

def display_cuisine_menu(add,lat,lng):
    cuisines = load_cuisines(add,lat,lng)
    print(cuisines)
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
                return None
        except ValueError:
            print("Please enter a valid number.")
            return None

def get_place_id(location):

    cookies = {
        '_device_id': '6878b61d-3d72-6ade-4964-99f19869737c',
        '_guest_tid': 'seo_data-973d7170-abe6-4c5b-8802-a03e52fabf1b',
        '__SW': 'Q9VW4sjmKgs-U3YfZLdLEQfox5iXiQl1',
        '_gcl_au': '1.1.285494118.1746211374',
        '_gid': 'GA1.2.1030471882.1746211375',
        'userLocation': '%7B%22lat%22%3A22.9798586%2C%22lng%22%3A72.502735%2C%22address%22%3A%22Sarkhej-Okaf%2C%20Gujarat%2C%20India%22%2C%22area%22%3A%22sarkhej-okaf%22%7D',
        'location': '%7B%22lat%22%3A22.9798586%2C%22lng%22%3A72.502735%2C%22address%22%3A%22Sarkhej-Okaf%2C%20Gujarat%2C%20India%22%2C%22area%22%3A%22sarkhej-okaf%22%7D',
        '_ga_YE38MFJRBZ': 'GS1.1.1746211374.1.1.1746212539.0.0.0',
        '_ga_34JYJ0BCRN': 'GS1.1.1746211374.1.1.1746212539.0.0.0',
        '_ga': 'GA1.2.215497375.1746211374',
        '_gat_0': '1',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        'if-none-match': 'W/"c6b-7LYD2/iJjip8yQP0QqKLUD86OP4"',
        'priority': 'u=1, i',
        'referer': 'https://www.swiggy.com/restaurants-near-me',
        'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
        # 'cookie': '_device_id=6878b61d-3d72-6ade-4964-99f19869737c; _guest_tid=seo_data-973d7170-abe6-4c5b-8802-a03e52fabf1b; __SW=Q9VW4sjmKgs-U3YfZLdLEQfox5iXiQl1; _gcl_au=1.1.285494118.1746211374; _gid=GA1.2.1030471882.1746211375; userLocation=%7B%22lat%22%3A22.9798586%2C%22lng%22%3A72.502735%2C%22address%22%3A%22Sarkhej-Okaf%2C%20Gujarat%2C%20India%22%2C%22area%22%3A%22sarkhej-okaf%22%7D; location=%7B%22lat%22%3A22.9798586%2C%22lng%22%3A72.502735%2C%22address%22%3A%22Sarkhej-Okaf%2C%20Gujarat%2C%20India%22%2C%22area%22%3A%22sarkhej-okaf%22%7D; _ga_YE38MFJRBZ=GS1.1.1746211374.1.1.1746212539.0.0.0; _ga_34JYJ0BCRN=GS1.1.1746211374.1.1.1746212539.0.0.0; _ga=GA1.2.215497375.1746211374; _gat_0=1',
    }

    params = {
        'input': location,
        'type': '',
    }

    response = requests.get(
    'https://www.swiggy.com/dapi/misc/place-autocomplete',
    params=params,
    # cookies=cookies,
    headers=headers)
    if response.status_code == 200:
        place_id=jmespath.search('data[0].place_id',response.json())
        return place_id
    else:
        return None
def get_address(place_id):
    cookies = {
        '_device_id': '6878b61d-3d72-6ade-4964-99f19869737c',
        '_guest_tid': 'seo_data-973d7170-abe6-4c5b-8802-a03e52fabf1b',
        '__SW': 'Q9VW4sjmKgs-U3YfZLdLEQfox5iXiQl1',
        '_gcl_au': '1.1.285494118.1746211374',
        '_gid': 'GA1.2.1030471882.1746211375',
        'userLocation': '%7B%22lat%22%3A22.9798586%2C%22lng%22%3A72.502735%2C%22address%22%3A%22Sarkhej-Okaf%2C%20Gujarat%2C%20India%22%2C%22area%22%3A%22sarkhej-okaf%22%7D',
        'location': '%7B%22lat%22%3A22.9798586%2C%22lng%22%3A72.502735%2C%22address%22%3A%22Sarkhej-Okaf%2C%20Gujarat%2C%20India%22%2C%22area%22%3A%22sarkhej-okaf%22%7D',
        '_ga_YE38MFJRBZ': 'GS1.1.1746211374.1.1.1746212539.0.0.0',
        '_ga_34JYJ0BCRN': 'GS1.1.1746211374.1.1.1746212539.0.0.0',
        '_ga': 'GA1.2.215497375.1746211374',
        '_gat_0': '1',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        'if-none-match': 'W/"2fb-3bp3DzIqbJGPaJnlIbIhm5NBOBg"',
        'priority': 'u=1, i',
        'referer': 'https://www.swiggy.com/restaurants-near-me',
        'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
        # 'cookie': '_device_id=6878b61d-3d72-6ade-4964-99f19869737c; _guest_tid=seo_data-973d7170-abe6-4c5b-8802-a03e52fabf1b; __SW=Q9VW4sjmKgs-U3YfZLdLEQfox5iXiQl1; _gcl_au=1.1.285494118.1746211374; _gid=GA1.2.1030471882.1746211375; userLocation=%7B%22lat%22%3A22.9798586%2C%22lng%22%3A72.502735%2C%22address%22%3A%22Sarkhej-Okaf%2C%20Gujarat%2C%20India%22%2C%22area%22%3A%22sarkhej-okaf%22%7D; location=%7B%22lat%22%3A22.9798586%2C%22lng%22%3A72.502735%2C%22address%22%3A%22Sarkhej-Okaf%2C%20Gujarat%2C%20India%22%2C%22area%22%3A%22sarkhej-okaf%22%7D; _ga_YE38MFJRBZ=GS1.1.1746211374.1.1.1746212539.0.0.0; _ga_34JYJ0BCRN=GS1.1.1746211374.1.1.1746212539.0.0.0; _ga=GA1.2.215497375.1746211374; _gat_0=1',
    }

    params = {
        'place_id': place_id,
    }

    response = requests.get(
        'https://www.swiggy.com/dapi/misc/address-recommend',
        params=params,
        headers=headers)
    if response.status_code == 200:
        lat=jmespath.search('data[0].geometry.location.lat',response.json())
        lng=jmespath.search('data[0].geometry.location.lng',response.json())
        address=jmespath.search('data[0].formatted_address',response.json())
        area=jmespath.search('data[0].address_components[0].long_name',response.json())
        address_json={
            'lat':lat,
            'lng':lng,
            'address':address,
            'area':area
        }
        return address_json,lat,lng
    else:
        return None
def get_restaurants(cuisine_id,encoded_address,lat,lng):
    

    cookies = {
        '_device_id': '6878b61d-3d72-6ade-4964-99f19869737c',
        '__SW': 'Q9VW4sjmKgs-U3YfZLdLEQfox5iXiQl1',
        '_gcl_au': '1.1.285494118.1746211374',
        '_gid': 'GA1.2.1030471882.1746211375',
        'fontsLoaded': '1',
        '_guest_tid': '6143549f-1f6e-46bd-8587-3e2344c1440e',
        'x-web-checkout-flow': 'dineoutcart',
        'userLocation': encoded_address,
        'location': encoded_address,
        '_ga': 'GA1.1.215497375.1746211374',
        '_ga_YE38MFJRBZ': 'GS1.1.1746287653.3.1.1746287696.0.0.0',
        '_ga_34JYJ0BCRN': 'GS2.1.s1746287653$o3$g1$t1746287697$j0$l0$h0',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        'latitude': '23.0120338',
        'longitude': '72.51075399999999',
        'origin': 'https://www.swiggy.com',
        'priority': 'u=1, i',
        'referer': 'https://www.swiggy.com/restaurants-near-me',
        'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    }

    params = {
        'lat': lat,
        'lng': lng,
        'apiV2': 'true',
    }

    # # Get cuisine selection from user
    # print("\nDo you want to filter by cuisine? (y/n): ")
    # choice = input().lower()
    
    # # Initialize facets
    # facets = {}
    # isFiltered=False
    # if choice == 'y':
    #     isFiltered=True
    #     selected_cuisine = display_cuisine_menu(encoded_address,lat,lng)
    #     if selected_cuisine:
    #         facets = {
    #             'catalog_cuisines': [
    #                 {
    #                     'value': selected_cuisine['id']
    #                 }
    #             ]
    #         }
    if cuisine_id:
        isFiltered=True
        facets = {
                    'catalog_cuisines': [
                        {
                            'value': cuisine_id
                        }
                    ]
                }
    else:
        isFiltered=False
        facets = {}
    json_data = {
        'tags': 'layout_dineout_seo',
        'isFiltered': isFiltered,
        'sortAttribute': '',
        'queryId': 'seo-data-bf3c027a-6314-4eb7-b4d7-4f63b41ab46c',
        'metaMap': {
            'locality': '',
            'ambienceTag': '',
            'restaurantCategory': '',
            'allCuisines': '',
            'landmarkName': '',
            'brandId': '',
            'dinersoneTag': '',
        },
        'seoParams': {
            'apiName': 'DOCollectionApi',
            'brandId': '',
            'seoUrl': 'www.swiggy.com/restaurants-near-me',
            'pageType': 'DO_NEAR_ME_PAGE',
            'businessLine': 'DINEOUT',
        },
        'facets': facets
    }

    response = requests.post(
        'https://www.swiggy.com/api/seo/getListing',
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    if response.status_code == 200:
        with open('pdp.json', 'w') as file:
            json.dump(response.json(), file, indent=4)
        json_data=response.json()
        restayrants_url=[]
        for restaurant in jmespath.search('data.success.cards[1].card.card.gridElements.infoWithStyle.restaurants',json_data):
            restaurant_url=jmespath.search('cta.link',restaurant)
            restayrants_url.append(restaurant_url)
        return restayrants_url
    else:
        print("Failed to retrieve restaurants.")
        return None

def get_restaurant_details(link):
    cookies = {
    'deviceId': 's%3Abf78c218-e7f9-4f04-b540-d17aed4e8851.wyN9mLTIHzFC8bZ7%2BkxZkCVa9BzAZNh87NfzS0PcqL4',
    'versionCode': '1200',
    'platform': 'web',
    'subplatform': 'dweb',
    'statusBarHeight': '0',
    'bottomOffset': '0',
    'genieTrackOn': 'false',
    'isNative': 'false',
    'openIMHP': 'false',
    'addressId': 's%3A.4Wx2Am9WLolnmzVcU32g6YaFDw0QbIBFRj2nkO7P25s',
    'webBottomBarHeight': '0',
    '_gcl_au': '1.1.1616147151.1744179870',
    '_fbp': 'fb.1.1744179870386.28986454615278261',
    '__SW': 'DJ-yh28h0S0tp3nf_k6bkS8MLcDzcsAX',
    '_device_id': '92d6f4d5-fa54-d26f-2622-16efaf45517e',
    'fontsLoaded': '1',
    'lat': 's%3A28.4594965.DB41%2BR75i8extjUTcYtManLeoZ4w9iC5%2BnVhmIsVR%2Fs',
    'lng': 's%3A77.0266383.7L0gBRJhuGHt0ylK16iJE3e6Pg4%2BGI%2Fsl%2BLFTFdwBLQ',
    'address': 's%3AGurugram%2C%20Haryana%2C%20India.EVDQWUvgRpCz6UWZfF%2FfhbIkj4qXMLwukHZu5wI4rLA',
    'tid': 's%3A45257690-5284-4b42-b543-bbf5f9b7b3f8.r7aaou9goXgcG1PECMowkMJktK4lau34KvW82U7qmDM',
    '_ga_0XZC5MS97H': 'GS1.1.1744208551.2.1.1744211333.0.0.0',
    '_ga_VEG1HFE5VZ': 'GS1.1.1744208550.2.1.1744211333.0.0.0',
    '_ga_8N8XRG907L': 'GS1.1.1744208550.5.1.1744211333.0.0.0',
    '_guest_tid': 'b86867ab-e0da-4ca5-80bb-d26c2a40c331',
    '_sid': 'k5rd399c-5756-4c72-8108-03c06e11b11c',
    '_gid': 'GA1.2.1077586132.1745229002',
    'dadl': 'true',
    'userLocation': '{%22lat%22:23.022505%2C%22lng%22:72.5713621%2C%22address%22:%22Ahmedabad%2C%20Gujarat%2C%20India%22%2C%22area%22:%22%22%2C%22showUserDefaultAddressHint%22:false}',
    '_gat_0': '1',
    '_ga_YE38MFJRBZ': 'GS1.1.1745229002.1.1.1745230426.0.0.0',
    '_ga_34JYJ0BCRN': 'GS1.1.1745229002.2.1.1745230426.0.0.0',
    '_ga': 'GA1.2.1617159752.1744179870',
}

    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.swiggy.com/brunch-restaurants-dineout-near-me',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    # 'cookie': 'deviceId=s%3Abf78c218-e7f9-4f04-b540-d17aed4e8851.wyN9mLTIHzFC8bZ7%2BkxZkCVa9BzAZNh87NfzS0PcqL4; versionCode=1200; platform=web; subplatform=dweb; statusBarHeight=0; bottomOffset=0; genieTrackOn=false; isNative=false; openIMHP=false; addressId=s%3A.4Wx2Am9WLolnmzVcU32g6YaFDw0QbIBFRj2nkO7P25s; webBottomBarHeight=0; _gcl_au=1.1.1616147151.1744179870; _fbp=fb.1.1744179870386.28986454615278261; __SW=DJ-yh28h0S0tp3nf_k6bkS8MLcDzcsAX; _device_id=92d6f4d5-fa54-d26f-2622-16efaf45517e; fontsLoaded=1; lat=s%3A28.4594965.DB41%2BR75i8extjUTcYtManLeoZ4w9iC5%2BnVhmIsVR%2Fs; lng=s%3A77.0266383.7L0gBRJhuGHt0ylK16iJE3e6Pg4%2BGI%2Fsl%2BLFTFdwBLQ; address=s%3AGurugram%2C%20Haryana%2C%20India.EVDQWUvgRpCz6UWZfF%2FfhbIkj4qXMLwukHZu5wI4rLA; tid=s%3A45257690-5284-4b42-b543-bbf5f9b7b3f8.r7aaou9goXgcG1PECMowkMJktK4lau34KvW82U7qmDM; _ga_0XZC5MS97H=GS1.1.1744208551.2.1.1744211333.0.0.0; _ga_VEG1HFE5VZ=GS1.1.1744208550.2.1.1744211333.0.0.0; _ga_8N8XRG907L=GS1.1.1744208550.5.1.1744211333.0.0.0; _guest_tid=b86867ab-e0da-4ca5-80bb-d26c2a40c331; _sid=k5rd399c-5756-4c72-8108-03c06e11b11c; _gid=GA1.2.1077586132.1745229002; dadl=true; userLocation={%22lat%22:23.022505%2C%22lng%22:72.5713621%2C%22address%22:%22Ahmedabad%2C%20Gujarat%2C%20India%22%2C%22area%22:%22%22%2C%22showUserDefaultAddressHint%22:false}; _gat_0=1; _ga_YE38MFJRBZ=GS1.1.1745229002.1.1.1745230426.0.0.0; _ga_34JYJ0BCRN=GS1.1.1745229002.2.1.1745230426.0.0.0; _ga=GA1.2.1617159752.1744179870',
}

    # URL to fetch
    

    try:
        # Make the request
        response = requests.get(link, headers=headers, cookies=cookies)
        if response.status_code != 200:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
            return None
        response.raise_for_status()
        
        # Parse HTML content
        selector = Selector(text=response.text)
        
        # Extract JSON data from script tag
        script_element = selector.xpath('//script[@id="__NEXT_DATA__"]/text()').get()
        # print(script_element)
        if script_element:
            # print(script_element)
            json_data = json.loads(script_element)
            restaurant_details = {}
        
        # Get restaurant ID
            # restaurant_details['restaurant_id'] = json_data['props']['pageProps']['restaurantId']
            
            # Navigate to restaurant info section
            restaurant_info = None
            for card in json_data['props']['pageProps']['widgetResponse']['success']['cards']:
                if '@type' in card['card']['card'] and 'RestaurantShortInfo' in card['card']['card']['@type']:
                    restaurant_info = card['card']['card']
                    break
            
            if restaurant_info:
                # Extract basic details
                restaurant_details['restaurant_name'] = restaurant_info['name']
                # Split locality and get city (last part)
                locality_parts = restaurant_info['locality'].split(',')
                restaurant_details['city'] = locality_parts[-1].strip()
                restaurant_details['address'] = restaurant_info['locationInfo']['address']
                # restaurant_details['latitude'] = restaurant_info['locationInfo']['lat']
                # restaurant_details['longitude'] = restaurant_info['locationInfo']['long']
                
                # Join cuisines with comma
                restaurant_details['cuisines'] = ','.join(restaurant_info['cuisines'])
                
                # Extract cost for two
                for info in restaurant_info['infoList']:
                    if info.get('subtitle') == 'for two':
                        restaurant_details['cost_for_two'] = info['title'].strip("₹")
                        break
                
                # Extract and format rating
                for info in restaurant_info['infoList']:
                    if info.get('type') == 'INFO_TYPE_RATING':
                        # restaurant_details['rating'] = float(info['title'])
                        restaurant_details['rating'] = info['title']
                        break
                
                # Extract phone number
                restaurant_details['phone'] = restaurant_info['contactInfo'][0]['text']['subtitle']
                
                # Format timing
                timing_text = "Mon-Sun : "
                if 'outletTiming' in restaurant_info['serviceability']:
                    timing = restaurant_info['serviceability']['outletTiming']['infoList'][0]['subtitle']
                    timing = timing.replace('Noon', '12noon')
                    timing = timing.replace('·', ',')
                    restaurant_details['opening_hours'] = timing_text + timing

            # Extract facilities
            for card in json_data['props']['pageProps']['widgetResponse']['success']['cards']:
                if '@type' in card['card']['card'] and 'RestaurantFacilities' in card['card']['card']['@type']:
                    facilities = card['card']['card']['element']
                    restaurant_details['features'] = '|'.join([f['text'] for f in facilities])
                    break
            offers_list = []
            for card in json_data['props']['pageProps']['widgetResponse']['success']['cards']:
                if '@type' in card['card']['card'] and 'type.googleapis.com/swiggy.dinersone.dineoutdiscovery.webview.v1.RestaurantOfferInfo' in card['card']['card']['@type']:
                    offers = card['card']['card']['offers']
                    
                    # Extract vendor offer if exists
                    if 'vendorOffer' in offers:
                        offer = offers['vendorOffer']
                        offers_list.append({
                            'title': offer.get('title', 'N/A'),
                            'subtitle': offer.get('subtitle', 'N/A'),
                            'offerDetails': {
                                'title': offer.get('offerDetails', {}).get('title', 'N/A'),
                                'subtitle': offer.get('offerDetails', {}).get('subtitle', 'N/A')
                            }
                        })
                    
                    # Extract deal offers if exists
                    if 'dealOffers' in offers:
                        for deal in offers['dealOffers']:
                            offers_list.append({
                                'title': deal.get('title', 'N/A'),
                                'subtitle': deal.get('subtitle', 'N/A'),
                                'offerDetails': {
                                    'title': deal.get('offerDetails', {}).get('title', 'N/A'),
                                    'subtitle': deal.get('offerDetails', {}).get('subtitle', 'N/A')
                                }
                            })
            
            restaurant_details['offers'] = offers_list
            restaurant_details['book_your_table']= "N/A"
            element_type=jmespath.search("props.pageProps.widgetResponse.success.cards",json_data)
            for element in element_type:
                # print(jmespath.search('card.card."@type"',element))
                if jmespath.search('card.card."@type"',element) == "type.googleapis.com/swiggy.dinersone.dineoutdiscovery.webview.v1.TableBookingCTA":
                    book_table_link = jmespath.search('card.card.cta.link',element)
                    restaurant_details['book_your_table'] = book_table_link  
                    break
            
            
            # get directions
            restaurant_details['directions'] = "N/A"
            for link in element_type:
                if jmespath.search('card.card."@type"',link) == "type.googleapis.com/swiggy.dinersone.dineoutdiscovery.webview.v1.RestaurantLocation":
                    lat=jmespath.search('card.card.locationInfo.lat',link)
                    long=jmespath.search('card.card.locationInfo.long',link)
                    if lat and long:
                        directions=f"https://www.google.com/maps?q={lat},{long}"
                        restaurant_details['directions'] = directions
                        break
            restaurant_details['photos'] = "N/A"
            restaurant_details['menu'] = "N/A"
            for pm in element_type:
                if jmespath.search('card.card."@type"',pm) == "type.googleapis.com/swiggy.gandalf.widgets.v2.RestaurantBlTab":
                    for tab in jmespath.search('card.card.tabs',pm):
                        if jmespath.search('title',tab) == "Photos":
                            photos=jmespath.search('cta',tab)
                            restaurant_details['photos'] = photos
                        if jmespath.search('title',tab) == "Menu":  
                            menu=jmespath.search('cta',tab)
                            restaurant_details['menu'] = menu
            return restaurant_details
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
def process_restaurant_urls(urls):
    if urls:
        result=[]
        for link in urls:
            data=get_restaurant_details(link)
            if data:
                result.append(data)
            else:
                continue
        return result
def main(location):     
    place_id=get_place_id(location)
    if place_id:
        address_json,lat,lng=get_address(place_id)
        if address_json and lat and lng:
            encoded_address = urllib.parse.quote(json.dumps(address_json))
            cuisines = load_cuisines(encoded_address,lat,lng)
            if cuisines:
                return cuisines,encoded_address,lat,lng
            else:
                print("Failed to retrieve cuisines.")
                return None
            # links=get_restaurants(encoded_address,lat,lng)
            # if links:
            #     result=[]
            #     for link in links:
            #         data=get_restaurant_details(link)
            #         if data:
            #             result.append(data)
            #         else:
            #             continue
            #     with open('restaurant_details.json', 'w') as file:
            #         json.dump(result, file, indent=4)

            # else:
            #     print("Failed to retrieve restaurants.")
        else:
            print("Failed to retrieve address.")
    else:
        print("Failed to retrieve place_id.")