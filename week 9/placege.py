from scrapy.http import TextResponse
import pandas as pd
import requests
import re

url = requests.get("https://place.ge/ge/ads/page:1?object_type=flat&order_by=date&currency_id=1&city_id=1&mode=list&limit=200")
res = TextResponse(url.url, body=url.text, encoding='utf-8')
all = res.css(".infoFilter")

data = []
sanitized_data = []
filter_words = ["ტელ", "ფასი:", " – "]
replace_words = [",", "ბინა", "ოთახი", "სართული", "თბილისი"]

for e in all:
    data.append(e.css(".infoFilter::text, span.price strong::text").getall())

for e in data:
    dt = []
    temp = []
    for each in e:
        each = re.sub(r"[\n\t]", "", each)
        for replace in replace_words:
            each = each.replace(replace, "")
        for word in filter_words:
            if word in each:
                each = ""
        if each not in ["", " "]:
            dt.append(each)
    if len(dt) == 3:        
        for text in dt:
            temp = dt[0].split(" ")
            temp = [item for item in temp if item != ""]
            temp.append(dt[1])
            temp.append(dt[2])
            print(len(dt))
        sanitized_data.append([temp[0], temp[1] + temp[2], temp[3], temp[4], temp[5]])

df = pd.DataFrame(sanitized_data, columns=["ოთახი", "ფართობი", "სართული", "მდებარეობა", "ფასი"])
df.to_excel('placege.xlsx', index=False)