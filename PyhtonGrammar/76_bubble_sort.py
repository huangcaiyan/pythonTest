# @Time :18/3/21 下午5:37
# @Author :huangcaiyan
# @File : 76_bubble_sort
# @Software : PyCharm

def bubble_sort( lists ):
    # 获取列表长度
    count = len( lists ) - 1
    # n 个元素遍历 n 次
    for index in range( count , 0 , -1 ):
        # 第 i 个和第 i＋1 个进行对比
        print(index)
        for sub_index in range( index ):
            print( sub_index )
            if lists[ sub_index ] > lists[ sub_index + 1 ]:
                lists[ sub_index ] , lists[ sub_index + 1 ] = lists[ sub_index + 1 ] , lists[ sub_index ]
    return lists


alist = [ 0 , 10 , 88 , 19 , 9 , 1 ]
print( bubble_sort( alist ) )
