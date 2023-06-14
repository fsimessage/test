# -*- coding: utf-8 -*-
import time
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

res = driver.get('https://www.baidu.com')
# 睡眠3秒
time.sleep(3)
print(res)
# 关闭浏览器
driver.quit()
cookie_use_times = time.time()
print("quit")
