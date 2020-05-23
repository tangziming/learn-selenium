"""
1、学习目标
    掌握 定位超链接的方法: xpath
2、操作步骤（语法）
    1、xpath
        dirver.find_element_by_xpath("xpath路径")
        
    2、xpath表达式
        2.1、绝对路径
            从根节点开始一层一层进行查找
            /表示绝对路径
            /html/body/div/div/div/form/div/div[2]/div/input
        2.2、相对路径（重点）
            //表示相对路径
            1、使用标签+属性定位
                //标签名[@属性名='属性值']
                //input[@id='field_｛login｝_01']
            2、层级定位
                //父标签[@父标签属性名='父标签属性值']/子标签名
                //button[@id='button_｛login｝_01']/span
                注意:层级定位不仅限于2层，可以是多层的
            
                
"""     

from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "http://192.168.0.90/zfcapp/index.html#login"
driver.get(url)

time.sleep(2)

#绝对路径定位
#xpath_abs = driver.find_element_by_xpath("/html/body/div/div/div/form/div/div[2]/div/input")
#print(xpath_abs.get_attribute("outerHTML"))

#使用标签+属性定位
#xpath_input = driver.find_element_by_xpath("//input[@id='field_｛login｝_01']")
#print(xpath_input.get_attribute("outerHTML"))

#层级定位
xpath_span = driver.find_element_by_xpath("//button[@id='button_｛login｝_01']/span")
print(xpath_span.get_attribute("outerHTML"))

driver.quit()