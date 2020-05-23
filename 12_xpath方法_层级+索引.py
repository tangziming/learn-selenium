"""
1、学习目标
    掌握 定位超链接的方法: link_text, partial_link_text
2、操作步骤（语法）
    3、索引
        当一个父标签有多个相同的子标签时
        //父标签[@父标签属性名='父标签属性值']/子标签名[索引值]
        xpath索引从1开始
"""     

from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "http://192.168.0.90/zfcapp/index.html#login"
driver.get(url)

time.sleep(2)

ele_div2 = driver.find_element_by_xpath("//form[@class='van-form']/div[2]")
ele_div3 = driver.find_element_by_xpath("//form[@class='van-form']/div[3]") 
print("第二个div",ele_div2.get_attribute("outerHTML"))
print("第三个div",ele_div3.get_attribute("outerHTML"))

time.sleep(3)

driver.quit()