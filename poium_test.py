'''
这个测试库支持selenium/appium


> pip install poium

Page中有些js封装,需要的时候可以过来找


'''
from poium import Page, PageElement
from selenium import webdriver
import time

class BaiduIndexPage(Page):
    search_input = PageElement(name='wd')#搜索文本框
    search_button = PageElement(id_='su')#‘百度一下’按钮


driver = webdriver.Chrome()

page = BaiduIndexPage(driver)
page.get("https://www.baidu.com")

page.search_input = "poium"
time.sleep(5)
page.search_button.click()
time.sleep(5)

driver.quit()