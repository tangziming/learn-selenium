"""
1、find_element 使用给定的方法定位和查找一个元素
2、find_elements 使用给定的方法定位和查找所有元素list

By_id
当所定位的元素具有ID属性的时候我们可以通过by_id来定位该元素。

1、学习目标
    必须张伟selenium中元素定位方法，id
2、操作步骤（语法）
    通过元素id属性定位
    driver.find_element_by_id (id属性值)
"""

#导包
from selenium import webdriver
import time
#打开谷歌浏览器
driver = webdriver.Chrome()
#打开网址
driver.get("http://192.168.0.90/zfcapp/index.html#login")
#元素定位
element = driver.find_element_by_id("field_｛login｝_01")

print(element.get_attribute("outerHTML")) #查看元素对应的源码

#关闭浏览器
time.sleep(3)
driver.quit()  