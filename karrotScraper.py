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
    driver.get('https://www.daangn.com/')
    input_elem = driver.find_element(By.XPATH, "//input[@type='text']")
    input_elem.send_keys(keyword)
    input_elem.send_keys(Keys.ENTER)
    return driver


def format_entry(name, price):
    name = name.strip("\n ")
    if price != "N/A":
        price = int(re.sub("[\n 원,]", "", price))
    return "당근마켓\t{}\t{}\n".format(name, price)


def print_info(catalogue, db):
    for entry in catalogue:
        try:
            name = entry.find(class_="article-title").get_text()
        except AttributeError:
            name = "N/A"
        price = entry.find(class_="article-price").get_text()
        if '-' in price:
            price = "N/A"
        item_info = format_entry(name, price)
        db.write(item_info)


def load_entries(driver):
    try:
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@onclick, 'moreResult')]")))
        time.sleep(.5)
        button.click()
        time.sleep(.5)
    except TimeoutException as e:
        print("10 seconds passed but could not find item.")
        return


def scrape_karrot(keyword, nitems, db):
    driver = enter_search_word(keyword)
    npages = math.ceil((int(nitems) - 6)/12)
    for i in range(1, npages):
        load_entries(driver)
    page = driver.page_source
    bs = BeautifulSoup(page, 'html.parser')
    print_info(bs.find_all(class_="flea-market-article flat-card"), db)
    driver.close()