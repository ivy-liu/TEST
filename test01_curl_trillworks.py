'''
https://curl.trillworks.com

'''
import requests
from concurrent.futures import ThreadPoolExecutor


cookies = {
    'BAIDUID': '106625EC54D47B0161A84CB23A9BB476:FG=1',
    'BDUSS': 'Uc3bW1vNmdhek53UFQtQ2p6cnlld1BSZUppSUV4MWlSbXZxQ0ItT1YyQkRjLTVjSVFBQUFBJCQAAAAAAAAAAAEAAADwEwkqwfXWrrW6AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEPmxlxD5sZcU',
    'ZD_ENTRY': 'sogou',
    'BIDUPSID': '106625EC54D47B0161A84CB23A9BB476',
    'PSTM': '1558795063',
    'BDRCVFR[5IRyTarJWqT]': 'mbxnW11j9Dfmh7GuZR8mvqV',
    'delPer': '0',
    'BD_CK_SAM': '1',
    'PSINO': '1',
    'BD_UPN': '15314753',
    'pgv_pvi': '8333405184',
    'pgv_si': 's8032889856',
    'BD_HOME': '1',
    'H_PS_PSSID': '1450_21093_29064_28518_29099_28835_28584_26350_22158',
}

headers = {
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36 OPR/60.0.3255.109',
    'Accept': 'text/plain, */*; q=0.01',
    'Referer': 'https://www.baidu.com/',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
}

params = (
    ('num', '8'),
    ('indextype', 'manht'),
    ('_req_seqid', '0xc3f798b9000406eb'),
    ('asyn', '1'),
    ('t', '1559463797888'),
    ('sid', '1450_21093_29064_28518_29099_28835_28584_26350_22158'),
)


#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://www.baidu.com/home/msg/data/personalcontent?num=8&indextype=manht&_req_seqid=0xc3f798b9000406eb&asyn=1&t=1559463797888&sid=1450_21093_29064_28518_29099_28835_28584_26350_22158', headers=headers, cookies=cookies)


def ten(i):
    response = requests.get('https://www.baidu.com/home/msg/data/personalcontent', headers=headers, params=params, cookies=cookies)
    
with ThreadPoolExecutor () as pool:  #创建线程池
    pool.map(ten,range(10))   //执行10次