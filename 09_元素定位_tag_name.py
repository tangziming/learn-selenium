"""
1、学习目标
    掌握tag_name元素定位方法
2、操作步骤（语法）
    #单数：优先查找第一个元素
    driver.find_element_by_tag_name("tag标签名")
    #复数：查出元素列表
    driver.find_elements_by_tag_name("tag标签名")
"""

from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "http://192.168.0.90/zfcapp/index.html#login"
driver.get(url)

time.sleep(2)

tag_elements = driver.find_elements_by_tag_name("input")
print(tag_elements)
for i in tag_elements:
    print(i.get_attribute("outerHTML"))



tag_elements[1].send_keys("001")

time.sleep(3)

driver.quit()