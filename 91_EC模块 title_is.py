"""
1、学习目标
    掌握selenium中EC模块的使用方法
    expected_conditions 模块可以对网页上元素是否存在；可点击等等进行判断，
    一般用于断言或者与webdriverwait配合使用
    一般情况下，在使用expected_conditions类时都会对其进行重命名， 通过as 关键字对其重命名为EC
    

2、操作步骤（语法）
    引包： from selenium.webdriver.support import expected_conditions as EC

    title_is
    
    适用场景：
"""     

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

url = "http://192.168.0.90/zfcapp/index.html#login"
driver.get(url)
time.sleep(5)
ele = WebDriverWait(driver,10).until(EC.title_is("登录"),message="标题不正确")

print(ele)

time.sleep(5)
driver.quit()