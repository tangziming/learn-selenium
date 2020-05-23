"""
1、学习目标
    掌握 定位超链接的方法: link_text, partial_link_text
2、操作步骤（语法）
    4、逻辑关系
        4.1、and 
        当元素属性玉其他元素有相同部分的时候，不能只利用一个属性定位
        需要多个元素属性进行定位， and 
        //标签名[@属性名1='属性值1' and @属性名2='属性值2'  and ，，，，]
        //input[@name='user' and @class='login-test']
"""     

from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "http://192.168.0.90/zfcapp/index.html#login"
driver.get(url)

time.sleep(2)

ele_input = driver.find_element_by_xpath("//input[@class='van-field__control' and @type='text']")
print("xpath逻辑",ele_input.get_attribute("outerHTML"))

time.sleep(3)

driver.quit()