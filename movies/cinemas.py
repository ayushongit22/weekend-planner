# import pymysql
# import json
# from curl_cffi import requests


# def get_region_code(city_name):
#     connection = pymysql.connect(
#         host='localhost',
#         user='root',
#         password='actowiz',
#         database='bookmyshow',
#     )

#     try:
#         with connection.cursor() as cursor:
#             sql = "SELECT RegionCode FROM cities WHERE RegionName = %s"
#             cursor.execute(sql, (city_name,))
#             result = cursor.fetchone()
#             print(result)
#             if result:
#                 return result[0]
#             else:
#                 raise Exception(f"No regionCode found for city: {city_name}")
#     finally:
#         connection.close()


# def extract_cinemas(city_name):
#     try:
#         region_code = get_region_code(city_name)
#         # print(f"Fetched regionCode: {region_code}")

#         headers = {
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
#     'priority': 'u=0, i',
#     'referer': 'https://in.bookmyshow.com/explore/movies-ahmedabad',
#     'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
#     'sec-ch-ua-arch': '"x86"',
#     'sec-ch-ua-bitness': '"64"',
#     'sec-ch-ua-full-version': '"137.0.7151.120"',
#     'sec-ch-ua-full-version-list': '"Google Chrome";v="137.0.7151.120", "Chromium";v="137.0.7151.120", "Not/A)Brand";v="24.0.0.0"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-model': '""',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-ch-ua-platform-version': '"19.0.0"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-user': '?1',
#     'service-worker-navigation-preload': 'true',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
#     # 'cookie': 'bmsId=1.73199175.1749973346042; preferences=%7B%22ticketType%22%3A%22M-TICKET%22%7D; _gcl_au=1.1.2101305210.1749973317; _ga=GA1.1.1916945428.1749973318; WZRK_G=a12861b46c3d4782a7d0d499b1cddd3d; tvc_bmscookie=GA1.2.1916945428.1749973318; _fbp=fb.1.1749973318865.710746440227948402; geoHash=%22%22; geolocation=%7B%22x-location-shared%22%3Afalse%2C%22x-location-selection%22%3A%22manual%22%2C%22timestamp%22%3A1750055781327%7D; newShowtime=%22https%3A%2F%2Fin.bookmyshow.com%2Fmovies%2Fahmedabad%2Fhousefull-5%2Fbuytickets%2FET00363347%2F20250616%22; tvc_vid=41750058975384; userCine=%7Cmrs%3DRCNK%3BPPAM%3B%7C; mrs=%5B%22PPAM%22%5D; _uetvid=a6aee4204a8311f0abc9f975f5be9966; rgn={"regionNameSlug":"ahmedabad","regionCodeSlug":"ahd","regionName":"Ahmedabad","regionCode":"AHD","subName":"","subCode":"","Lat":"","Long":""}; __cf_bm=RVWIBzALmhzyT2sAExIaOKdyZqBA5hDqsOU6EaZBlhU-1751260147-1.0.1.1-tHG6YOyUSjPjNKFQcelVmfHJzKyv0mdMCBuhUpX2cDHoQ89cAsIkzr5M2DVY3D4nUFZW_bHA_Rnzmy52qP_uP24aOlsRcE5St07wQrcu92c; __cfruid=5fd4fd1e99368d418c26f31e716a550f86496d11-1751260147; _cfuvid=A.7j3zXUw6trZDE6HspHCQLFKPccFFai3fXZJaB7PsI-1751260147422-0.0.1.1-604800000; cf_clearance=3oDT3uQkDovtc9gPeaOWo9Z_PmrAZO5n9wqU_tMbib8-1751260148-1.2.1.1-zJ8oilpF_oGxbzm.Un7uaRaAQKfkQ8dzXmxeHjDVzUNpbmlPj0ijtVT9hiApck6GGzFZAqQ5kaNRcohe8S_Gi1ynND4kvC8j5wkhuFFdcHEJBqwyA2Sy89xTw5nB.FQ1PLxuk5wAijkm6.P4WG0i6JDltTrnwU6TrU1BPQXjOUeSlsRPvjlxE6hCpmDf3YUiYGfqvfK8CgDAbzJOzl5L54k9kyaOByY8EyICsnb1KyUJZu.PCd0bvRG0Y3lf0ltu9yNX3Abh4Yq2yVv43QpCbSX2fjMDyCILG4tkSNW6sBlIXKe8_9yHxKReKpm5ES8cI_U.vs5P7fElUG2Kj_yIJtlgnNbp7.MUUT0uWzvJKDs; AMP_TOKEN=%24NOT_FOUND; tvc_bmscookie_gid=GA1.2.1544179585.1751260125; _gat_UA-27207583-8=1; _ga_84T5GTD0PC=GS2.1.s1751260124$o10$g1$t1751260128$j56$l0$h0; WZRK_S_RK4-47R-98KZ=%7B%22p%22%3A2%2C%22s%22%3A1751260149%2C%22t%22%3A1751260128%7D; cto_bundle=82sM2F9jdk54QW5OeTNhcVAlMkZ2ODQ0dSUyQjAxaUZNSjliQmc1MkQ0S2xGcjhwQjFFZHgwbjV3Z3BlOE5IR3l3QnFrWGNGa1lTc3RwQUJGTThXRGowWk9kenMwQmY5dzRUaldtUEVmekVVcUZqS2k3Q3lrcVVtSk5LMDJQTlVIdEpneVl1RlF1QUdJNUJyODlDYXhwenBEaWNwVWxnJTNEJTNE; platform={"segments":""}',
# }

