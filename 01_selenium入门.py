"""
最简单的demo
"""

# 导入selenium
from selenium import webdriver

#打开浏览器
dirver  = webdriver.Chrome()

#访问被测地址（百度）
dirver.get('http://www.baidu.com')

#操作地址
#@%#@……%！……￥%#！   

#关闭浏览器
dirver.quit()