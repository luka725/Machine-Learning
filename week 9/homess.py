from scrapy.http import TextResponse
import pandas as pd
import requests

filters = ["", "გაიგე მეტი", "ყველა ფოტო", " +", "(", ")", "•", ",", " ", "სასწრაფოდ", "ამოწევის სერვისი ", "იყიდება ბინა", "გაფერადების სერვისი", "თბილისი"]
substrings = ["VIP", "სიის თავში", "ფერით სხვა"]
data = []
real_data = []

for i in range(1, 10, 1):
    url = requests.get(f"https://home.ss.ge/ka/udzravi-qoneba/l/bina/iyideba?cityIdList=95&page={i}")
    res = TextResponse(url.url, body=url.text, encoding='utf-8')
    all = res.css("div.indQQP, div.kbVTfj")

    for e in all:
        data.append(e.css("::text").getall())

    for e in data:
        dt = []
        sanitized = []
        for str in e:
            str = str.replace(",", "")
            for s in substrings:
                if s in str:
                    str = ""
            if str not in filters:
                dt.append(str)
        if len(dt[0]) < 2:
            dt.pop(0)
        if dt[0] == "ფასი შეთანხმებით":
            dt[0] = ""
        if len(dt) == 11:
            sanitized.append(dt[0] + dt[1])
            sanitized.append(dt[2] + dt[3])
            sanitized.append(dt[4])
            sanitized.append(dt[5] +  dt[6] + dt[7])
            sanitized.append(dt[8])
            sanitized.append(dt[9])
            sanitized.append(dt[10])
            real_data.append(sanitized)

#print(real_data)
df = pd.DataFrame(real_data, columns=["ფასი", "ფართობი", "ოთახი", "სართული", "რაიონი", "უბანი", "ქუჩა"])
#print(df)
df.to_excel('homess.xlsx', index=False)
