"""
1、学习目标
    掌握selenium中隐式等待的使用方法
2、操作步骤（语法）
    driver.implicitly_wait(时间) #时间单位 秒
    时间： 最大等待时间
    隐式等待时通过一定的时长等待页面所有元素加载完成。
    如果超出了设置的时长，元素还没有被加载，则抛出NoSuchElementException异常。

    适用场景：
        当需要验证页面上所有元素加载完成的时间时，可以使用隐式等待
"""     

from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "http://192.168.0.90/zfcapp/index.html#login"
driver.get(url)

print("开始等待",time.time())
driver.implicitly_wait(5)

try:
    companyid = driver.find_element_by_id("field_｛login｝_01")
    print("正常结束等待",time.time())
    companyid.send_keys("2222")
except Exception as  msg:
    print(msg)
    print("报错结束等待",time.time())

time.sleep(3)

driver.quit()