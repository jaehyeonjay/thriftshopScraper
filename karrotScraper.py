from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import math
import re
import stringHandler


def enter_search_word(keyword):
    driver = webdriver.Chrome(stringHandler.chromeDriverPath)
    driver.maximize_window()
    driver.get(stringHandler.karrotURL)
    input_elem = driver.find_element(By.XPATH, stringHandler.searchEngineXPath)
    input_elem.send_keys(keyword)
    input_elem.send_keys(Keys.ENTER)
    return driver


def format_entry(name, price):
    name = re.sub("[\t\n]", "", name)
    price = int(re.sub("[\t\n 원,]", "", price))
    return "당근마켓\t{}\t{}\n".format(name, price)


def collect_info(catalogue, db):
    for entry in catalogue:
        try:
            name = entry.find(class_ = stringHandler.karrotName).get_text()
        except AttributeError:
            name = "0"
        try:
            price = entry.find(class_ = stringHandler.karrotPrice).get_text()
        except AttributeError:
            name = "0"
        if '-' in price or '나눔' in price:
            price = "0"
        item_info = format_entry(name, price)
        print(item_info)
        db.write(item_info)


def no_entries(driver):
    try:
        driver.find_element(By.CLASS_NAME, stringHandler.karrotNoElement)
    except NoSuchElementException:
        return False
    return True


def load_entries(driver):
    try:
        button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, stringHandler.karrotLoadMore)))
        time.sleep(.5)
        button.click()
        time.sleep(.5)
    except TimeoutException:
        return False
    return True


def scrape_karrot(keyword, nitems, db):
    driver = enter_search_word(keyword)
    npages = math.ceil((int(nitems) - 6)/12)

    # if no entries exist at all:
    if no_entries(driver):
        print("No entries with keyword " + keyword + " in Karrot.")
        driver.close()
        return

    for i in range(1, npages):
        if not load_entries(driver):
            break
    page = driver.page_source
    bs = BeautifulSoup(page, 'html.parser')
    collect_info(bs.find_all(class_ = stringHandler.karrotCatalogue), db)
    driver.close()