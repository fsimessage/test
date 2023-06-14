# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
options = Options()
options.add_argument("--headless=new")
s = Service('bin/chromedriver')
driver = webdriver.Chrome(service=s, options=options)

res = driver.get('https://www.baidu.com')
# 睡眠3秒
time.sleep(3)
print(res)
# 关闭浏览器
driver.quit()
cookie_use_times = time.time()
print("quit")
