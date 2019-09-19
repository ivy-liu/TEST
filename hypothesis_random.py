# import random
# # import 

# # random.sample('123456789abcdefg',5)
# for i in range(5):
#     user_email=random.sample('123456789abcdefg',5)
#     print(user_email)
#     user_email=''.join(user_email)+'@163.com'
#     print(user_email)

# print('-------------------------')

'''
厉害一点的生成测试数据
pip install hypothesis
让测试数据更有价值
email生成，可能不一定符合各个公司的正则，使用要慎重，
按照正则写一个随机比较，正则校验什么的可以手工测试
个人认为

'''
import unittest
from hypothesis import given,settings
import hypothesis.strategies as st 


class AddTest(unittest.TestCase):  
    #数字 
    @settings(max_examples=3)
    @given(a=st.integers(),b=st.integers())
    def test_case_01(self,a,b):
        print('a->',a)
        print('b->',b)
        c1=a+b
        c2=sum([a,b])
        self.assertEqual(c1,c2)
    #email
    @settings(max_examples=4)
    @given(a=st.emails())
    def test_case_02(self,a):
        print('a->',a)
        # print('b->',b)
        # c1=a+b
        # c2=sum([a,b])
        self.assertIn('@',a)


if __name__=='__main__':
    unittest.main()


'''
a-> 0
b-> 0
a-> 14
b-> 8344
a-> 32
b-> -48
.a-> 0@A.com
a-> zN#KL#T/+'C*hd%*+@MQeo.lACAIXa
a-> e@r.O1J--D.boEHRInGEr
a-> ^0@Qr.DeliVerY
.
----------------------------------------------------------------------
Ran 2 tests in 0.555s

OK
'''