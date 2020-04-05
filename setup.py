from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import json

f=open('AMAZON_FASHION_5.json',)
data = json.load(f)

uniqueIds = []
for i in data['productDetails']: 
    if(i["asin"] not in uniqueIds):
        uniqueIds.append(i["asin"])

f.close()
print(uniqueIds)
for asin in uniqueIds:
    option = webdriver.ChromeOptions()
    option.add_argument("--incognito")

    browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver', chrome_options=option)
    url = "https://www.amazon.com/dp/"+str(asin)
    browser.get(url)

    titles_element = browser.find_elements_by_xpath("//span[@id='productTitle']")

    titles = [x.text for x in titles_element]

    try:
        title = titles[0]
        print(titles[0])
    except IndexError:
        continue

    browser.close()

    details = {
        'asin' : asin,
        'productName' : title
    }
    with open('product_details.json', 'a') as json_file:
        json.dump(details, json_file)