#         params = {
#             'regionCode': region_code,
#             'eventType': 'MT',
#             'bmsId': '1.926025550.1741584779798',
#         }

#         response = requests.get(
#             'https://in.bookmyshow.com/api/v2/mobile/venues',
#             params=params,
#             headers=headers,
#             impersonate='chrome100'
#         )

#         print(f"HTTP Status: {response.status_code}")

#         data = response.json()

#         base_url = "https://in.bookmyshow.com/buytickets/{}/cinema-{}-{}-{}/{}"

#         cinemas = data["venues"]
#         cinema_details = []

#         for cinema in cinemas:
#             cinema_name = cinema["VenueName"].lower().replace(",", "").replace(" ", "-").replace(":", "")
#             venue_code = cinema["VenueCode"]
#             region_code_lower = cinema["RegionCode"].lower()
#             venue_type = cinema["VenueType"].strip("|")
#             city = cinema["City"]
#             state = cinema["State"]
#             country = cinema["Country"]

#             for date in cinema["arrDates"]:
#                 date_code = date["ShowDateCode"]
#                 url = base_url.format(cinema_name, region_code_lower, venue_code, venue_type, date_code)

#                 cinema_info = {
#                     "url": url,
#                     "cinema_name": cinema["VenueName"],
#                     "city": city,
#                     "state": state,
#                     "country": country,
#                     "date": date_code,
#                 }
#                 cinema_details.append(cinema_info)
#                 break

#         return cinema_details

#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return []



import json
from curl_cffi import requests
from pymongo import MongoClient


# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")  # or your Atlas URI
db = client["bookmyshow"]        # database name
collection = db["regions"]        # collection name


def get_region_code(city_name):
    """Fetch RegionCode from MongoDB by RegionName"""
    result = collection.find_one({"RegionName": city_name}, {"RegionCode": 1, "_id": 0})
    if result:
        return result["RegionCode"]
    else:
        raise Exception(f"No regionCode found for city: {city_name}")


