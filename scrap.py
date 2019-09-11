from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import pandas as pd
import time


driver = webdriver.Chrome("\chromium_driver\chromedriver.exe")
url = "https://www.google.com/maps?hl=en"
driver.get(url)
id_count = 0
id=[]
name=[]
address=[]
website=[]
plus_code=[]
rating=[]
review=[]
web_url=[]

def start():
    try:
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "section-query-on-pan"))
        )
        time.sleep(2)
        try:
            driver.find_element_by_class_name('section-no-result')
            driver.quit()
        except NoSuchElementException:
            div = driver.find_elements_by_class_name('section-result')

            if len(div) < 1:
                driver.quit()
            else:
                count = len(div)

            scrapping(count)
    except TimeoutException:
        print("Loading took too much time!11111")

#function for scrapping individual item
def scrapping(count):
    global id_count
    i=0

    while(i<count):
        div = driver.find_elements_by_class_name('section-result')
        div[i].send_keys(Keys.ENTER)
        try:
            element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME,"section-info"))
            )

            try:
                name_tag = driver.find_element_by_class_name('GLOBAL__gm2-headline-5')
            except NoSuchElementException:
                name_tag = type('obj', (object,), {'text' : ''})

            try:
                address_tag = driver.find_element_by_xpath('//div[@vet="36622"]')
            except NoSuchElementException:
                address_tag = type('obj', (object,), {'text' : ''})

            try:
                website_tag = driver.find_element_by_xpath('//div[@vet="3443"]')
            except NoSuchElementException:
                website_tag = type('obj', (object,), {'text' : ''})

            try:
                plus_code_tag = driver.find_element_by_xpath('//div[@vet="27644"]')
            except NoSuchElementException:
                plus_code_tag = type('obj', (object,), {'text': ''})

            try:
                rating_tag = driver.find_element_by_class_name('section-star-display')
            except NoSuchElementException:
                rating_tag = type('obj', (object,), {'text': ''})

            try:
                review_tag = driver.find_element_by_xpath('//button[@vet="3648"]')
            except NoSuchElementException:
                review_tag = type('obj', (object,), {'text' : ''})

            web_url_tag = type('obj', (object,), {'text' : driver.current_url})

            id.append(id_count)

            if len(name_tag.text):
                name.append(name_tag.text)
            else:
                name.append("")

            if len(address_tag.text):
                address.append(address_tag.text)
            else:
                address.append("")

            if len(website_tag.text):
                website.append(website_tag.text)
            else:
                website.append("")

            if len(plus_code_tag.text):
                plus_code.append(plus_code_tag.text)
            else:
                plus_code.append("")

            if len(rating_tag.text):
                rating.append(rating_tag.text)
            else:
                rating.append("")

            if len(review_tag.text):
                review.append(review_tag.text)
            else:
                review.append("")

            if len(web_url_tag.text):
                web_url.append(web_url_tag)
            else:
                web_url.append("")

            id_count= id_count+1
        except TimeoutException:
            print("Loading took too much time!")
        back = driver.find_element_by_class_name('section-back-to-list-button')
        back.send_keys(Keys.ENTER)
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "n7lv7yjyC35__left"))
        )
        i=i+1

    next_page=driver.find_element_by_id('n7lv7yjyC35__section-pagination-button-next')
    if next_page.is_enabled():
        next_page.send_keys(Keys.ENTER)
        start()
    else:
        time.sleep(3)
        driver.quit()


#main function
try:
    element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "q"))
            )
    driver.find_element_by_name('q').send_keys("futsal, baneshwor")
    driver.find_element_by_id('searchbox-searchbutton').send_keys(Keys.ENTER)
    start()
except TimeoutException:
    print("Loading took too much time!")

for i in range(len(id)):
    print("id : {}, name : {}, address : {}, website : {}, plus_code : {}, raitng : {}, review : {}, url :{}".format(id[i],name[i],address[i],
            website[i],plus_code[i],rating[i],review[i],web_url[i]))



