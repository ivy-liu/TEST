from selenium import webdriver
import time

driver=webdriver.Firefox()  #选择浏览器
driver.get("https://www.baidu.com")
cookie_1={"name":"BAIDUID","value":"D99D40F90C8602C91D4F3469DFDCE81A:FG=1"}#应该有这个
cookie_2={"name":"BDUSS","value":"U3bmpCcjU3cHlKbVBwVGZGNTJ5SFdKQllvdmJEM1hHTTRlWU5hR1JpYXkxeWRkSUFBQUFBJCQAAAAAAAAAAAEAAADwEwkqwfXWrrW6AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALJKAF2ySgBdVU"} #可能有这个
#cookie_3={"name":"BIDUPSID","value":"D99D40F90C8602C91D4F3469DFDCE81A"} #可能有这个 没有

time.sleep(5) #
driver.add_cookie(cookie_1)
driver.add_cookie(cookie_2)
driver.get("https://www.baidu.com")