"""
1、学习目标
    04_掌握selenium中控制浏览器大小的方法

2、操作步骤
    1、导包
    2、
        设置浏览器窗口大小，高度、宽度
        driver.set_window_size(宽，高)
        将浏览器最大化
        driver.maximize_window()
    3、打开谷歌浏览器
    4、打开地址
    5、关闭浏览器
"""



# 1、导包
from selenium import webdriver
import time

# 2、打开谷歌浏览器
driver = webdriver.Chrome()
# 3、设置浏览器窗口大小，高度、宽度

#   driver.set_window_size(宽，高)
driver.set_window_size(1000,500)

time.sleep(5)

#     将浏览器最大化
driver.maximize_window()

# 4、打开地址
url = 'http://www.baidu.com'
driver.get(url)
# 5、关闭浏览器
time.sleep(5)
driver.quit()