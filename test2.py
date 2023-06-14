# -*- coding: utf-8 -*-
import time
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)

res = driver.get('https://www.baidu.com')
# 睡眠3秒
time.sleep(3)
print(res)
# 关闭浏览器
driver.quit()
cookie_use_times = time.time()
print("quit")
