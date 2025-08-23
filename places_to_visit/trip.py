import requests
import jmespath
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
        '_RF1': '194.61.40.28',
        '_bfa': '1.1746126135217.a2e9h3NAiN4R.1.1746126597344.1746126641228.1.10.10650012671',
        'cto_bundle': '8DPYF19uakRWT1NaYiUyRmtxJTJCbk9ycGp5eFFzb2pCblowdktEYk9UVTlheUZNeFBzRkRLUXBsZkdFbVBoa1kwWkxMdkpKVjRYZXQxeFNsQU0lMkZzc1U5Tk1rMDZiY1Z6STk2WXRxQ2VabDNGSnhjTUtheEtIYzFENmQlMkZsNmk3SE1XZ2xzenRyYk81Mlh2b2ROM0o4VlFUNElGTEo5ZyUzRCUzRA',
        'ttcsid': '1746126139659::OmKy3AW7l1_X0pY7TXuD.1.1746126644428',
        'ttcsid_CIR4RVBC77UD5V58BBNG': '1746126139658::QbQcJDvMcyaBGzSUcyGe.1.1746126644709',
        '_ga': 'GA1.2.503151568.1746126139',
        '_ga_37RNVFDP1J': 'GS1.2.1746126279.1.1.1746126644.60.0.0',
        '_ga_2DCSB93KS4': 'GS1.2.1746126288.1.1.1746126645.60.0.0',
        '_ga_X437DZ73MR': 'GS1.1.1746126139.1.1.1746126662.60.0.0',
    }

    headers = {
        'accept': 'application/json',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json;charset=UTF-8',
        'currency': 'INR',
        'locale': 'en-XX',
        'origin': 'https://www.trip.com',
        'priority': 'u=1, i',
        'referer': 'https://www.trip.com/',
        'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
        # 'cookie': 'ibulanguage=EN; ibulocale=en_xx; cookiePricesDisplayed=INR; GUID=09031092212461070172; UBT_VID=1746126135217.a2e9h3NAiN4R; _gcl_au=1.1.1821938774.1746126138; _RSG=OlqfYL.bWPBM6hTcLWyDpB; _RDG=28d9202230966221fd2cb112b27f917fb1; _RGUID=b66097e5-62a7-4bd8-bccd-f2056676b196; _fwb=13rEGFoY6AQODC5ub5w3Af.1746126139087; _tt_enable_cookie=1; _ttp=01JT6KMW870BJGPDH72P2FNDZE_.tt.1; TRIP_DEST_TTD_PC=100080; _fbp=fb.1.1746126192851.252372712458383940; _gid=GA1.2.733654616.1746126279; _RF1=194.61.40.28; _bfa=1.1746126135217.a2e9h3NAiN4R.1.1746126597344.1746126641228.1.10.10650012671; cto_bundle=8DPYF19uakRWT1NaYiUyRmtxJTJCbk9ycGp5eFFzb2pCblowdktEYk9UVTlheUZNeFBzRkRLUXBsZkdFbVBoa1kwWkxMdkpKVjRYZXQxeFNsQU0lMkZzc1U5Tk1rMDZiY1Z6STk2WXRxQ2VabDNGSnhjTUtheEtIYzFENmQlMkZsNmk3SE1XZ2xzenRyYk81Mlh2b2ROM0o4VlFUNElGTEo5ZyUzRCUzRA; ttcsid=1746126139659::OmKy3AW7l1_X0pY7TXuD.1.1746126644428; ttcsid_CIR4RVBC77UD5V58BBNG=1746126139658::QbQcJDvMcyaBGzSUcyGe.1.1746126644709; _ga=GA1.2.503151568.1746126139; _ga_37RNVFDP1J=GS1.2.1746126279.1.1.1746126644.60.0.0; _ga_2DCSB93KS4=GS1.2.1746126288.1.1.1746126645.60.0.0; _ga_X437DZ73MR=GS1.1.1746126139.1.1.1746126662.60.0.0',
    }

    params = {
        'x-traceID': '09031092212461070172-1746126880452-4371',
    }

    json_data = {
        'head': {
            'extension': [
                {
                    'name': 'bookingTransactionId',
                    'value': '1746126598234_5737',
                },
            ],
        },
        'client': {
            'cid': '09031092212461070172',
            'locale': 'en-XX',
            'currency': 'INR',
            'version': None,
            'source': 'tnt_search_popover',
            'variables': [
                {
                    'key': 'BASE_SUGGEST',
                    'value': 'true',
                },
                {
                    'key': 'CHANNEL_ID',
                    'value': '118',
                },
                {
                    'key': 'SYSTEM',
                    'value': '',
                },
                {
                    'key': 'DEVICE_NAME',
                    'value': '',
                },
                {
                    'key': 'SCREEN_WIDTH',
                    'value': '1280',
                },
                {
                    'key': 'SCREEN_HEIGHT',
                    'value': '305',
                },
            ],
            'trace': None,
            'channel': None,
        },
        'keyword': location,
        'tab': 10,
        'channel': 'Online',
        'geo': {
            'location': {
                'id': 0,
                'type': 'gs_district',
                'category': 3,
            },
        },
    }

    response = requests.post(
        'https://m.trip.com/restapi/soa2/20684/suggest',
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_url(json_data):
    place_name=jmespath.search("modules[0].items[0].name",json_data)
    base_url=f"https://www.trip.com/things-to-do/list-100080/city?citytype=&id=100080&name=undefined&keyword={place_name}&pshowcode=Ticket2&locale=en-XX&curr=INR"
    return base_url
if __name__ == "__main__":
    location='ahmedabad'
    json_data = make_request(location)
    if json_data:
        url=get_url(json_data)
        print(url)
    else:
        print("Request failed.")