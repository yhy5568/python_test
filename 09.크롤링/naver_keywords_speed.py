from ast import Continue
import requests
from bs4 import BeautifulSoup
import time

def time_function(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        end_time = time.time() - start_time
        print("{} {} time {}".format(f.__name__, args[1], end_time))
        return result
    return wrapper

@time_function
def r_fild_all(url, parser):
    r = requests.get(url)
    bs = BeautifulSoup(r.text, parser)
    lists = bs.find_all("li")

    titles = []
    for li in lists:
        if li.select("a.link_news_end") != []:
            title = li.select("a.link_news_end")[0].text
            titles.append(title)
    return titles

@time_function
def r_select(url, parser):
    r = requests.get(url)
    bs = BeautifulSoup(r.text, parser)

    lists = bs.find_all("li")

    titles = []
    for li in lists:
        if li.select("a.link_news_end") != []:
            title = li.select("a.link_news_end")[0].text
            titles.append(title)
    return titles

url = "https://sports.news.naver.com/wfootball/index"
r_fild_all(url, "html.parser")
r_select(url, "html.parser")

r_fild_all(url, "lxml")
r_select(url, "lxml")

'''
r = requests.get("https://sports.news.naver.com/wfootball/index")
#bs = BeautifulSoup(r.text, "html.parser")
bs = BeautifulSoup(r.text, "lxml") #속도에서 더 빠름


main_title = bs.find_all("h2", {"class":"news_title"})
print("----------{}----------".format(main_title[0].text))

# lists = bs.find_all("li")
# for li in lists:
#     if li.find("a", {"class":"link_news_end"}) == None:
#         Continue
#     else:
#         title = li.find("a", {"class":"link_news_end"}).text
#         print(title)


lists = bs.select("li")
for li in lists:
    if li.select("a.link_news_end") != []:
        title = li.select("a.link_news_end")[0].text
        count = li.select("span.number")[0].text
        print("{}. {}".format(count,title))
        print("\n")
print("----------{}----------".format("종료"))
'''