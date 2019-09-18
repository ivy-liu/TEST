'''
验证title
验证元素
显性等待


'''

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.get('http://www.5itest.cn/register')
time.sleep(5)
result_title=EC.title_contains("注册")
print(result_title)
# DevTools listening on ws://127.0.0.1:61930/devtools/browser/9898bafd-9664-4ffa-a430-466fab48a40f
# <selenium.webdriver.support.expected_conditions.title_contains object at 0x0000026120926D30>
'''
EC.title_contains("注册")
使用这个，简单验证一下title，确定网页是不是加载好了
'''


element_node=driver.find_elements_by_class_name("controls")[1]
element_node.find_element_by_class_name("form-control").send_keys("qerqewre")

time.sleep(3)




result_element=EC.visibility_of_element_located(element_node)
print(result_element)
# <selenium.webdriver.support.expected_conditions.visibility_of_element_located object at 0x000001F6AD1D6D68>   
'''
EC.visibility_of_element_located(element_node)
使用这个，验证一下element，确定网页是不是加载好了
'''

locator=(By.CLASS_NAME,"controls")
WebDriverWait(driver,1).until(EC.visibility_of_element_located(locator))
'''
WebDriverWait(driver,1).until(EC.visibility_of_element_located(locator))
验证locator存在，执行，超时时间1
显性等待 详细在笔记中

显性等待 针对元素
WebDriverWait，配合该类的until()和until_not()方法，就能够根据判断条件而进行灵活地等待。
举个栗子，每隔N秒检查下，如果条件成立了，则执行下一步，否则继续等待，知道超过设置的最长时间，然后抛出TimeoutException异常。

语法如下：
from selenium,webdriver.support.wait import WebDriverWait
WebDriverWait(driver，超时时长，调用频率).until(可执行方法，超时的时候返回的信息)
例如：
WebDriverWait(driver,10).until(lambda x:x.find_element_by_id("words")).send_keys("测试测试测试")
参数解释：
	• driver：
	• 超时时长：就是最大等待时间
	• 调用频率：调用until或者until_not中的方法的间隔时间，默认0.5秒
	• until是当某原色出现或什么条件成立则继续执行，until_not是当某元素消失或什么条件不成立则继续执行

'''



driver.implicitly_wait(5)
'''
隐形等待
对整个driver的周期都起作用，所以只要设置一次即可。和sleep不同。
'''


driver.close()