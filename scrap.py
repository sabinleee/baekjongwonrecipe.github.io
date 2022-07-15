import bs4 as bs
import requests as req

url = 'https://www.10000recipe.com/bbs/1266'
res = req.get(url)
soup = bs.BeautifulSoup(res.text, 'lxml')

lists = []
for p in soup.select('#contents_area > div > div.talk_content > p > a'):
    lists.append(p)

for i in lists:
    print(f"<p>{i}</p>")
    
