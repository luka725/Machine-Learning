from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import pandas as pd
import time

chrome_service = ChromeService(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=chrome_service)


product_links = []
for i in range(1, 14):
    url = f'https://www.mymarket.ge/ka/search/123/teqnika/kompiuteruli-teqnika/monitori/?CatID=123&CondTypeID=1&Limit=10&OfferPrice=0&Page={i}&SetTypeID=2'
    driver.get(url)
    time.sleep(8)
    elements = driver.find_elements(By.CSS_SELECTOR, '.h-100[href]')
    for element in elements:
        product_links.append(element.get_attribute('href'))


product_list = []
for link in product_links:
    url = link
    if url != "https://www.mymarket.ge/ka":
        product_name = product_price = product_frequency = product_resolution = product_manufacturer = product_type = ""
        driver.get(url)
        print(url)
        time.sleep(8)
        product_main = driver.find_elements(By.ID, 'width_id')
        product_spec = driver.find_elements(By.CLASS_NAME, 'spec-list')
        for element in product_main:
            product_name = element.find_element(By.CLASS_NAME, 'line-height-14').text
            product_price = element.find_element(By.CLASS_NAME, 'line-height-10').text
            product_price = product_price[:-1]
            print(product_name)
            print(product_price)
            
        for element in product_spec:
            specifiactions = element.find_elements(By.CLASS_NAME, 'd-flex')
            for e in specifiactions:
                if e.find_element(By.CSS_SELECTOR, 'span').text == "მონიტორის სიხშირე":
                    product_frequency = e.find_element(By.CSS_SELECTOR, 'p').text
                    print(product_frequency)
                if e.find_element(By.CSS_SELECTOR, 'span').text == "რეზოლუცია":
                    product_resolution = e.find_element(By.CSS_SELECTOR, 'p').text
                    print(product_resolution)
                if e.find_element(By.CSS_SELECTOR, 'span').text == "ბრენდი":
                    product_manufacturer = e.find_element(By.CSS_SELECTOR, 'p').text
                    print(product_manufacturer)
                if e.find_element(By.CSS_SELECTOR, 'span').text == "მონიტორის ტიპი":
                    product_type = e.find_element(By.CSS_SELECTOR, 'p').text
                    print(product_type)
            product_list.append([product_manufacturer, product_name, product_price, product_frequency, product_resolution, product_type])
driver.quit()
products = pd.DataFrame(product_list, columns=["ბრენდი", "სახელი", "ფასი", "სიხშირე", "რეზოლუცია", "ტიპი"])
products.to_excel('monitors.xlsx', index=False)
