from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
driver=webdriver.Chrome()
driver.get('http://www.5itest.cn/register')
time.sleep(5)
result=EC.title_contains("注册")
print(result)
# DevTools listening on ws://127.0.0.1:61930/devtools/browser/9898bafd-9664-4ffa-a430-466fab48a40f
# <selenium.webdriver.support.expected_conditions.title_contains object at 0x0000026120926D30>
'''
EC.title_contains("注册")
使用这个，简单验证一下，是不是加载好了
'''

