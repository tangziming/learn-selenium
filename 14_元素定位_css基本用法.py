"""
1、学习目标
    必须掌握css_selector元素定位方法
2、操作步骤（语法）
    2.1、selenium中的语法
        driver.find_element_by_css_selector('css表达式')
        driver.find_elements_by_css_selector('css表达式')
    2.2、css表达式
        1、id、class
            id ：#表示ID属性
            class：.表示class属性
        2、其他属性
            标签名[属性名=“属性值”]
        3、层级定位
            父标签[父标签属性名="父标签属性值"]>子标签    或者将“>”换成 空格
        4、索引
            父标签[父标签属性名="父标签属性值"]>子标签:nth-child(索引值)   索引从1开始 
        5、逻辑关系
            标签名[属性名1='属性值1'][属性名2='属性名2']
        6、模糊查询
            ^ 以什么开头
            ele_tag = driver.find_element_by_css_selector("input[placeholder^='请输入企业ID']")
            $ 以什么结尾
            ele_tag = driver.find_element_by_css_selector("input[placeholder*='请输入企业ID']")
            * 匹配所有
            ele_tag = driver.find_element_by_css_selector("input[placeholder*='请输入企业ID']")

"""     

from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "http://192.168.0.90/zfcapp/index.html#login"
driver.get(url)

time.sleep(2)

#使用class属性定位
ele_css = driver.find_element_by_css_selector(".title")
print("css_class",ele_css.get_attribute("outerHTML"))

#使用ID属性定位
ele_id = driver.find_element_by_css_selector("#button_｛login｝_01")
print("css_id",ele_id.get_attribute("outerHTML"))

#使用其他属性
ele_tag = driver.find_element_by_css_selector("input[placeholder='请输入企业ID']")
print("css_tag",ele_tag.get_attribute("outerHTML"))

#使用层级定位
ele_ceng = driver.find_element_by_css_selector("div[class='box box-ff']>p")
print("css_cengji",ele_ceng.get_attribute("outerHTML"))

#使用索引定位
ele_index = driver.find_element_by_css_selector("form.van-form>div:nth-child(2)>div:nth-child(2)")
print("css_index>>>>>>>>>",ele_index.get_attribute("outerHTML"))

#使用逻辑关系
ele_and = driver.find_element_by_css_selector("input[type='text'][name='职员编码/姓名/手机等']")
print("css_and<<<<<<<<<",ele_and.get_attribute("outerHTML"))

time.sleep(3)

driver.quit()