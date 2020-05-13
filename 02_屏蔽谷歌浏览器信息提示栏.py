"""
1、学习目标
隐藏谷歌浏览器信息提示栏：（Chrome 正受到自动化软件的控制。）

2、操作步骤
    1、导包
    2、添加谷歌浏览器加载项
        屏蔽信息提示栏
    3、打开谷歌浏览器---将屏蔽信息提示栏参数传入打开浏览器种
    4、打开地址
    5、关闭浏览器
"""




# 1、导包
from selenium import webdriver
import time 
# 2、添加谷歌浏览器加载项
options = webdriver.ChromeOptions()
#  屏蔽信息提示栏
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("excludeSwitches", ['enable-automation'])
# 3、打开谷歌浏览器---将屏蔽信息提示栏参数传入打开浏览器种
driver = webdriver.Chrome(options=options)
# 4、打开地址
url = "http://www.baidu.com"
driver.get(url)
# 5、关闭浏览器
time.sleep(5)
driver.quit()
