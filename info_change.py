'''
验证输入的信息，是否符合预期
个别情况出现，实际输入的信息，不是预期要输入的信息

'''

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By



driver=webdriver.Chrome()
driver.get('http://www.5itest.cn/login?goto=http%3A//www.5itest.cn/')
time.sleep(5)
result_title=EC.title_contains("注册")
print(result_title)
# DevTools listening on ws://127.0.0.1:61930/devtools/browser/9898bafd-9664-4ffa-a430-466fab48a40f
# <selenium.webdriver.support.expected_conditions.title_contains object at 0x0000026120926D30>
'''
EC.title_contains("注册")
使用这个，简单验证一下title是否可见，确定网页是不是加载好了
'''


element=driver.find_element_by_id("login_username")
element.send_keys("qerqewre")

info01=element.get_attribute("placeholder")
print(info01)# 邮箱/手机/用户名
info02=element.get_attribute("value")
print(info02)# qerqewre

time.sleep(3)
driver.close()