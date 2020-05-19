"""
1、学习目标
    掌握 定位超链接的方法: link_text, partial_link_text
2、操作步骤（语法）
    1、link_text
        driver.find_element_by_link_text("超链接文本全部内容")
    2、partial_link_text
        driver.find_element_by_partial_link_text("超链接文本的部分内容")
        部分内容一定是连续的内容
"""     

from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "http://192.168.0.90/zfcapp/index.html#login"
driver.get(url)

time.sleep(2)

link_elements = driver.find_element_by_link_text("忘记密码？")
print(link_elements)
print(link_elements.get_attribute("outerHTML"))
print(link_elements.get_attribute("outerText"))

link_elements1 = driver.find_element_by_partial_link_text("忘记")
print(link_elements.get_attribute("outerHTML"))
print(link_elements.get_attribute("outerText"))


time.sleep(3)

driver.quit()