import requests
import re,json
import unittest

Url = 'https://maoyan.com/board?4'

def get_html(Url):
    user_agent = 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
    #不要用中划线命名，报错can't assign to operator
    headers={'User-Agent':user_agent}

    response_first = requests.get(url=Url,headers=headers)

    html=response_first.text
    print(html)
    return html



#2.正则匹配
def parse_one_page(html):
    #主演+时间+名称
    #编译成对象，提高效率
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
        +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
        +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    # .*? 匹配任意字符，懒惰匹配
    # (.*?) 匹配到，取出来
    # re.S 匹配换行符
    items=re.findall(pattern,html)
    # print(items)
    #()元组不可变，[]列表可变
    for item in items:
        yield{
            'number':item[0],
            'image_url':item[1],
            'name':item[2],
            'actor':item[3].strip()[3:],
            'time':item[4].strip()[5:],
            'score':item[5]+item[6]
        }

html=get_html(Url)
for item in parse_one_page(html):
    print (item)