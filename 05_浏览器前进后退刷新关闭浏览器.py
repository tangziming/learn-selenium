"""
1、学习目标
    05_浏览器前进、后退、刷新、关闭浏览器的方法

2、操作步骤
    1、导包
    2、打开谷歌浏览器
    3、打开地址
    4、
        4.1、 前进
            driver.forward()
        4.2、 后退
            driver.back()
        4.3、 刷新
            driver.refresh()
        4.4、关闭浏览器
            driver.close()  #只关闭浏览器不关闭浏览器驱动欧冠
            driver.quit()  #即关闭浏览器也关闭浏览器驱动
    5、关闭浏览器
"""

# 1、导包
from selenium import webdriver
import time 
# 2、打开谷歌浏览器 并且最大化
driver = webdriver.Chrome()
driver.maximize_window()
# 3、打开地址
urltaobao = "http://www.taobao.com"
urljingdong = "http://www.jd.com"
urlbaidu = "http://www.baidu.com"
driver.get(urlbaidu)
driver.get(urltaobao)
driver.get(urljingdong)

# 4、
# 4.1、 后退
#     driver.back()
driver.back()  #后退到淘宝
time.sleep(2)
driver.back()  #后退到百度
time.sleep(2)
# 4.2、 前进
#     driver.forward()
driver.forward()  #前进到淘宝
time.sleep(2)
# 4.3、 刷新
#     driver.refresh()
driver.refresh() #保持在淘宝
time.sleep(2)
# 5、关闭浏览器
driver.quit()