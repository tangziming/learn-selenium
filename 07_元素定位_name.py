"""
1、学习目标
    掌握name元素定位方法
2、操作步骤（语法）
    driver.find_element_by_name("name的属性值")
"""

from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "http://192.168.0.90/zfcapp/index.html#login"
driver.get(url)

time.sleep(2)

companyID = driver.find_element_by_name("企业ID")

print(companyID.get_attribute("outerHTML"))

companyID.send_keys("2")

time.sleep(3)

driver.quit()