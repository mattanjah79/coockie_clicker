from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import sqlite3
from sqlite3 import Error
import json
from save_data import save_data





s = Service("C:/Users/pcm9x/Desktop/Pliki/chrome web driver/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://orteil.dashnet.org/experiments/cookie/")
time_frame = 5
timer = time.time() + time_frame
five_min = time.time() + 60*5
start_limit = 1000
limit = start_limit
multiplier = 1.25


start_time = time.time()
while time.perf_counter() < 600:

    cookie = driver.find_element(By.ID, "cookie")
    cookie.click()
    score = driver.find_element(By.ID, "money").text

    if "," in score:
        score = score.replace(",", "")

    all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")

    money = float(score)

    if money > limit:

        if time.time() > timer:

            items = driver.find_elements(By.CSS_SELECTOR, "#store div")
            items_list = [item.get_attribute("id") for item in items]

            for i in items_list:
                if i == '':
                    items_list.remove(i)

            item_prices = [price.text for price in all_prices]

            price_list = []

            for item in item_prices:
                if item != '':
                    price_list.append(int(item.split("-")[1].strip().replace(",", "")))

            balance_list = []
            for price in price_list:
                if price < float(score.strip().replace(",", "")):
                    balance_list.append(price)

            possible_purchases = items_list[0:len(balance_list)]

            def buyer(posible_list):
                for i in posible_list:
                    if i != '':
                        product = driver.find_element(By.ID, f"{i}")
                        product.click()
                        time.sleep(0.2)

            buyer(list(reversed(possible_purchases)))
            timer = time.time() + 5
            limit *= multiplier
            cps = driver.find_element(By.ID, "cps").text
            save_data(money, balance_list, possible_purchases, limit, cps, timer, start_limit, multiplier)









