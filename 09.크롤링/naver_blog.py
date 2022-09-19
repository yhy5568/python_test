import json
import requests
import json
from bs4 import BeautifulSoup

query = "파이썬강좌"

def get_search_naver_blog(query, start_page, end_page=None):
    start = (start_page - 1) * 10 + 1
    url = "https://s.search.naver.com/p/blog/search.naver?where=blog&api_type=1&query={}&rev=10&start={}".format(query, start_page)
    #url = "https://search.naver.com/search.naver?where=blog&rev=10&query={}&start={}".format(query, start_page)
    r = requests.get(url)
    _json = json.loads(r.text.replace("(","").replace(")","").strip())
    bs = BeautifulSoup(_json.get("html"), "lxml")
    result = []

    if end_page is None:
        tot_counts = int(_json.get("total"))
        end_page = tot_counts / 10

        if end_page > 900:
            end_page = 900

    lis = bs.select("li")     
    for li in lis:
        try:
            thumnail = li.select_one("img.thumb").get("src")
            title_link = li.select_one("a.api_txt_lines").get("href")
            title_text = li.select_one("a.api_txt_lines").text
            summary = li.select_one("div.api_txt_lines").text
            result.append((thumnail, title_text, title_link, summary))
        except:
            continue
    
    if start_page < end_page:
        start_page += 1
        result.extend(get_search_naver_blog(query, start_page=start_page, end_page=end_page))
    return result
   

results = get_search_naver_blog("파이썬강좌", start_page=1, end_page=3)
for result in results:
    print(result)