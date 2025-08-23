import requests
import json
import jmespath
import datetime
def get_events(location):
    try:
        cookies = {
        'PHPSESSID': 's8hl762hjmj91f66hipoopegid',
        'user_city': 'Ahmedabad',
        '_ae_utm_track': 'utmcsr=google|utmcmd=organic|utmccn=(not set)|utmctr=(not provided)',
        '_fbp': 'fb.1.1746341654455.165344992',
        '_pk_id.1.6c4e': '8f042f787600ba74.1746341655.',
        'ACTRKID': 'a26ca9a0-28b4-11f0-8844-e3634bdb9c5a',
        '_gcl_au': '1.1.627321860.1746341655',
        '_ga': 'GA1.1.986172126.1746341655',
        'WZRK_G': 'aa95e51cc3d140c5b49345768a0719f9',
        'current_lat': '23.0276',
        'current_long': '72.5871',
        '_ae_utm_track_ses': '1',
        '_pk_ref.1.6c4e': '%5B%22%22%2C%22%22%2C1746772701%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
        '_pk_ses.1.6c4e': '1',
        '_clck': '1bykr0p%7C2%7Cfvr%7C0%7C1950',
        '__AP_SESSION__': '2e46cd6e-3aa1-4830-aa04-9729bd668f13',
        '_pubcid': '78d0e55c-07d2-4b32-9a49-d8177528f2f5',
        '_pubcid_cst': 'zix7LPQsHA%3D%3D',
        '_cc_id': 'fae50173f72e2f392306d3a0ca2ee64b',
        'panoramaId_expiry': '1747377584364',
        'panoramaId': '7135a014a9a27eacc61919bddef8185ca02c5dc7710f1fca045e51ed8bf2d121',
        'panoramaIdType': 'panoDevice',
        'pbjs-unifiedid': '%7B%22TDID%22%3A%225dfe263d-38f7-47ad-8196-1d0757df3ee3%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222025-04-09T06%3A39%3A49%22%7D',
        'pbjs-unifiedid_cst': 'zix7LPQsHA%3D%3D',
        '_ctuid': '5b0a3419-3043-4c96-9ca4-c8a8518f57b0',
        'fpestid': '3f1jGNgteF69ihM-5m7dxIO3UHD2rVs7Pbk2vOs0JjjKhcALq9jCpenMTnfMB0mpW1MMAA',
        '_aff': 'u1gjbz',
        'fblogin-remind': 'true',
        'fblike-remind': 'true',
        'cto_bundle': '8QKipF9BZVc5U2klMkJmSTVsOGVzZUp4RElZWHd1SG1rYzlocDNPVGtqeHd0ME42ang0MWpTVUJxaWtIWFBhdEpic1UxM3NLZzYlMkIxJTJCJTJGNEY2SzJLR1BTbkJnJTJCb1VxN2hmMGlkZWNqMmE1WFJmbzUzZTFOQnVsSGVFQjR1WjdwR1VPNHNkRCUyQjBJMnZ1bXElMkI1MkJUejFCUFVrazU5USUzRCUzRA',
        'cto_bidid': '13JLwl9GTWRqaVhlWGNXemRMYkU1REc3ZnRPWGQ5dHNkNjVLb1EwbWNERzVFdGRTT0RwMnlYZjA1USUyRkdGYUFIUUpkMjZQejFLenZ6d0tWME1xSTdDOVdrMGR2blk3d1NZOGpqWHQ0ZGJNM2N6WXU0JTNE',
        '_ctz_opt_out': '_ctz_opt_out_ddu',
        '__gads': 'ID=0d77ca66b27d51b7:T=1746341678:RT=1746773090:S=ALNI_MbTGJ0rrOmaXQ82Z0NnBRrQnElCTQ',
        '__gpi': 'UID=00001018458e3335:T=1746341678:RT=1746773090:S=ALNI_MaFJYMegqBmE8kLhZb4ouKTXUyiiw',
        '__eoi': 'ID=c540d266e0287c02:T=1746341678:RT=1746773090:S=AA-AfjZF1nFDcealZ7Ll5rEtLZXt',
        '_ref': 'quicksearch-t-events',
        'user_city_query': 'ahmedabad',
        '_pgrf': '404',
        'WZRK_S_69R-556-545Z': '%7B%22p%22%3A7%2C%22s%22%3A1746772728%2C%22t%22%3A1746773287%7D',
        '_visit': '7',
        'FCNEC': '%5B%5B%22AKsRol8Mc13cj7H3jKz1K1tt-Xxe6ZC1dbAxWoixijLBkBPfYKgzpidKsGeTVmHMgQBLAnxxye5CjwpVLqI-XJn8bLDJbU-2hqHS4fZ8m8Y0joURhH4nFy8-5xqQQMSJBKpDlrL9oPzyzON8p2PlSQHRWLIeWYb3Jw%3D%3D%22%5D%5D',
        '_ga_DZD3QFXNY7': 'GS2.1.s1746772700$o2$g1$t1746773291$j42$l0$h0',
        '_clsk': '2xr33p%7C1746773294409%7C3%7C1%7Cl.clarity.ms%2Fcollect',
        '_ctpuid': 'e701b9df-1523-4c07-8243-d68d407e8f2a',
        }

        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/json;charset=UTF-8',
            'origin': 'https://allevents.in',
            'priority': 'u=1, i',
            'referer': 'https://allevents.in/ahmedabad/all',
            'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
            # 'cookie': 'PHPSESSID=s8hl762hjmj91f66hipoopegid; user_city=Ahmedabad; _ae_utm_track=utmcsr=google|utmcmd=organic|utmccn=(not set)|utmctr=(not provided); _fbp=fb.1.1746341654455.165344992; _pk_id.1.6c4e=8f042f787600ba74.1746341655.; ACTRKID=a26ca9a0-28b4-11f0-8844-e3634bdb9c5a; _gcl_au=1.1.627321860.1746341655; _ga=GA1.1.986172126.1746341655; WZRK_G=aa95e51cc3d140c5b49345768a0719f9; current_lat=23.0276; current_long=72.5871; _ae_utm_track_ses=1; _pk_ref.1.6c4e=%5B%22%22%2C%22%22%2C1746772701%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.1.6c4e=1; _clck=1bykr0p%7C2%7Cfvr%7C0%7C1950; __AP_SESSION__=2e46cd6e-3aa1-4830-aa04-9729bd668f13; _pubcid=78d0e55c-07d2-4b32-9a49-d8177528f2f5; _pubcid_cst=zix7LPQsHA%3D%3D; _cc_id=fae50173f72e2f392306d3a0ca2ee64b; panoramaId_expiry=1747377584364; panoramaId=7135a014a9a27eacc61919bddef8185ca02c5dc7710f1fca045e51ed8bf2d121; panoramaIdType=panoDevice; pbjs-unifiedid=%7B%22TDID%22%3A%225dfe263d-38f7-47ad-8196-1d0757df3ee3%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222025-04-09T06%3A39%3A49%22%7D; pbjs-unifiedid_cst=zix7LPQsHA%3D%3D; _ctuid=5b0a3419-3043-4c96-9ca4-c8a8518f57b0; fpestid=3f1jGNgteF69ihM-5m7dxIO3UHD2rVs7Pbk2vOs0JjjKhcALq9jCpenMTnfMB0mpW1MMAA; _aff=u1gjbz; fblogin-remind=true; fblike-remind=true; cto_bundle=8QKipF9BZVc5U2klMkJmSTVsOGVzZUp4RElZWHd1SG1rYzlocDNPVGtqeHd0ME42ang0MWpTVUJxaWtIWFBhdEpic1UxM3NLZzYlMkIxJTJCJTJGNEY2SzJLR1BTbkJnJTJCb1VxN2hmMGlkZWNqMmE1WFJmbzUzZTFOQnVsSGVFQjR1WjdwR1VPNHNkRCUyQjBJMnZ1bXElMkI1MkJUejFCUFVrazU5USUzRCUzRA; cto_bidid=13JLwl9GTWRqaVhlWGNXemRMYkU1REc3ZnRPWGQ5dHNkNjVLb1EwbWNERzVFdGRTT0RwMnlYZjA1USUyRkdGYUFIUUpkMjZQejFLenZ6d0tWME1xSTdDOVdrMGR2blk3d1NZOGpqWHQ0ZGJNM2N6WXU0JTNE; _ctz_opt_out=_ctz_opt_out_ddu; __gads=ID=0d77ca66b27d51b7:T=1746341678:RT=1746773090:S=ALNI_MbTGJ0rrOmaXQ82Z0NnBRrQnElCTQ; __gpi=UID=00001018458e3335:T=1746341678:RT=1746773090:S=ALNI_MaFJYMegqBmE8kLhZb4ouKTXUyiiw; __eoi=ID=c540d266e0287c02:T=1746341678:RT=1746773090:S=AA-AfjZF1nFDcealZ7Ll5rEtLZXt; _ref=quicksearch-t-events; user_city_query=ahmedabad; _pgrf=404; WZRK_S_69R-556-545Z=%7B%22p%22%3A7%2C%22s%22%3A1746772728%2C%22t%22%3A1746773287%7D; _visit=7; FCNEC=%5B%5B%22AKsRol8Mc13cj7H3jKz1K1tt-Xxe6ZC1dbAxWoixijLBkBPfYKgzpidKsGeTVmHMgQBLAnxxye5CjwpVLqI-XJn8bLDJbU-2hqHS4fZ8m8Y0joURhH4nFy8-5xqQQMSJBKpDlrL9oPzyzON8p2PlSQHRWLIeWYb3Jw%3D%3D%22%5D%5D; _ga_DZD3QFXNY7=GS2.1.s1746772700$o2$g1$t1746773291$j42$l0$h0; _clsk=2xr33p%7C1746773294409%7C3%7C1%7Cl.clarity.ms%2Fcollect; _ctpuid=e701b9df-1523-4c07-8243-d68d407e8f2a',
        }

        json_data = {
            'query': location,
            # 'latitude': '23.0276',
            # 'longitude': '72.5871',
            # 'city': 'Ahmedabad',
            # 'country': 'India',
            # 'region_code': 'GJ',
            'search_scope': 'city',
        }

        response = requests.post(
            'https://allevents.in/api/index.php/events/web/qs/search_v1',
            cookies=cookies,
            headers=headers,
            json=json_data,
        )
        if response.status_code != 200:
            return None
        results = []
        for event in jmespath.search('events',response.json()):
            url = jmespath.search('share_url',event)
            eventName = jmespath.search('eventname',event)
            image = jmespath.search('banner_url',event)
            timestamp = int(jmespath.search('start_time',event))
            time = datetime.datetime.fromtimestamp(timestamp)
            address = jmespath.search('venue.full_address',event)
            label = jmespath.search('label',event)
            has_ticket = jmespath.search('ticket.has_tickets',event)
            minimumPrice = jmespath.search('ticket.min_ticket_price',event)
            maximumTicketPrice = jmespath.search('ticket.max_ticket_price',event)
            currency = jmespath.search('ticket.ticket_currency',event)
            ticketStatus = 'Sold Out'
            if has_ticket:
                ticketStatus = 'Available'
            results.append({
                'url':url,
                'eventName':eventName,
                'image':image,
                'time':str(time),
                'address':address,
                'label':label,
                'ticketStatus':ticketStatus,
                'minimumPrice':minimumPrice,
                'maximumTicketPrice':maximumTicketPrice,
                'currency':currency
            })
            
        return results
    except Exception as e:
        return None

