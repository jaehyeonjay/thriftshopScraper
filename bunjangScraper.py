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
    driver.get(stringHandler.bunjangURL)
    input_elem = driver.find_element(By.XPATH, stringHandler.searchEngineXPath)
    input_elem.send_keys(keyword)
    input_elem.send_keys(Keys.ENTER)
    return driver


def format_entry(name, price):
    name = re.sub("[\t\n]", "", name)
    price = int(re.sub("[\t\n 원,]", "", price))
    return "번개장터\t{}\t{}\n".format(name, price)


def collect_info(entry):
    try:  #TODO: the names of the class keeps changing
        name = entry.find(class_= stringHandler.bunjangName).get_text()
    except AttributeError:
        name = "0"
    try:
        price = entry.find(class_=stringHandler.bunjangPrice).get_text()
    except AttributeError:
        price = "0"
    return format_entry(name, price)


def no_entries(driver):
    try:
        driver.find_element(By.XPATH, stringHandler.bunjangNoElement)
    except NoSuchElementException:
        return False
    return True


def parse_page(driver, url, db):
    driver.get(url)
    cur_page = driver.page_source
    bs = BeautifulSoup(cur_page, 'html.parser')
    catalogue = bs.find_all(class_=stringHandler.bunjangCatalogue)
    for item in catalogue:
        item_info = collect_info(item)
        print(item_info)
        db.write(item_info)


def load_entries(driver, page_number):
    try:
        if page_number % 10 == 1:
            button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                 stringHandler.bunjangLoadMore)))
        else:
            button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, str(page_number))))
        time.sleep(.5)
        button.click()
        time.sleep(.5)
    except TimeoutException:
        return False
    return True


def scrape_bunjang(keyword, nitems, db):
    driver = enter_search_word(keyword)
    npages = math.ceil(int(nitems) / 100)
    url = driver.current_url

    # if no entries exit at all:
    if no_entries(driver):
        print("No entries with keyword " + keyword + " in Bunjang.")
        driver.close()
        return

    for i in range(1, npages + 1):
        parse_page(driver, url, db)
        if not load_entries(driver, i + 1):
            break
        url = driver.current_url
    driver.close()
