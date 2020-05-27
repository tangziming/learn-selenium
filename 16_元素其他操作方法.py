"""
1、学习目标
    掌握 定位超链接的方法: link_text, partial_link_text
2、操作步骤（语法）
    1、返回元素大小                               size   
    2、获取元素文本，元素文本值的是标签之间的文字    text
    3、获取页面title                              title
    4、获取当前页面url                           urrent_url
    5、获取属性值XXX：要获取标签内的属性名的值     get_attribute("xxx")
    6、判断元素是否可见，返回布尔值，true false       is_display()  
    7、判断元素是否可用，返回布尔值，true false       is_enabled()  
    提示：  
            1、size、text、title、current_url：为属性，调用时无括号；如:XXX.size
            2、title、current_url : 使用浏览器实例化对象直接调用; 如：driver.title
"""     

from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "http://192.168.0.90/zfcapp/index.html#login"
driver.get(url)

time.sleep(2)


input01 = driver.find_element_by_id("field_｛login｝_01")
button = driver.find_element_by_id("button_｛login｝_01")
#元素大小
print("元素大小:",input01.size)
#元素文本
print("元素文本:",button.text)
#获取页面title
print("获取页面title:",driver.title)
#获取当前页面url 
print("获取当前页面url :",driver.current_url)
#获取属性值
print("获取属性值:",input01.get_attribute("inputmode"))
#判断元素是否可见
print("判断元素是否可见:",input01.is_displayed())
#判断元素是否可用
print("判断元素是否可用:",button.is_enabled())



time.sleep(3)

driver.quit()