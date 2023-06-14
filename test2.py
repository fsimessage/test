# -*- coding: utf-8 -*-
import time
from selenium import webdriver

driver_path = "/usr/bin/chromedriver"

# 创建chrome参数对象
opt = webdriver.ChromeOptions()
# 把chrome设置成为无界面模式
opt.add_argument('--headless')
# 创建chrome无界面对象
driver = webdriver.Chrome(options=opt, executable_path=driver_path)
driver.implicitly_wait(100)
time.sleep(2)

# 打开浏览器，模拟浏览器请求页面
res = driver.get('https://www.baidu.com')
# 睡眠3秒
time.sleep(3)
print(res)
# 关闭浏览器
driver.quit()
cookie_use_times = time.time()
print("quit")
