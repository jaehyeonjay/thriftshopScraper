from selenium import webdriver
from bs4 import BeautifulSoup
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
    driver.get('https://m.joongna.com/home')
    input_elem = driver.find_element(By.XPATH, "//input[@type='text']")  #TODO: why doesn't this work occasionally?
    input_elem.send_keys(keyword)
    input_elem.send_keys(Keys.ENTER)
    return driver


def format_entry(name, price):
    name = name.strip("\n ")
    if price != "N/A":
        price = int(re.sub("[\n 원,]", "", price))
    return "중고나라\t{}\t{}\n".format(name, price)


def collect_info(catalogue, db):
    for entry in catalogue:
        try:
            name = entry.find(class_="ProductItemV2_title__1KDby").get_text()
        except AttributeError:
            name = "N/A"
        try:
            price = entry.find(class_="ProductItemV2_price__1a5yb mt3").get_text()
        except AttributeError:
            price = "N/A"
        item_info = format_entry(name, price)
        db.write(item_info)


def load_entries(driver):
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='SearchList_moreButton__11RNU']")))
    time.sleep(.5)
    button.click()
    time.sleep(.5)


def scrape_joongna(keyword, nitems, db):
    driver = enter_search_word(keyword)
    npages = math.ceil(int(nitems) / 11)
    for i in range(1, npages + 1):
        load_entries(driver)
    cur_page = driver.page_source
    bs = BeautifulSoup(cur_page, 'html.parser')
    collect_info(bs.find_all(class_="ProductItemV2_info__1tF2R"), db)