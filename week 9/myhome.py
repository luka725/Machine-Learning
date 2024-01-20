from scrapy.http import TextResponse
import pandas as pd
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
data = []
sanitized_data = []

for i in range(0, 10, 1):
    url = f"https://www.myhome.ge/ka/s/iyideba-bina-Tbilisi?Keyword=%E1%83%97%E1%83%91%E1%83%98%E1%83%9A%E1%83%98%E1%83%A1%E1%83%98&AdTypeID=1&PrTypeID=1&Page={i}&mapC=41.73188365%2C44.8368762993663&cities=1996871&GID=1996871"
    response = requests.get(url, headers=headers)
    res = TextResponse(response.url, body=response.text ,encoding='utf-8')
    all = res.css("div.card-body div.wrapper")

    for e in all:
        data.append(e.css("b.item-price-gel::text, div.item-size::text, span.unit::text, div.options-texts span::text, div.address::text").getall())

    for e in data:
        dt = []
        if len(e) == 8:
            dt.append(e[0])
            dt.append(e[2] + e[1])
            dt.append(e[4].replace("სარ. ", ""))
            dt.append(e[5].replace("ოთ. ", ""))
            dt.append(e[6].replace("საძ. ", ""))
            dt.append(e[7])
            sanitized_data.append(dt)

df = pd.DataFrame(sanitized_data, columns=["ფასი", "ფართობი", "სართული", "ოთახი", "საძინებელი", "მისამართი"])
df.to_excel('myhome.xlsx', index=False)
