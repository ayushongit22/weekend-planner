import hashlib
import os
from parsel import Selector
from curl_cffi import requests
import json
import jmespath
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from movies.cinemas import extract_cinemas

# ---- Configurations ----
MAX_THREADS = 10  # You can increase or decrease based on performance and API limits
cookies = {
    'bmsId': '1.3114045748.1741349222679',
    '_gcl_au': '1.1.1440267025.1741349097',
    '_ga': 'GA1.1.1227075379.1741349097',
    '_fbp': 'fb.1.1741349099960.417382361992121119',
    'tvc_vid': '61741349124903',
    'tvc_bmscookie': 'GA1.2.1227075379.1741349097',
    'newShowtime': '%22https%3A%2F%2Fin.bookmyshow.com%2Fbuytickets%2Fpvr-palladium-mall-ahmedabad%2Fcinema-ahd-PPAM-MT%2F20250307%22',
    'preferences': '%7B%22ticketType%22%3A%22M-TICKET%22%7D',
    'userCine': '%7Cmrs%3DPPAM%3BARED%3B%7C',
    '_uetvid': '64190c80fb4c11ef8dc715bb6c127a39',
    'cto_bundle': 'p-DRAl9BaDZUcUY3dDYxdjhnYSUyQiUyRmNPNSUyRmUzZXd1U3dOQnlLemMzNlMxME1KWVlVeENKbFM4RTljYnBoNDhsQWIlMkYyRnc1QjhlNW9qUEZVeDR6aVZsREZFcjVydmFDRk1vRks2cE1PbGVXTTlvaSUyRktxcGNLa2VYQlV3JTJCU1hRM2NIOVNHUU9YUE9rYXYzN0dlMzZqaTRTTUQzdXclM0QlM0Q',
    'WZRK_G': 'f886bfceabde490c86dc090086e0a092',
    '__cf_bm': 'Rt4IZp_RuejB_QbD0H9ibFvEIy.G4TL3ISR0WxVLQRg-1741500216-1.0.1.1-0VrSAEbJON_PyxNyOFm95PNC0x_DZ1Ll4g2GYR7hjWo_8mIXCG_Porn3MrYqgGxMYGwPAeqTKHEOBg0uXwSR1_Ap4CqYM0c7IiUFA6S_.1E',
    '__cfruid': '74e3077ca5492249c127528ca6bc28c7c0b18e57-1741500216',
    '_cfuvid': 'dCIu76mvMamHfHUmXIRmdS0wJkHEudHlmzow8ubMqGo-1741500216276-0.0.1.1-604800000',
    'cf_clearance': 'lbdSYPhsza_8YSn4EsP8MJ5evOfUmzzaZwIMEoBj7do-1741500217-1.2.1.1-8tRtY32D707laA36IJ3Op798uph3tcrPbz9fhdlrrL3BPJN7mo2rEAvwXKcs4ZGLMbnFxBZ9.Q.KPiWWPNHMMrifW18OMXfaIYRL8l5GAcNy.eptRYLHLWcpNndICZ4MImEhn6t5wN3xclkD09HQyWJqr0hhjWqPyGkZvwqbVuA4V8noumbr02cQm7LJAFPHPHoWnb1O1Sy_0OH.PbOebBiwNkEvL2Hc3rmM5ZN_6k7z_vO8.Q4CVck4jTNdGlzcHiQB9YulG3Ds6Oa4N_nj6RVaNJNSDRJWHMNDBoLqhfcx1YrO4rDeOCEoB4L2q_fMZzzH35XnP5gWuDhW7qgiUejPAVkB04M6jPI6kf4zxd6A9UXxZOn1qgwFHzRQQqFLqSevzhPDWOOiDIKyz91gbxNXLFApdZctLdSZAg1Ju0U',
    'AMP_TOKEN': '%24NOT_FOUND',
    'tvc_bmscookie_gid': 'GA1.2.698529296.1741500084',
    'geoHash': '%22%22',
    'geolocation': '%7B%22x-location-shared%22%3Afalse%2C%22x-location-selection%22%3A%22manual%22%2C%22timestamp%22%3A1741500088588%7D',
    'rgn': '%7B%22regionNameSlug%22%3A%22mumbai%22%2C%22regionCodeSlug%22%3A%22mumbai%22%2C%22regionName%22%3A%22Mumbai%22%2C%22regionCode%22%3A%22MUMBAI%22%2C%22subName%22%3A%22%22%2C%22subCode%22%3A%22%22%2C%22Lat%22%3A%2219.076%22%2C%22Long%22%3A%2272.8777%22%2C%22GeoHash%22%3A%22te7%22%7D',
    '_gat_UA-27207583-8': '1',
    'mrs': '%5B%22CSWO%22%2C%22PPAM%22%5D',
    'platform': '%7B%22segments%22%3A%22%22%7D',
    '_ga_84T5GTD0PC': 'GS1.1.1741500082.3.1.1741500427.33.0.0',
    'WZRK_S_RK4-47R-98KZ': '%7B%22p%22%3A7%2C%22s%22%3A1741500218%2C%22t%22%3A1741500427%7D',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'priority': 'u=0, i',
    'referer': 'https://in.bookmyshow.com/buytickets/cinepolis-nexus-seawoods-navi-mumbai/cinema-mumbai-CSWO-MT/20250309',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'service-worker-navigation-preload': 'true',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    # 'cookie': 'bmsId=1.3114045748.1741349222679; _gcl_au=1.1.1440267025.1741349097; _ga=GA1.1.1227075379.1741349097; _fbp=fb.1.1741349099960.417382361992121119; tvc_vid=61741349124903; tvc_bmscookie=GA1.2.1227075379.1741349097; newShowtime=%22https%3A%2F%2Fin.bookmyshow.com%2Fbuytickets%2Fpvr-palladium-mall-ahmedabad%2Fcinema-ahd-PPAM-MT%2F20250307%22; preferences=%7B%22ticketType%22%3A%22M-TICKET%22%7D; userCine=%7Cmrs%3DPPAM%3BARED%3B%7C; _uetvid=64190c80fb4c11ef8dc715bb6c127a39; cto_bundle=p-DRAl9BaDZUcUY3dDYxdjhnYSUyQiUyRmNPNSUyRmUzZXd1U3dOQnlLemMzNlMxME1KWVlVeENKbFM4RTljYnBoNDhsQWIlMkYyRnc1QjhlNW9qUEZVeDR6aVZsREZFcjVydmFDRk1vRks2cE1PbGVXTTlvaSUyRktxcGNLa2VYQlV3JTJCU1hRM2NIOVNHUU9YUE9rYXYzN0dlMzZqaTRTTUQzdXclM0QlM0Q; WZRK_G=f886bfceabde490c86dc090086e0a092; __cf_bm=Rt4IZp_RuejB_QbD0H9ibFvEIy.G4TL3ISR0WxVLQRg-1741500216-1.0.1.1-0VrSAEbJON_PyxNyOFm95PNC0x_DZ1Ll4g2GYR7hjWo_8mIXCG_Porn3MrYqgGxMYGwPAeqTKHEOBg0uXwSR1_Ap4CqYM0c7IiUFA6S_.1E; __cfruid=74e3077ca5492249c127528ca6bc28c7c0b18e57-1741500216; _cfuvid=dCIu76mvMamHfHUmXIRmdS0wJkHEudHlmzow8ubMqGo-1741500216276-0.0.1.1-604800000; cf_clearance=lbdSYPhsza_8YSn4EsP8MJ5evOfUmzzaZwIMEoBj7do-1741500217-1.2.1.1-8tRtY32D707laA36IJ3Op798uph3tcrPbz9fhdlrrL3BPJN7mo2rEAvwXKcs4ZGLMbnFxBZ9.Q.KPiWWPNHMMrifW18OMXfaIYRL8l5GAcNy.eptRYLHLWcpNndICZ4MImEhn6t5wN3xclkD09HQyWJqr0hhjWqPyGkZvwqbVuA4V8noumbr02cQm7LJAFPHPHoWnb1O1Sy_0OH.PbOebBiwNkEvL2Hc3rmM5ZN_6k7z_vO8.Q4CVck4jTNdGlzcHiQB9YulG3Ds6Oa4N_nj6RVaNJNSDRJWHMNDBoLqhfcx1YrO4rDeOCEoB4L2q_fMZzzH35XnP5gWuDhW7qgiUejPAVkB04M6jPI6kf4zxd6A9UXxZOn1qgwFHzRQQqFLqSevzhPDWOOiDIKyz91gbxNXLFApdZctLdSZAg1Ju0U; AMP_TOKEN=%24NOT_FOUND; tvc_bmscookie_gid=GA1.2.698529296.1741500084; geoHash=%22%22; geolocation=%7B%22x-location-shared%22%3Afalse%2C%22x-location-selection%22%3A%22manual%22%2C%22timestamp%22%3A1741500088588%7D; rgn=%7B%22regionNameSlug%22%3A%22mumbai%22%2C%22regionCodeSlug%22%3A%22mumbai%22%2C%22regionName%22%3A%22Mumbai%22%2C%22regionCode%22%3A%22MUMBAI%22%2C%22subName%22%3A%22%22%2C%22subCode%22%3A%22%22%2C%22Lat%22%3A%2219.076%22%2C%22Long%22%3A%2272.8777%22%2C%22GeoHash%22%3A%22te7%22%7D; _gat_UA-27207583-8=1; mrs=%5B%22CSWO%22%2C%22PPAM%22%5D; platform=%7B%22segments%22%3A%22%22%7D; _ga_84T5GTD0PC=GS1.1.1741500082.3.1.1741500427.33.0.0; WZRK_S_RK4-47R-98KZ=%7B%22p%22%3A7%2C%22s%22%3A1741500218%2C%22t%22%3A1741500427%7D',
}
def extract_cinema_code(url):
    match = re.search(r'cinema-\w+-(\w+)-MT', url)
    if match:
        return match.group(1)
    return None

