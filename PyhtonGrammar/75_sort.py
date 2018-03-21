# @Time :18/3/21 下午5:06
# @Author :huangcaiyan
# @File : sort
# @Software : PyCharm

'''
75.排序
    sorted（array）默认从小到达从左到右依次排列；
    sorted(array,reverse=True) 从大到小从左到右依次排列（反排序）
'''
alist = [ 0 , 10 , 88 , 19 , 9 , 1 ]
print( sorted( alist ) )
print( sorted( alist , reverse=True ) )

alist.sort()
print(alist)
