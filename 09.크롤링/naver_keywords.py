from ast import Continue
import requests
from bs4 import BeautifulSoup

r = requests.get("https://sports.news.naver.com/wfootball/index")
bs = BeautifulSoup(r.text, "html.parser")

'''
네이버스포츠 해외축구 이시각 많이 본 뉴스
'''
main_title = bs.find_all("h2", {"class":"news_title"})
print("----------{}----------".format(main_title[0].text))

# lists = bs.find_all("li")
# for li in lists:
#     if li.find("a", {"class":"link_news_end"}) == None:
#         Continue
#     else:
#         title = li.find("a", {"class":"link_news_end"}).text
#         print(title)

'''
select함수로 구하는 방법
'''
lists = bs.select("li")
for li in lists:
    if li.select("a.link_news_end") != []:
        title = li.select("a.link_news_end")[0].text
        count = li.select("span.number")[0].text
        print("{}. {}".format(count,title))
        print("\n")
print("----------{}----------".format("종료"))