def process_single_url(entry):
    url = entry.get('url')
    cinema_name = entry.get('cinema_name')
    city = entry.get('city')
    state = entry.get('state')
    country = entry.get('country')
    date = entry.get('date')

    print(f"Processing URL: {url}")
    cinema_code = extract_cinema_code(url)
    if not cinema_code:
        print(f"Could not extract cinema code from URL: {url}")
        return []

    try:
        response = requests.get(url, cookies=cookies, headers=headers, impersonate='chrome110')
        if response.status_code != 200:
            print(f"Failed to fetch data from URL: {url}. Status Code: {response.status_code}")
            return 

        html_content = response.text
        selector = Selector(text=html_content)
        script_tags = selector.xpath('//script[@type="text/javascript"]/text()').getall()
      
        for script in script_tags:
            if 'window.__INITIAL_STATE__' in script:
                data = script.strip('window.__INITIAL_STATE__ = ').strip()
                data = json.loads(data)
                break
        else:
            print(f"Could not find window.__INITIAL_STATE__ in the script tags for URL: {url}")
            return

        data = json.loads(data) if isinstance(data, str) else data
        queries = data.get("venueShowtimesFunctionalApi", {}).get("queries", {})
        extracted_key = next((key for key in queries if key.startswith("getShowtimesByVenue")), None)

        if not extracted_key:
            return 

        showtimes_data = queries.get(extracted_key, {})
        events = jmespath.search("data.showDetailsTransformed.Event", showtimes_data)
        results = []

        if events:
            for event in events:
                for child_event in event.get("ChildEvents", []):
                    event_name = child_event.get("EventName")
                    age = child_event.get("EventCensor")
                    language = child_event.get("EventLanguage")
                    dimensions = child_event.get("EventDimension")
                    for showtime in child_event.get("ShowTimes", []):
                        session_id = showtime.get("SessionId")
                        if session_id:
                            base_url = f'https://in.bookmyshow.com/seatlayout?cid={cinema_code}&sid={session_id}&routeCheck=1&sl=Y&newShowtime=1#!seatlayout'
                            results.append({
                                "movie name": event_name,
                                "age": age,
                                "language": language,
                                "dimensions": dimensions,
                                "show_url": base_url,
                                "cinema_url": url,
                                "cinema_name": cinema_name,
                                "city": city,
                                "state": state,
                                "country": country,
                                "date": date,
                                "showtime":showtime.get("ShowTime"),
                           
                            })
        return results

    except Exception as e:
        print(f"Error making request to URL: {url}. Error: {e}")
        return

# def process_urls(urls):
#     final_data = []
#     with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
#         futures = [executor.submit(process_single_url, entry) for entry in urls]
#         for future in as_completed(futures):
#             final_data.extend(future.result())
#     return final_data

# if __name__ == "__main__":
#     data = extract_cinemas()
#     if data:
#         print(f"Fetched {len(data)} URLs from the database.")
#         results = process_urls(data)

#         print(f"\nCollected {len(results)} showtime entries.")
#         # You can save or return results here if needed
#         with open('showtimes.json', 'w') as f:
#             json.dump(results, f, indent=4)
#     else:
#         print("No URLs found in the database.")
