"""
1、学习目标
    二次定位的使用 
2、操作步骤（语法）
    2.1、先定位主元素 --select
        元素定位的八种方式
    2.2、定位主元素中的子元素 --option
        元素定位的八种方式
"""     

from selenium import webdriver
import time

# 2、添加谷歌浏览器加载项
options = webdriver.ChromeOptions()
#  移动端模式选项
mobileEmulation = {"deviceName":"iPhone X"}
options.add_experimental_option("mobileEmulation",mobileEmulation)
#  开发者模式
options.add_argument("--auto-open-devtools-for-tabs")
# 3、打开谷歌浏览器---将移动端模式选项参数传入打开浏览器种
driver = webdriver.Chrome(options=options)

url = "http://192.168.0.90/zfcapp/index.html#login"
driver.get(url)
time.sleep(2)

#登陆
companyID = driver.find_element_by_id("field_｛login｝_01").send_keys("2")
username = driver.find_element_by_id("field_｛login｝_02").send_keys("001")
password = driver.find_element_by_id("field_｛login｝_03").send_keys("123")
button = driver.find_element_by_id("button_｛login｝_01").click()




time.sleep(5)

driver.quit()