from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import math
import re


def enter_search_word(keyword):
    driver = webdriver.Chrome('/Users/jaypark/Downloads/chromedriver')
    driver.maximize_window()
    driver.get('https://m.bunjang.co.kr/')
    input_elem = driver.find_element(By.XPATH, "//input[@type='text']")
    input_elem.send_keys(keyword)
    input_elem.send_keys(Keys.ENTER)
    return driver


def format_entry(name, price):
    name = name.strip("\n ")
    if price != "N/A":
        price = int(re.sub("[\n 원,]", "", price))
    return "번개장터\t{}\t{}\n".format(name, price)


def collect_info(entry):
    try:  #TODO: the names of the class keeps changing
        name = entry.find(class_="sc-drlKqa ksilmM").get_text()
    except AttributeError:
        name = "N/A"
    try:
        price = entry.find(class_="sc-bIqbHp jdYBdp").get_text()
    except AttributeError:
        price = "N/A"
    product_info = format_entry(name, price)
    return product_info


def parse_page(driver, url, db):
    driver.get(url)
    cur_page = driver.page_source
    bs = BeautifulSoup(cur_page, 'html.parser')
    catalogue = bs.find_all(class_="sc-OxbzP kDNmKk")
    for product in catalogue:
        product_info = collect_info(product)
        db.write(product_info)


def load_entries(driver, page_number):
    try:
        if page_number % 10 == 1:
            button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                    "//a[@class='sc-ccbnFN jbSbET']//img[@src='data:image/svg+xml;"
                                                    "base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdp"
                                                    "ZHRoPSIxMiIgaGVpZ2h0PSIxMiIgdmlld0JveD0iMCAwIDEyIDEyIj4KICAgIDx"
                                                    "wYXRoIGZpbGw9IiM5Qjk5QTkiIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTMuNiA"
                                                    "xMmEuNTk2LjU5NiAwIDAgMCAuNDQ5LS4yMDJsNC44LTUuNGEuNi42IDAgMCAwIDA"
                                                    "tLjc5N2wtNC44LTUuNGEuNi42IDAgMSAwLS44OTcuNzk3TDcuNTk4IDYgMy4xNTI"
                                                    "gMTFBLjYuNiAwIDAgMCAzLjYgMTIiLz4KPC9zdmc+Cg==']")))
        else:
            button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, str(page_number))))
        time.sleep(.5)
        button.click()
        time.sleep(.5)
    except TimeoutException as e:
        print(e + ": 10 seconds passed but could not find item.")
        return


def scrape_bunjang(keyword, nitems, db):
    driver = enter_search_word(keyword)
    url = driver.current_url
    npages = math.ceil(int(nitems) / 100)
    for i in range(1, npages + 1):
        parse_page(driver, url, db)
        load_entries(driver, i + 1)
        url = driver.current_url
    driver.close()
