# @Time :18/3/21 下午4:14
# @Author :huangcaiyan
# @File : 63_lambda_function
# @Software : PyCharm

"""
63.什么是lambda函数？
    1）匿名函数，即没有函数名多函数；
"""
# # 计算加法
# def plus( x , y ):
#     return x + y
#
#
# # 计算平方
# def square( z ):
#     return z ** 2
#
#
# print( plus( 1 , 2 ) )
# print( square( 3 ) )

# # lambda表达式 加法
p = lambda x , y: x + y
print( p( 1 , 2 ) )

# lambda表达式 平方
s = lambda x: x ** 2
print( s( 3 ) )
