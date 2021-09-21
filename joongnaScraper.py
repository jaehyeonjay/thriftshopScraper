from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
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
    driver.get(stringHandler.joongnaURL)
    input_elem = driver.find_element(By.XPATH, stringHandler.searchEngineXPath)  #TODO: why doesn't this work occasionally?
    input_elem.send_keys(keyword)
    input_elem.send_keys(Keys.ENTER)
    return driver


def format_entry(name, price):
    name = re.sub("[\t\n]", "", name)
    price = int(re.sub("[\t\n 원,]", "", price))
    return "중고나라\t{}\t{}\n".format(name, price)


def collect_info(catalogue, db):
    for entry in catalogue:
        try:
            name = entry.find(class_=stringHandler.joongnaName).get_text()
        except AttributeError:
            name = "0"
        try:
            price = entry.find(class_=stringHandler.joongnaPrice).get_text()
        except AttributeError:
            price = "0"
        item_info = format_entry(name, price)
        print(item_info)
        db.write(item_info)


def no_entries(driver):
    try:
        driver.find_element(By.CLASS_NAME, stringHandler.joongnaNoElement)
    except NoSuchElementException:
        return False
    return True


def load_entries(driver):
    try:
        button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, stringHandler.joongnaLoadMore)))
        time.sleep(.5)
        button.click()
        time.sleep(.5)
    except TimeoutException:
        return False
    return True


def scrape_joongna(keyword, nitems, db):
    driver = enter_search_word(keyword)
    npages = math.ceil(int(nitems) / 11)

    # if no corresponding item at all:
    if no_entries(driver):
        print("No entries with keyword " + keyword + " in Joongna.")
        driver.close()
        return

    for i in range(1, npages + 1):
        if not load_entries(driver):
            break
    cur_page = driver.page_source
    bs = BeautifulSoup(cur_page, 'html.parser')
    collect_info(bs.find_all(class_=stringHandler.joongnaCatalogue), db)
    driver.close()