def extract_cinemas(city_name):
    try:
        region_code = get_region_code(city_name.lower())
        headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'priority': 'u=0, i',
    'referer': 'https://in.bookmyshow.com/explore/movies-ahmedabad',
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
    # 'cookie': 'bmsId=1.73199175.1749973346042; preferences=%7B%22ticketType%22%3A%22M-TICKET%22%7D; _gcl_au=1.1.2101305210.1749973317; _ga=GA1.1.1916945428.1749973318; WZRK_G=a12861b46c3d4782a7d0d499b1cddd3d; tvc_bmscookie=GA1.2.1916945428.1749973318; _fbp=fb.1.1749973318865.710746440227948402; geoHash=%22%22; geolocation=%7B%22x-location-shared%22%3Afalse%2C%22x-location-selection%22%3A%22manual%22%2C%22timestamp%22%3A1750055781327%7D; newShowtime=%22https%3A%2F%2Fin.bookmyshow.com%2Fmovies%2Fahmedabad%2Fhousefull-5%2Fbuytickets%2FET00363347%2F20250616%22; tvc_vid=41750058975384; userCine=%7Cmrs%3DRCNK%3BPPAM%3B%7C; mrs=%5B%22PPAM%22%5D; _uetvid=a6aee4204a8311f0abc9f975f5be9966; rgn={"regionNameSlug":"ahmedabad","regionCodeSlug":"ahd","regionName":"Ahmedabad","regionCode":"AHD","subName":"","subCode":"","Lat":"","Long":""}; __cf_bm=RVWIBzALmhzyT2sAExIaOKdyZqBA5hDqsOU6EaZBlhU-1751260147-1.0.1.1-tHG6YOyUSjPjNKFQcelVmfHJzKyv0mdMCBuhUpX2cDHoQ89cAsIkzr5M2DVY3D4nUFZW_bHA_Rnzmy52qP_uP24aOlsRcE5St07wQrcu92c; __cfruid=5fd4fd1e99368d418c26f31e716a550f86496d11-1751260147; _cfuvid=A.7j3zXUw6trZDE6HspHCQLFKPccFFai3fXZJaB7PsI-1751260147422-0.0.1.1-604800000; cf_clearance=3oDT3uQkDovtc9gPeaOWo9Z_PmrAZO5n9wqU_tMbib8-1751260148-1.2.1.1-zJ8oilpF_oGxbzm.Un7uaRaAQKfkQ8dzXmxeHjDVzUNpbmlPj0ijtVT9hiApck6GGzFZAqQ5kaNRcohe8S_Gi1ynND4kvC8j5wkhuFFdcHEJBqwyA2Sy89xTw5nB.FQ1PLxuk5wAijkm6.P4WG0i6JDltTrnwU6TrU1BPQXjOUeSlsRPvjlxE6hCpmDf3YUiYGfqvfK8CgDAbzJOzl5L54k9kyaOByY8EyICsnb1KyUJZu.PCd0bvRG0Y3lf0ltu9yNX3Abh4Yq2yVv43QpCbSX2fjMDyCILG4tkSNW6sBlIXKe8_9yHxKReKpm5ES8cI_U.vs5P7fElUG2Kj_yIJtlgnNbp7.MUUT0uWzvJKDs; AMP_TOKEN=%24NOT_FOUND; tvc_bmscookie_gid=GA1.2.1544179585.1751260125; _gat_UA-27207583-8=1; _ga_84T5GTD0PC=GS2.1.s1751260124$o10$g1$t1751260128$j56$l0$h0; WZRK_S_RK4-47R-98KZ=%7B%22p%22%3A2%2C%22s%22%3A1751260149%2C%22t%22%3A1751260128%7D; cto_bundle=82sM2F9jdk54QW5OeTNhcVAlMkZ2ODQ0dSUyQjAxaUZNSjliQmc1MkQ0S2xGcjhwQjFFZHgwbjV3Z3BlOE5IR3l3QnFrWGNGa1lTc3RwQUJGTThXRGowWk9kenMwQmY5dzRUaldtUEVmekVVcUZqS2k3Q3lrcVVtSk5LMDJQTlVIdEpneVl1RlF1QUdJNUJyODlDYXhwenBEaWNwVWxnJTNEJTNE; platform={"segments":""}',
}

        params = {
            'regionCode': region_code,
            'eventType': 'MT',
            'bmsId': '1.926025550.1741584779798',
        }

        response = requests.get(
            'https://in.bookmyshow.com/api/v2/mobile/venues',
            params=params,
            headers=headers,
            impersonate='chrome100'
        )

        print(f"HTTP Status: {response.status_code}")

        data = response.json()
        base_url = "https://in.bookmyshow.com/buytickets/{}/cinema-{}-{}-{}/{}"

        cinemas = data.get("venues", [])
        cinema_details = []

        for cinema in cinemas:
            cinema_name = cinema["VenueName"].lower().replace(",", "").replace(" ", "-").replace(":", "")
            venue_code = cinema["VenueCode"]
            region_code_lower = cinema["RegionCode"].lower()
            venue_type = cinema["VenueType"].strip("|")
            city = cinema["City"]
            state = cinema["State"]
            country = cinema["Country"]

            for date in cinema.get("arrDates", []):
                date_code = date["ShowDateCode"]
                url = base_url.format(cinema_name, region_code_lower, venue_code, venue_type, date_code)

                cinema_info = {
                    "url": url,
                    "cinema_name": cinema["VenueName"],
                    "city": city,
                    "state": state,
                    "country": country,
                    "date": date_code,
                }
                cinema_details.append(cinema_info)
                break  # only take first date

        return cinema_details

    except Exception as e:
        print(f"An error occurred: {e}")
        return []
