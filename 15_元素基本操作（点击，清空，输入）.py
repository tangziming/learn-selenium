"""
1、学习目标
    掌握 定位超链接的方法: link_text, partial_link_text
2、操作步骤（语法）
    2.1、清空文本 clear()
        element.clear()
    2.2、点击 click()
        element.click()
    2.3、输入 send_keys()
        element.send_keys("输入的内容")
"""     

from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "http://192.168.0.90/zfcapp/index.html#login"
driver.get(url)

time.sleep(2)

#输入公司ID
driver.find_element_by_id("field_｛login｝_01").send_keys("2222222")
#清空公司ID
time.sleep(2)
driver.find_element_by_id("field_｛login｝_01").clear()
#重新输入公司ID
time.sleep(2)
driver.find_element_by_id("field_｛login｝_01").send_keys("2")

#输入用户名
driver.find_element_by_id("field_｛login｝_02").send_keys("001")
#输入密码
driver.find_element_by_id("field_｛login｝_03").send_keys("123")

#点击登陆
driver.find_element_by_id("button_｛login｝_01").click()

time.sleep(3)

driver.quit()