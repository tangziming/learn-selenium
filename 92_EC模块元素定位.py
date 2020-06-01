"""
1、学习目标
    掌握selenium中EC模块的元素定位方法
    presence_of_element_located(locator)方法的使用

    

2、操作步骤（语法）
    WebDriverWait(driver,10).until(EC.presence_of_element_located(locator))
    locator:定位器，是一个元组(定位方法，方法值) - 实例：（"id","field_｛login｝_01"）
    
    1、制作定位器： locator 是一个元组

    适用场景：
"""     

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

url = "http://192.168.0.90/zfcapp/index.html#login"
driver.get(url)
time.sleep(5)
locator = (By.ID,"field_｛login｝_02")
ele = WebDriverWait(driver,10).until(EC.presence_of_element_located(locator))
ele.send_keys("sdf")

print(ele)

time.sleep(5)
driver.quit()