#@Time :18/3/21 下午4:18
#@Author :huangcaiyan
#@File : 68_args_and_kwargs
#@Software : PyCharm
'''
68. *args, **kwargs 什么作用？
    1）＊args，可变的参数列表；
    2）＊＊kwargs，键值对参数列表；
'''


# arg
def test_args( first , *args ):
    print( first )
    for v in args:
        print( "args=" , v )


# args = (2, 3, 4, 5)
test_args( 1 , 2 , 3 , 4 , 5 , 6 )


# # kwargs
def test_kwargs( first , *args , **kwargs ):
    print( first )
    for v in args:
        print( "args %s" % v )
    for k , v in kwargs.items():
        print( "kwargs" , (k , v) )


# args = (2, 3, 4, 5)
# kwargs: k1=5, k2=6, k0=4
test_kwargs( 1 , 2 , 3 , 4 , 5 , k0=4 , k1=5 , k2=6 )