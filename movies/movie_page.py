from curl_cffi import requests
from parsel import Selector
import json
import jmespath
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
def make_request(url):
    cookies = {
        'bmsId': '1.0113328475.1748948603338',
        '_gcl_au': '1.1.153893029.1748948574',
        '_fbp': 'fb.1.1748948576314.405475588604223771',
        'preferences': '%7B%22ticketType%22%3A%22M-TICKET%22%7D',
        'WZRK_G': '0c4251880a5642a0868b050bd12629ac',
        'tvc_bmscookie': 'GA1.2.298414781.1748948575',
        'geoHash': '%22%22',
        'tvc_vid': '71749015284202',
        'newShowtime': '%22https%3A%2F%2Fin.bookmyshow.com%2Fmovies%2Fmumbai%2Fhousefull-5%2Fbuytickets%2FET00363347%2F20250606%22',
        'userCine': '%7Cmrs%3DCPNS%3BPPAM%3BCPVM%3BCSWO%3BPVVW%3B%7C',
        '_uetvid': '55233b3041d711f097f745e2be1ee0bb',
        'geolocation': '%7B%22x-location-shared%22%3Afalse%2C%22x-location-selection%22%3A%22manual%22%2C%22timestamp%22%3A1749536400324%7D',
        'rgn': '%7B%22Lat%22%3A%2219.076%22%2C%22Seq%22%3A%221.0%22%2C%22Long%22%3A%2272.8777%22%2C%22regionName%22%3A%22Mumbai%22%2C%22regionCode%22%3A%22MUMBAI%22%2C%22isOlaEnabled%22%3A%22N%22%2C%22regionCodeSlug%22%3A%22mumbai%22%2C%22regionNameSlug%22%3A%22mumbai%22%2C%22GeoHash%22%3A%22te7%22%2C%22subCode%22%3A%22MCENT%22%2C%22subName%22%3A%22Mumbai%3A%20South%20%26%20Central%22%7D',
        'tvc_bmscookie_gid': 'GA1.2.1874572454.1749704763',
        '_ga': 'GA1.2.298414781.1748948575',
        '_gid': 'GA1.2.1287156824.1749796653',
        '_ga_1289SNYQ86': 'GS2.1.s1749796652$o2$g0$t1749796670$j42$l0$h0',
        '_ga_SLZ1FMJLVC': 'GS2.1.s1749796652$o2$g0$t1749796670$j42$l0$h0',
        '_cfuvid': 'opsRU5lLkw3xXknIILL_BQne9Bsjb5do3x0nTcqZG38-1749796703850-0.0.1.1-604800000',
        'AMP_TOKEN': '%24NOT_FOUND',
        '__cf_bm': 'wGAo0evJcJWoPf7WlEOnwFKjKL4bHRcUt35iE3kRNXs-1749797605-1.0.1.1-2i6Rb3ez.TbJwb51RxpimeqtfoTk_oB_tdflJ3Jg.PV5Q2QLEhlzD_Ev8dQHVsjd8dy4n3mYyS_abbMrDTTFhHPfhdRhtgIzHl_YLhl0hBg',
        '__cfruid': '7822722e185592d1bca2b497b1d265dd29f798fc-1749797813',
        'cf_clearance': '4e3YOTGtsqVmYa1M6nd_.vk8JSwOhafat3xfxacrAsM-1749797815-1.2.1.1-AGI7mnT_vCDBWZQn.iRLh2cwp4QaQcDnAVcLXFHfhpZskkPO9b0AyHcBfTb.q8foDiEI_N1YNOHxmkS6UOJ25WASZkKNfhnUUfp1vkhKhcHR.gDW5fGBjsxMtr4q.AZebnU4_K5rnHyfnoO8EA3wUobvLSsehi0ZcvibjdJlejiNG2hhbCjsFuaWrc9eWckXggwqwDX32LbE5z6mJ1ggVFYB.xeYhhko7tb4kvz5ocncPGiAGTkYEiqyNAebRDL9164i9NBYMSm2x1u4aI_PeW8IQV3Qb8DUjIONqPNZJTkUcGS90C03I9vAxCq0cJmy6p_4FaTxEaAuGlHV0Xsn6xV1o9BzOuc4Cr6oLYFHwoU',
        'platform': '%7B%22segments%22%3A%22%22%7D',
        'cto_bundle': '-fAm9V9NaGh5SUhRRVpMbWtOcVhEcndYU0N5YTNaYmJveURCYUVuT2dIWUFCTW55dFNJeFJIYTVlbU5adkRzT3VTRFFzSU4xQlNqM2FUWTVGRUpwd1IyS05WQ2clMkI4NjE0Z0NXbWVYM1J4dDB3WCUyQklsVE5ZdmR0RENiNXJpTnRlZnFVMWRIQ2FOb1l0c1UlMkZmMWZYeSUyRmhNOVdiQSUzRCUzRA',
        '_ga_84T5GTD0PC': 'GS2.1.s1749796676$o15$g1$t1749797794$j35$l0$h0',
        'WZRK_S_RK4-47R-98KZ': '%7B%22p%22%3A8%2C%22s%22%3A1749796707%2C%22t%22%3A1749797794%7D',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'if-modified-since': 'Fri, 13 Jun 2025 07:00:15 GMT',
        'priority': 'u=0, i',
        'referer': 'https://in.bookmyshow.com/explore/home/mumbai',
        'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"137.0.7151.104"',
        'sec-ch-ua-full-version-list': '"Google Chrome";v="137.0.7151.104", "Chromium";v="137.0.7151.104", "Not/A)Brand";v="24.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"19.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'service-worker-navigation-preload': 'true',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
        # 'cookie': 'bmsId=1.0113328475.1748948603338; _gcl_au=1.1.153893029.1748948574; _fbp=fb.1.1748948576314.405475588604223771; preferences=%7B%22ticketType%22%3A%22M-TICKET%22%7D; WZRK_G=0c4251880a5642a0868b050bd12629ac; tvc_bmscookie=GA1.2.298414781.1748948575; geoHash=%22%22; tvc_vid=71749015284202; newShowtime=%22https%3A%2F%2Fin.bookmyshow.com%2Fmovies%2Fmumbai%2Fhousefull-5%2Fbuytickets%2FET00363347%2F20250606%22; userCine=%7Cmrs%3DCPNS%3BPPAM%3BCPVM%3BCSWO%3BPVVW%3B%7C; _uetvid=55233b3041d711f097f745e2be1ee0bb; geolocation=%7B%22x-location-shared%22%3Afalse%2C%22x-location-selection%22%3A%22manual%22%2C%22timestamp%22%3A1749536400324%7D; rgn=%7B%22Lat%22%3A%2219.076%22%2C%22Seq%22%3A%221.0%22%2C%22Long%22%3A%2272.8777%22%2C%22regionName%22%3A%22Mumbai%22%2C%22regionCode%22%3A%22MUMBAI%22%2C%22isOlaEnabled%22%3A%22N%22%2C%22regionCodeSlug%22%3A%22mumbai%22%2C%22regionNameSlug%22%3A%22mumbai%22%2C%22GeoHash%22%3A%22te7%22%2C%22subCode%22%3A%22MCENT%22%2C%22subName%22%3A%22Mumbai%3A%20South%20%26%20Central%22%7D; tvc_bmscookie_gid=GA1.2.1874572454.1749704763; _ga=GA1.2.298414781.1748948575; _gid=GA1.2.1287156824.1749796653; _ga_1289SNYQ86=GS2.1.s1749796652$o2$g0$t1749796670$j42$l0$h0; _ga_SLZ1FMJLVC=GS2.1.s1749796652$o2$g0$t1749796670$j42$l0$h0; _cfuvid=opsRU5lLkw3xXknIILL_BQne9Bsjb5do3x0nTcqZG38-1749796703850-0.0.1.1-604800000; AMP_TOKEN=%24NOT_FOUND; __cf_bm=wGAo0evJcJWoPf7WlEOnwFKjKL4bHRcUt35iE3kRNXs-1749797605-1.0.1.1-2i6Rb3ez.TbJwb51RxpimeqtfoTk_oB_tdflJ3Jg.PV5Q2QLEhlzD_Ev8dQHVsjd8dy4n3mYyS_abbMrDTTFhHPfhdRhtgIzHl_YLhl0hBg; __cfruid=7822722e185592d1bca2b497b1d265dd29f798fc-1749797813; cf_clearance=4e3YOTGtsqVmYa1M6nd_.vk8JSwOhafat3xfxacrAsM-1749797815-1.2.1.1-AGI7mnT_vCDBWZQn.iRLh2cwp4QaQcDnAVcLXFHfhpZskkPO9b0AyHcBfTb.q8foDiEI_N1YNOHxmkS6UOJ25WASZkKNfhnUUfp1vkhKhcHR.gDW5fGBjsxMtr4q.AZebnU4_K5rnHyfnoO8EA3wUobvLSsehi0ZcvibjdJlejiNG2hhbCjsFuaWrc9eWckXggwqwDX32LbE5z6mJ1ggVFYB.xeYhhko7tb4kvz5ocncPGiAGTkYEiqyNAebRDL9164i9NBYMSm2x1u4aI_PeW8IQV3Qb8DUjIONqPNZJTkUcGS90C03I9vAxCq0cJmy6p_4FaTxEaAuGlHV0Xsn6xV1o9BzOuc4Cr6oLYFHwoU; platform=%7B%22segments%22%3A%22%22%7D; cto_bundle=-fAm9V9NaGh5SUhRRVpMbWtOcVhEcndYU0N5YTNaYmJveURCYUVuT2dIWUFCTW55dFNJeFJIYTVlbU5adkRzT3VTRFFzSU4xQlNqM2FUWTVGRUpwd1IyS05WQ2clMkI4NjE0Z0NXbWVYM1J4dDB3WCUyQklsVE5ZdmR0RENiNXJpTnRlZnFVMWRIQ2FOb1l0c1UlMkZmMWZYeSUyRmhNOVdiQSUzRCUzRA; _ga_84T5GTD0PC=GS2.1.s1749796676$o15$g1$t1749797794$j35$l0$h0; WZRK_S_RK4-47R-98KZ=%7B%22p%22%3A8%2C%22s%22%3A1749796707%2C%22t%22%3A1749797794%7D',
    }

    response = requests.get(
        url,
        cookies=cookies,
        headers=headers,
        impersonate='chrome100'
    )
    if response.status_code == 200:
        return response.text
    else:
        print(f"Request failed with status code {response.status_code}")
        return None
