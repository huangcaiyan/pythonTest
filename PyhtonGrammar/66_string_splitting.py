#@Time :18/3/21 下午4:17
#@Author :huangcaiyan
#@File : 66_string_splitting
#@Software : PyCharm

'''
66.字符串的拆分方法有哪些？

    1)string 对象的 split 方法，不允许有多个分隔符；
    2)函数 re.split()，允许为分隔符指定多个正则模式；
    3)re.split(pattern,string,maxsplit),
        pattern:匹配的正则表达式、
        string：要匹配的字符串、
        maxsplit：分割次数
'''

line = 'I am super man!'

# string 的 split方法
print( line.split( ' ' ) )

# re 的 split 方法

import re

print( re.split( 'a' , line , 2 ) )