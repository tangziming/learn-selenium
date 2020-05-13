"""
1、学习目标
    03_使用移动端模式打开谷歌浏览器：开发者模式，移动端模式

2、操作步骤
    1、导包
    2、添加谷歌浏览器加载项
        设置手机型号
        mobileEmulation = {"deviceName":"iPhone 6"}
    3、打开谷歌浏览器---将屏蔽信息提示栏参数传入打开浏览器种
    4、打开地址
    5、关闭浏览器
"""




# 1、导包
from selenium import webdriver
import time 
# 2、添加谷歌浏览器加载项
options = webdriver.ChromeOptions()
#  移动端模式选项
mobileEmulation = {"deviceName":"iPhone 6"}
options.add_experimental_option("mobileEmulation",mobileEmulation)
#  开发者模式
options.add_argument("--auto-open-devtools-for-tabs")
# 3、打开谷歌浏览器---将移动端模式选项参数传入打开浏览器种
driver = webdriver.Chrome(options=options)
# 4、打开地址
url = "http://www.baidu.com"
driver.get(url)
# 5、关闭浏览器
time.sleep(5)
driver.quit()
