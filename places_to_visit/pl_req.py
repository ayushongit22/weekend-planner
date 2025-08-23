from operator import imod
import jmespath
import requests
from parsel import Selector
import threading
from queue import Queue
import json
from concurrent.futures import ThreadPoolExecutor
def make_request(location):
    
    cookies = {
        'ibulanguage': 'EN',
        'ibulocale': 'en_xx',
        'cookiePricesDisplayed': 'INR',
        'GUID': '09031092212461070172',
        'UBT_VID': '1746126135217.a2e9h3NAiN4R',
        '_gcl_au': '1.1.1821938774.1746126138',
        '_RSG': 'OlqfYL.bWPBM6hTcLWyDpB',
        '_RDG': '28d9202230966221fd2cb112b27f917fb1',
        '_RGUID': 'b66097e5-62a7-4bd8-bccd-f2056676b196',
        '_fwb': '13rEGFoY6AQODC5ub5w3Af.1746126139087',
        '_tt_enable_cookie': '1',
        '_ttp': '01JT6KMW870BJGPDH72P2FNDZE_.tt.1',
        'TRIP_DEST_TTD_PC': '100080',
        '_fbp': 'fb.1.1746126192851.252372712458383940',
        '_gid': 'GA1.2.733654616.1746126279',
        '_RF1': '194.61.40.26',
        '_ga_2DCSB93KS4': 'GS1.2.1746126288.1.1.1746128487.60.0.0',
        'ttcsid': '1746126139659::OmKy3AW7l1_X0pY7TXuD.1.1746128487758',
        'ttcsid_CIR4RVBC77UD5V58BBNG': '1746126139658::QbQcJDvMcyaBGzSUcyGe.1.1746128487992',
        '_bfa': '1.1746126135217.a2e9h3NAiN4R.1.1746128485960.1746128580031.1.30.10650012671',
        '_gat': '1',
        'wcs_bt': 's_33fb334966e9:1746128580',
        'cto_bundle': 'pOeMD19uakRWT1NaYiUyRmtxJTJCbk9ycGp5eFFzblp1V2x6cjFvMEhCYm1jSDNJYWJCNGszUXpuN3huTHFKMFZnUTQ0WDR0JTJGdzNES0w0bkZad3BQaHNLUjVWdnRUNlhRemQ5WGRnSjkzJTJCcGQ3Q1ZHTVlFZVBLaEtYYVhJeDdrcWF1VWpoN1JiOGljaUcxbGVmZWdMak5tTjc3WUdEUSUzRCUzRA',
        '_gat_UA-109672825-3': '1',
        '_ga': 'GA1.1.503151568.1746126139',
        '_ga_X437DZ73MR': 'GS1.1.1746126139.1.1.1746128580.30.0.0',
        '_ga_37RNVFDP1J': 'GS1.2.1746126279.1.1.1746128580.60.0.0',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        'origin': 'https://www.trip.com',
        'priority': 'u=1, i',
        'referer': 'https://www.trip.com/things-to-do/list-100080/city?citytype=&id=100080&name=undefined&keyword=Ahmedabad&pshowcode=Ticket2&locale=en-XX&curr=INR',
        'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
        # 'cookie': 'ibulanguage=EN; ibulocale=en_xx; cookiePricesDisplayed=INR; GUID=09031092212461070172; UBT_VID=1746126135217.a2e9h3NAiN4R; _gcl_au=1.1.1821938774.1746126138; _RSG=OlqfYL.bWPBM6hTcLWyDpB; _RDG=28d9202230966221fd2cb112b27f917fb1; _RGUID=b66097e5-62a7-4bd8-bccd-f2056676b196; _fwb=13rEGFoY6AQODC5ub5w3Af.1746126139087; _tt_enable_cookie=1; _ttp=01JT6KMW870BJGPDH72P2FNDZE_.tt.1; TRIP_DEST_TTD_PC=100080; _fbp=fb.1.1746126192851.252372712458383940; _gid=GA1.2.733654616.1746126279; _RF1=194.61.40.26; _ga_2DCSB93KS4=GS1.2.1746126288.1.1.1746128487.60.0.0; ttcsid=1746126139659::OmKy3AW7l1_X0pY7TXuD.1.1746128487758; ttcsid_CIR4RVBC77UD5V58BBNG=1746126139658::QbQcJDvMcyaBGzSUcyGe.1.1746128487992; _bfa=1.1746126135217.a2e9h3NAiN4R.1.1746128485960.1746128580031.1.30.10650012671; _gat=1; wcs_bt=s_33fb334966e9:1746128580; cto_bundle=pOeMD19uakRWT1NaYiUyRmtxJTJCbk9ycGp5eFFzblp1V2x6cjFvMEhCYm1jSDNJYWJCNGszUXpuN3huTHFKMFZnUTQ0WDR0JTJGdzNES0w0bkZad3BQaHNLUjVWdnRUNlhRemQ5WGRnSjkzJTJCcGQ3Q1ZHTVlFZVBLaEtYYVhJeDdrcWF1VWpoN1JiOGljaUcxbGVmZWdMak5tTjc3WUdEUSUzRCUzRA; _gat_UA-109672825-3=1; _ga=GA1.1.503151568.1746126139; _ga_X437DZ73MR=GS1.1.1746126139.1.1.1746128580.30.0.0; _ga_37RNVFDP1J=GS1.2.1746126279.1.1.1746128580.60.0.0',
    }

    json_data = {
        'head': {
            'extension': [
                {
                    'name': 'platform',
                    'value': 'Online',
                },
                {
                    'name': 'locale',
                    'value': 'en-XX',
                },
                {
                    'name': 'currency',
                    'value': 'INR',
                },
                {
                    'name': 'user-agent',
                    'value': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
                },
            ],
            'cid': '1746126135217.a2e9h3NAiN4R',
        },
        'scene': 'ticket',
        'districtId': 0,
        'index': 1,
        'count': 10,
        'sortType': 1,
        'returnModuleType': 'all',
        'filter': {
            'filterItems': [],
            'coordinateFilter': {
                'coordinateType': '',
                'latitude': None,
                'longitude': None,
            },
            'itemType': '',
        },
        'token': None,
        'keyword': location,
        'cityId': 100080,
        'pageId': '10650012750',
        'traceId': '0a611ff4-a227-e097-2897-1744e2d82051',
    }

    response = requests.post(
        'https://www.trip.com/restapi/soa2/19913/getTripAttractionList',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_pdp_url(json_data):
    urls=[]
    for item in jmespath.search("attractionList",json_data):
        url=jmespath.search("card.detailUrl",item)
        urls.append(url)
    return urls

def get_pdp(url):  
    

    cookies = {
        'ibulanguage': 'EN',
        'ibulocale': 'en_xx',
        'cookiePricesDisplayed': 'INR',
        'GUID': '09031092212461070172',
        'UBT_VID': '1746126135217.a2e9h3NAiN4R',
        '_gcl_au': '1.1.1821938774.1746126138',
        '_RSG': 'OlqfYL.bWPBM6hTcLWyDpB',
        '_RDG': '28d9202230966221fd2cb112b27f917fb1',
        '_RGUID': 'b66097e5-62a7-4bd8-bccd-f2056676b196',
        '_fwb': '13rEGFoY6AQODC5ub5w3Af.1746126139087',
        '_tt_enable_cookie': '1',
        '_ttp': '01JT6KMW870BJGPDH72P2FNDZE_.tt.1',
        'TRIP_DEST_TTD_PC': '100080',
        '_fbp': 'fb.1.1746126192851.252372712458383940',
        '_gid': 'GA1.2.733654616.1746126279',
        '_ga': 'GA1.1.503151568.1746126139',
        '_ga_37RNVFDP1J': 'GS1.2.1746126279.1.1.1746128580.60.0.0',
        '_ga_2DCSB93KS4': 'GS1.2.1746126288.1.1.1746128582.60.0.0',
        '_bfa': '1.1746126135217.a2e9h3NAiN4R.1.1746129246607.1746129707296.1.34.10650006154',
        'wcs_bt': 's_33fb334966e9:1746129708',
        'ttcsid': '1746126139659::OmKy3AW7l1_X0pY7TXuD.1.1746129709231',
        'ttcsid_CIR4RVBC77UD5V58BBNG': '1746126139658::QbQcJDvMcyaBGzSUcyGe.1.1746129709467',
        '_ga_X437DZ73MR': 'GS1.1.1746126139.1.1.1746129709.48.0.0',
        'cto_bundle': 'WicR4F9uakRWT1NaYiUyRmtxJTJCbk9ycGp5eFFzcGtRUjJVREpmREQlMkZ3RWhWanY1NllrblJibFR3YUV2enpMRWVqYklqT3d1a3d5eGZMSm84SWVSeSUyQnpmRnYxd1plaDdlbkhwQWVVcHNjVXhzUmlnMTBRVlVLc2VrMVlzVENiYUN6cXBlNTNKZHJodXFuU1hFMkUyTzUzeER5RFhpQSUzRCUzRA',
        '_RF1': '194.61.40.44',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'if-none-match': 'W/"482c1-5N1b6Bg14IMuLotmctQcBsXtEW4"',
        'priority': 'u=0, i',
        'referer': 'https://www.trip.com/things-to-do/list-100080/city?citytype=&id=100080&name=undefined&keyword=Ahmedabad&pshowcode=Ticket2&locale=en-XX&curr=INR',
        'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
        # 'cookie': 'ibulanguage=EN; ibulocale=en_xx; cookiePricesDisplayed=INR; GUID=09031092212461070172; UBT_VID=1746126135217.a2e9h3NAiN4R; _gcl_au=1.1.1821938774.1746126138; _RSG=OlqfYL.bWPBM6hTcLWyDpB; _RDG=28d9202230966221fd2cb112b27f917fb1; _RGUID=b66097e5-62a7-4bd8-bccd-f2056676b196; _fwb=13rEGFoY6AQODC5ub5w3Af.1746126139087; _tt_enable_cookie=1; _ttp=01JT6KMW870BJGPDH72P2FNDZE_.tt.1; TRIP_DEST_TTD_PC=100080; _fbp=fb.1.1746126192851.252372712458383940; _gid=GA1.2.733654616.1746126279; _ga=GA1.1.503151568.1746126139; _ga_37RNVFDP1J=GS1.2.1746126279.1.1.1746128580.60.0.0; _ga_2DCSB93KS4=GS1.2.1746126288.1.1.1746128582.60.0.0; _bfa=1.1746126135217.a2e9h3NAiN4R.1.1746129246607.1746129707296.1.34.10650006154; wcs_bt=s_33fb334966e9:1746129708; ttcsid=1746126139659::OmKy3AW7l1_X0pY7TXuD.1.1746129709231; ttcsid_CIR4RVBC77UD5V58BBNG=1746126139658::QbQcJDvMcyaBGzSUcyGe.1.1746129709467; _ga_X437DZ73MR=GS1.1.1746126139.1.1.1746129709.48.0.0; cto_bundle=WicR4F9uakRWT1NaYiUyRmtxJTJCbk9ycGp5eFFzcGtRUjJVREpmREQlMkZ3RWhWanY1NllrblJibFR3YUV2enpMRWVqYklqT3d1a3d5eGZMSm84SWVSeSUyQnpmRnYxd1plaDdlbkhwQWVVcHNjVXhzUmlnMTBRVlVLc2VrMVlzVENiYUN6cXBlNTNKZHJodXFuU1hFMkUyTzUzeER5RFhpQSUzRCUzRA; _RF1=194.61.40.44',
    }

    params = {
        'curr': 'INR',
        'locale': 'en-XX',
    }

    response = requests.get(
        url,
        params=params,
        cookies=cookies,
        headers=headers,
    )
    if response.status_code == 200:
        selector=Selector(text=response.text)
        raw_json=selector.xpath('//script[@id="__NEXT_DATA__"]/text()').get()
        json_data=json.loads(raw_json)
        if json_data:
            directUrl=jmespath.search("props.pageProps.appData.overviewData.basicInfo.detailUrl",json_data) or "N/A"
            name=jmespath.search("props.pageProps.appData.overviewData.basicInfo.poiName",json_data) or "N/A"
            address=jmespath.search("props.pageProps.appData.overviewData.basicInfo.address",json_data) or "N/A"
            phone=jmespath.search("props.pageProps.appData.overviewData.basicInfo.telephone",json_data)
            if phone:
                number=','.join(phone)
            else:
                number="N/A"
            rating=jmespath.search("props.pageProps.appData.overviewData.basicInfo.hotScore",json_data) or "N/A"
            images=jmespath.search("props.pageProps.appData.overviewData.imageInfo.imageList",json_data) or []
            timings=jmespath.search("props.pageProps.appData.overviewData.openInfo.openTimeDetailDesc",json_data) or "N/A"
            return {
                "directUrl":directUrl,
                "name":name,
                "address":address,
                "phone":number,
                "rating":rating,
                "images":images,
                "timings":timings,
            }
        else:
            return None
    else:
        return None

def process_urls_batch(urls, total_data, lock):
    """Process a batch of URLs and add results to total_data list thread-safely"""
    for url in urls:
        data = get_pdp(url)
        if data:
            with lock:
                total_data.append(data)

def process_urls_with_threading(urls, batch_size=10):
    """Process URLs in batches using multiple threads"""
    total_data = []
    lock = threading.Lock()
    
    # Split URLs into batches
    for i in range(0, len(urls), batch_size):
        batch = urls[i:i + batch_size]
        threads = []
        
        # Create and start threads for each URL in the batch
        for url in batch:
            thread = threading.Thread(
                target=process_urls_batch,
                args=([url], total_data, lock)
            )
            threads.append(thread)
            thread.start()
        
        # Wait for all threads in current batch to complete
        for thread in threads:
            thread.join()
    
    return total_data

def places_to_visit(location):
    json_data = make_request(location)
    if json_data:
        urls = get_pdp_url(json_data)
        if urls:
            # Process URLs with threading
            total_data = process_urls_with_threading(urls)
            return total_data
        else:
            return None
    else:
        return None