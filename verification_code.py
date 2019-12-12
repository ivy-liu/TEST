'''
解析验证码
下载-解析

'''
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
# from poium import Page, PageElement
# KeyError: "Please use a locator：
# 'id_'、'name'、'class_name'、'css'、'xpath'、
# 'link_text'、'partial_link_text'."

driver=webdriver.Chrome()
driver.get('http://www.5itest.cn/register?goto=http%3A//www.5itest.cn/')
time.sleep(5)



#下载图片
driver.save_screenshot('verification_code_pic\\01_s_pic.png')
code_element=driver.find_element_by_id('getcode_num')
print(code_element.location)#{'x': 538, 'y': 523}
x1=code_element.location['x']
y1=code_element.location['y']
x2=code_element.size['width']+x1
y2=code_element.size['height']+y1
print('x1:',x1,' y1:',y1,' x2:',x2,' y2:',y2)
time.sleep(4)

'''
pip install Pillow

from PIL import Image

处理图片,裁剪图片可以
'''
from PIL import Image
img=Image.open('verification_code_pic\\01_s_pic.png')
image=img.crop((x1,y1,x2,y2))
image.save('verification_code_pic\\02_s_pic_code.png')

#以上，裁剪到的图片验证码不准，受浏览器影响估计

'''
from urllib.request import urlretrieve
urlretrieve(pic_url, 'verification_code_pic\\03_pic_code.png')
下载图片很方便
'''
# import urllib
from urllib.request import urlretrieve

# 首先对验证码进行定位
pic = driver.find_element_by_id('getcode_num')
# 获取验证码的src属性
pic_url = pic.get_attribute('src')
# 保存验证码图片到指定路径
urlretrieve(pic_url, 'verification_code_pic\\03_pic_code.png')

#这个没毛病，拿到验证码图片

'''
pip install pytesseract
识别文字
import pytesseract
报错：tesseract is not installed or it's not in your path
tesseract-ocr-setup-4.00.00dev.exe
需要安装这个文件，然后
pytesseract.py中更改
 tesseract_cmd = 'tesseract'
 为安装时的目录
 esseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

 该方法只能识别，比较正常的文字，验证码这个比较扭曲的识别不成功！！
'''
 
# import pytesseract
# image=Image.open('verification_code_pic\\03_pic_code.png')
# text=pytesseract.image_to_string(image)
# print(text)


'''
https://www.showapi.com/apiGateway/view?apiCode=184
一个付费比较便宜的图片识别
# 需要引入requests包 ：运行终端->进入python/Scripts ->输入：pip install requests

下载扩展包 ShowapiRequest.py 放在当前目录下，引用

'''
from ShowapiRequest import ShowapiRequest

r = ShowapiRequest("http://route.showapi.com/184-5","my_appId","my_appSecret" )#appId、appSecret在我的应用中
r.addBodyPara("img_base64", "")
r.addBodyPara("typeId", "34")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
res = r.post()
print(res.text) # 返回信息


driver.close()







