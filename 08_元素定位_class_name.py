"""
1、学习目标
    掌握class_name元素定位方法
2、操作步骤（语法）
    #单数：优先查找第一个元素
    driver.find_element_by_class_name("class的属性值")
    #复数：查出元素列表
    driver.find_elements_by_class_name("class的属性值")
"""

from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "http://192.168.0.90/zfcapp/index.html#login"
driver.get(url)

time.sleep(2)

password = driver.find_elements_by_class_name("van-field__control")
print(password)

print(password[2].get_attribute("outerHTML"))

password[2].send_keys("123")

time.sleep(3)

driver.quit()