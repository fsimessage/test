# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")

s = Service('bin/chromedriver')
driver = webdriver.Chrome(service=s, options=options)

driver.get('https://www.baidu.com')
# 睡眠3秒
time.sleep(3)
print(driver.title)
# 关闭浏览器
driver.quit()
cookie_use_times = time.time()
print("quit")
