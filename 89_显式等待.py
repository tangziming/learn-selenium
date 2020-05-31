"""
1、学习目标
    掌握selenium中显式等待的使用方法

    在设定时间内，针对某一个元素，默认每隔一段时间检测该元素是否存在，
    如果超过设定时间检测不到则抛出异常

2、操作步骤（语法）
    引包： from selenium.webdriver.support.wait import WebDriverWait
    WebDriverWait()
    WebDriverWait(driver, timeout ,poll_frequency = 0.5 ,ignored_excptions=Nome)
    driver - webdriver的驱动程序
    timeout - 最长休眠时间，默认以秒为单位
    poll_frequency - 休眠时间的间隔时间，默认为 0.5秒
    ignored_excptions - 超时后的异常信息，默认情况下抛NoSuchElementExcption异常

    until() 、 until_not()
    until(method , message='')
    method - 在等待时期，每隔一段时间调用传入的这个方法，直到返回true
    message -   如果超时，抛出TimeoutExcption , 将message 传入异常
    until_not(method , message='')
    与until相反，until是当某元素出现或者什么条件成立则继续执行。
    until_not时当某元素消失或什么条件不成立则继续执行
    适用场景：
"""     

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome()

url = "http://192.168.0.90/zfcapp/index.html#login"
driver.get(url)

ele = WebDriverWait(driver,10).until(lambda x: x.find_element_by_id("field_｛login｝_022"),message="找不到用户名")

ele.send_keys("tzm")

time.sleep(5)
driver.quit()