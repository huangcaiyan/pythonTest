# @Time :18/3/21 下午4:24
# @Author :huangcaiyan
# @File : match_and_search_difference
# @Software : PyCharm

import re

s1 = 'helloworld,helloworld'
w1 = 'hello'
w2 = 'world'

# search 扫描整个字符串
print( 'search1=' , re.search( w1 , s1 ).span() )
print( 'search2=' , re.search( w2 , s1 ).span() )

# match只在字符串开始的位置匹配
print( 'match1=' , re.match( w1 , s1 ).end() )
print( 'match2=' , re.match( w2 , s1 ) )
