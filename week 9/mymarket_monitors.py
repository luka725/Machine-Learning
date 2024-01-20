from scrapy.http import TextResponse
import pandas as pd
import requests
import numpy as np
import pprint as pp
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}


def remove_quote(list):
    for index, element in enumerate(list):
        list[index] = element.replace("'", "").replace('"', "").replace("″", "")
    return list


# <===== ALTA =====>

# url = f"https://alta.ge/monitors.html?items_per_page=100"
# response = requests.get(url, headers=headers)
# res = TextResponse(response.url, body=response.text, encoding='utf-8')
# data_alta = res.css("div.ty-grid-list__item-name > bdi > a::text, span.ty-price span:first-child::text").getall()
# data_alta = remove_quote(data_alta)

# length = len(data_alta) / 2
# data_alta = np.array_split(data_alta, length)

# df = pd.DataFrame(data_alta, columns=["დასახელება", "ფასი"])
# df.to_excel('alta.xlsx', index=False)

# <===== ATHOME =====>

# url = f"https://athome.ge/ka/product-category/monitors/page/1"
# response = requests.get(url, headers=headers)
# res = TextResponse(response.url, body=response.text, encoding='utf-8')
# data_athome = res.css(".product-details > h3 > a::text, span.price > span > bdi::text, span.price > ins > span > bdi::text").getall()
# data_athome = remove_quote(data_athome)

# length = len(data_athome) / 2
# data_athome = np.array_split(data_athome, length)

# df = pd.DataFrame(data_athome, columns=["დასახელება", "ფასი"])
# df.to_excel('athome.xlsx', index=False)

# <===== ELIT =====>

# # Set up the Selenium WebDriver
# chrome_service = ChromeService(executable_path='chromedriver.exe')
# driver = webdriver.Chrome(service=chrome_service)
# ee_data = []

# # Navigate to the URL
# for i in range(9):
#     url = f'https://ee.ge/kompiuteruli-teqnika/monitori?page={i}'
#     driver.get(url)

#     paragraphs = WebDriverWait(driver, 10).until(
#         EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span.title.d-xs-none:first-child, div.price-section > span:first-child'))
#     )
#     time.sleep(1)
#     for paragraph in paragraphs:
#         ee_data.append(paragraph.text)
    
# driver.quit()

# length = len(ee_data) / 2
# ee_data = np.array_split(ee_data, length)

# df = pd.DataFrame(ee_data, columns=["დასახელება", "ფასი"])
# df.to_excel('ee.xlsx', index=False)