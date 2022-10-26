import requests
import geohash2

keyword = "광진구"
url = "https://apis.zigbang.com/v2/search?leaseYn=N&q={}&serviceType=원룸".format(keyword)
r = requests.get(url)
_json = r.json()
if _json.get("success") == True:
    items = _json.get("items")[0]
    lat = items.get("lat")
    lng = items.get("lng")
    geocode = geohash2.encode(lat,lng,precision=5)
    url = "https://apis.zigbang.com/v2/items?" \
        "deposit_gteq=0&" \
        "domain=zigbang&" \
        "geohash={}&" \
        "needHasNoFiltered=true&" \
        "rent_gteq=0&" \
        "sales_type_in=전세%7C월세&" \
        "service_type_eq=원룸".format(geocode)
    r = requests.get(url)
    _json = r.json()
    _items = _json.get("items")
    item_ids = []
    for item in _items:
        item_ids.append(item.get("item_id"))
    
    url = "https://apis.zigbang.com/v2/items/list"
    items = {"item_ids": item_ids[:100]}
    _results = requests.post(url, data=items).json()
    datas = _results.get("items")
    for d in datas:
        print("*"*50)
        print(d)