def extract_json(data):
    selector= Selector(text=data)
    script = selector.xpath('//script[@type="text/javascript"]/text()').getall()
    for s in script:
        if 'window.__INITIAL_STATE__' in s:
            clean_script = s.strip('window.__INITIAL_STATE__ = ').strip()
            json_data = json.loads(clean_script)
            return json_data
    return None
def convert_release_date(date_str):
    # Parse the date from the given format
    parsed_date = datetime.strptime(date_str, "%b %d, %Y")
    # Convert to desired format YYYYMMDD
    return parsed_date.strftime("%Y%m%d")
def remove_movie_code(url):
    parts = url.rstrip('/').split('/')
    if parts[-1].startswith('ET'):
        parts = parts[:-1]
    return '/'.join(parts)
def extract_pdp(json_data,url):
    try:
        short_url =  urlparse(url).path
        movieName = jmespath.search('synopsisStore.synopsis.eventName', json_data) or "N/A"
        eventCode = jmespath.search('synopsisStore.synopsis.eventCode', json_data) or "N/A"
        releaseDate = jmespath.search('synopsisStore.synopsis.releaseDate', json_data) or "N/A"
        movieLanguages = jmespath.search('synopsisStore.synopsis.eventLanguage', json_data) or "N/A"
        dimension = jmespath.search('synopsisStore.synopsis.eventDimension', json_data) or "N/A"
        image = jmespath.search('synopsisStore.synopsisRender.bannerWidget.multimedia.objectData.imageUrl', json_data) or "N/A"
        likes = jmespath.search('synopsisStore.synopsisRender.bannerWidget.secondaryData.interested.objectData.headerInfo.preTitle', json_data) or "N/A"
        genre = jmespath.search(f'seo."{short_url}".ldSchema.movieJsonLd.genre', json_data) or "N/A"
        isBookingAvailable = "yes" if jmespath.search('synopsisStore.synopsis.bookButton', json_data) else "No"
        showUrl = "N/A"
        if isBookingAvailable == "yes":
            formatedDate = convert_release_date(releaseDate)
            baseUrl = remove_movie_code(url)
            showUrl = f'{baseUrl}/buytickets/{eventCode}/{formatedDate}'

        return {
            "url": url,
            "movieName": movieName,
            "eventCode": eventCode,
            "releaseDate": releaseDate,
            "movieLanguages": json.dumps(movieLanguages),
            "dimension": dimension,
            "image": image,
            "likes": likes,
            "genre": json.dumps(genre),
            "isBookingAvailable": isBookingAvailable,
            "showUrl": showUrl,
            "status": "pending"
        }
    except Exception as e:
        print(f"Error extracting PDP data: {e}")
        return None

