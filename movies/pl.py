import json
from curl_cffi import requests
import jmespath
from parsel import Selector
def make_request():
    try:
        cookies = {
            'bmsId': '1.73199175.1749973346042',
            'preferences': '%7B%22ticketType%22%3A%22M-TICKET%22%7D',
            '_gcl_au': '1.1.2101305210.1749973317',
            '_ga': 'GA1.1.1916945428.1749973318',
            'WZRK_G': 'a12861b46c3d4782a7d0d499b1cddd3d',
            'tvc_bmscookie': 'GA1.2.1916945428.1749973318',
            '_fbp': 'fb.1.1749973318865.710746440227948402',
            'geoHash': '%22%22',
            'geolocation': '%7B%22x-location-shared%22%3Afalse%2C%22x-location-selection%22%3A%22manual%22%2C%22timestamp%22%3A1750055781327%7D',
            'newShowtime': '%22https%3A%2F%2Fin.bookmyshow.com%2Fmovies%2Fahmedabad%2Fhousefull-5%2Fbuytickets%2FET00363347%2F20250616%22',
            '_uetvid': 'a6aee4204a8311f0abc9f975f5be9966',
            'tvc_vid': '41750058975384',
            'userCine': '%7Cmrs%3DRCNK%3BPPAM%3B%7C',
            'rgn': '{"regionNameSlug":"ahmedabad","regionCodeSlug":"ahd","regionName":"Ahmedabad","regionCode":"AHD","subName":"","subCode":"","Lat":"","Long":""}',
            '__cf_bm': 'yqH5mIbq2J85FLJQuZLeGc.O1Ec1OgvI5dpZs5NRemk-1751024572-1.0.1.1-ppGEtyOd.kAGfZZRIcJFRDEhHT7Lm9sFeLZkpRwXRIf6LPx2HTGSHZSf6O6XbefZ9kumjw9dIj_zXswhxFm_LEpZ23d0ftGHUoVkQrXJTI0',
            '__cfruid': '4e1a294c22f07807ce5b7b60e6e4a98175e5006f-1751024572',
            '_cfuvid': 'CUUuAwDtl4DVrbqFq46KQdFFJc4OVl1uLlP17Q7In60-1751024572032-0.0.1.1-604800000',
            'cf_clearance': 'Eg6xOtraiNPh7BKrajlZ8YtS67C__RxdcCt.QIi4LNY-1751024574-1.2.1.1-GFsrzgQHl0XPmW4KPsqYMUihQSy3DOuTaiaqMmgF9IzcdMqdMM.lWQvLPfOFouMSGip4T97vh6CzNOkbQCgbms0bbPUPHz2St2BqOf.JAP4MUruW_2OjiTFIG9jwOQt0H8Si.f1xlZh65ZuvKlD_V0HKGBzYiZ8WalEpsJ_KdAjtj03DfCZ90w6KJOYZ4L60Arrc2wYpizNX8HG.QqQt6oKS6ovVDQXvoGuR6dO0ymdzPhGsk4ZWP6mpWfsv3mEqeTZWblwsld_Xg7Iw8.sMQge5yJ_DITuDGkt6YamacaAP.943AA5EsJjBD5BjhPlIieJCzHnFyB54qQIt.I_vPoZ7AGT1JmvVCuTbWtMvwfU',
            'AMP_TOKEN': '%24NOT_FOUND',
            'tvc_bmscookie_gid': 'GA1.2.29499267.1751024550',
            '_gat_UA-27207583-8': '1',
            'platform': '%7B%22segments%22%3A%22%22%7D',
            '_ga_84T5GTD0PC': 'GS2.1.s1751024548$o7$g1$t1751024684$j36$l0$h0',
            'WZRK_S_RK4-47R-98KZ': '%7B%22p%22%3A7%2C%22s%22%3A1751024574%2C%22t%22%3A1751024685%7D',
            'cto_bundle': 'YKHJz19Sb0JqVWhHUEVUcjBZZ1JrRWI5TTh1WHo5VUlxdEk1Nzc0QiUyQiUyQmpNM3RXNG8lMkI4UUdUJTJGY0x2NmNONHFiNjFNTlhtJTJCUDBwa2pzT3VERzBZQWdnandJNmxtQ2EyaE52S0wlMkJpVmRqeGglMkJrcmdxNk5hMjcwR3glMkY2YjIxVlFWU0dPWWlYREUlMkY0ZjN0WmV2Qk9VJTJCTzJ5ZVRHUSUzRCUzRA',
        }

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'priority': 'u=0, i',
            'referer': 'https://in.bookmyshow.com/explore/events-ahmedabad',
            'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-arch': '"x86"',
            'sec-ch-ua-bitness': '"64"',
            'sec-ch-ua-full-version': '"137.0.7151.120"',
            'sec-ch-ua-full-version-list': '"Google Chrome";v="137.0.7151.120", "Chromium";v="137.0.7151.120", "Not/A)Brand";v="24.0.0.0"',
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
            # 'cookie': 'bmsId=1.73199175.1749973346042; preferences=%7B%22ticketType%22%3A%22M-TICKET%22%7D; _gcl_au=1.1.2101305210.1749973317; _ga=GA1.1.1916945428.1749973318; WZRK_G=a12861b46c3d4782a7d0d499b1cddd3d; tvc_bmscookie=GA1.2.1916945428.1749973318; _fbp=fb.1.1749973318865.710746440227948402; geoHash=%22%22; geolocation=%7B%22x-location-shared%22%3Afalse%2C%22x-location-selection%22%3A%22manual%22%2C%22timestamp%22%3A1750055781327%7D; newShowtime=%22https%3A%2F%2Fin.bookmyshow.com%2Fmovies%2Fahmedabad%2Fhousefull-5%2Fbuytickets%2FET00363347%2F20250616%22; _uetvid=a6aee4204a8311f0abc9f975f5be9966; tvc_vid=41750058975384; userCine=%7Cmrs%3DRCNK%3BPPAM%3B%7C; rgn={"regionNameSlug":"ahmedabad","regionCodeSlug":"ahd","regionName":"Ahmedabad","regionCode":"AHD","subName":"","subCode":"","Lat":"","Long":""}; __cf_bm=yqH5mIbq2J85FLJQuZLeGc.O1Ec1OgvI5dpZs5NRemk-1751024572-1.0.1.1-ppGEtyOd.kAGfZZRIcJFRDEhHT7Lm9sFeLZkpRwXRIf6LPx2HTGSHZSf6O6XbefZ9kumjw9dIj_zXswhxFm_LEpZ23d0ftGHUoVkQrXJTI0; __cfruid=4e1a294c22f07807ce5b7b60e6e4a98175e5006f-1751024572; _cfuvid=CUUuAwDtl4DVrbqFq46KQdFFJc4OVl1uLlP17Q7In60-1751024572032-0.0.1.1-604800000; cf_clearance=Eg6xOtraiNPh7BKrajlZ8YtS67C__RxdcCt.QIi4LNY-1751024574-1.2.1.1-GFsrzgQHl0XPmW4KPsqYMUihQSy3DOuTaiaqMmgF9IzcdMqdMM.lWQvLPfOFouMSGip4T97vh6CzNOkbQCgbms0bbPUPHz2St2BqOf.JAP4MUruW_2OjiTFIG9jwOQt0H8Si.f1xlZh65ZuvKlD_V0HKGBzYiZ8WalEpsJ_KdAjtj03DfCZ90w6KJOYZ4L60Arrc2wYpizNX8HG.QqQt6oKS6ovVDQXvoGuR6dO0ymdzPhGsk4ZWP6mpWfsv3mEqeTZWblwsld_Xg7Iw8.sMQge5yJ_DITuDGkt6YamacaAP.943AA5EsJjBD5BjhPlIieJCzHnFyB54qQIt.I_vPoZ7AGT1JmvVCuTbWtMvwfU; AMP_TOKEN=%24NOT_FOUND; tvc_bmscookie_gid=GA1.2.29499267.1751024550; _gat_UA-27207583-8=1; platform=%7B%22segments%22%3A%22%22%7D; _ga_84T5GTD0PC=GS2.1.s1751024548$o7$g1$t1751024684$j36$l0$h0; WZRK_S_RK4-47R-98KZ=%7B%22p%22%3A7%2C%22s%22%3A1751024574%2C%22t%22%3A1751024685%7D; cto_bundle=YKHJz19Sb0JqVWhHUEVUcjBZZ1JrRWI5TTh1WHo5VUlxdEk1Nzc0QiUyQiUyQmpNM3RXNG8lMkI4UUdUJTJGY0x2NmNONHFiNjFNTlhtJTJCUDBwa2pzT3VERzBZQWdnandJNmxtQ2EyaE52S0wlMkJpVmRqeGglMkJrcmdxNk5hMjcwR3glMkY2YjIxVlFWU0dPWWlYREUlMkY0ZjN0WmV2Qk9VJTJCTzJ5ZVRHUSUzRCUzRA',
        }

        response = requests.get('https://in.bookmyshow.com/explore/movies-ahmedabad', cookies=cookies, headers=headers,impersonate='chrome110')
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
def extract_json(data):
    try:
        selector= Selector(text=data)
        script = selector.xpath('//script[@type="text/javascript"]/text()').getall()
        for s in script:
            if 'window.__INITIAL_STATE__' in s:
                clean_script = s.strip('window.__INITIAL_STATE__ = ').strip()
                json_data = json.loads(clean_script)
                return json_data
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    

def extract_data(data):
    try:
        urls = []
        for listing in jmespath.search("explore.movies.listings",data):
            if "listing-desktop" in jmespath.search("id",listing):
                for card in jmespath.search("cards",listing):
                    ctaUrl = jmespath.search("ctaUrl",card)
                    if ctaUrl:
                        urls.append(ctaUrl)
        return urls
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
def main():
    response = make_request()
    if response:
        json_data = extract_json(response)
        if json_data:
            urls = extract_data(json_data)
            if urls:
                return urls
            else:
                print("No URLs found in the JSON data.")
                return None
        else:
            print("No URLs found in the response.")
            return None
    else:
        print("Failed to retrieve the webpage.")
        return None
if __name__ == "__main__":
    main()