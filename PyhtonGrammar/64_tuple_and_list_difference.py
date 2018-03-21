#@Time :18/3/21 下午4:16
#@Author :huangcaiyan
#@File : 65_tuple_and_list_difference
#@Software : PyCharm
'''
64.tuple 和 list 什么区别？
    tuple的元素不可改；
    tuple可改变指针指向；
    list的元素可修改；
'''

tuple_a = (1 , 2 , 3 , 4 , 5)
list_b = [ 1 , 2 , 3 , 4 , 5 ]

tuple_a = (10 , 2 , 3 , 4 , 5)
list_b[ 0 ] = 10

print( tuple_a )
print( list_b )