def main(url):
    data = make_request(url)
    if data:
        json_data = extract_json(data)
        if json_data:
            data = extract_pdp(json_data,url)
            if data:
                with open('movies.json', 'w') as json_file:
                    json.dump(data, json_file, indent=4)
            else:
                print("Failed to extract PDP data.")
        else:
            print("JSON data not found in the script.")
    else:
        print("Failed to make the request.")

def fetch_url():
    urls = select_data('bookmyshow', 'upcoming_movies', ['url'], {'status': 'pending'})

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(main, row[0]) for row in urls]
        for future in as_completed(futures):
            # Optional: log when each thread finishes
            try:
                future.result()
            except Exception as e:
                print(f"Thread exception: {e}")


if __name__ == "__main__":
    get_connection("bookmyshow")
    columns = {
    "id": "INT AUTO_INCREMENT PRIMARY KEY",
    "url": "TEXT",
    "movieName": "TEXT",
    "eventCode": "VARCHAR(20)",
    "releaseDate": "VARCHAR(50)",
    "movieLanguages": "TEXT",
    "dimension": "TEXT",
    "image": "TEXT",
    "likes": "VARCHAR(10)",
    "genre": "TEXT",
    "isBookingAvailable": "VARCHAR(10)",
    "showUrl": "TEXT",
    "showDetails": "TEXT",
    "status": "VARCHAR(20)"
}
    create_table("bookmyshow","movie_details",columns)
    fetch_url()
    # main('https://in.bookmyshow.com/movies/ahmedabad/avatar-fire-and-ash/ET00407893')