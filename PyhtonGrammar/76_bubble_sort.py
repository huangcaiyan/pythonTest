# @Time :18/3/21 下午5:37
# @Author :huangcaiyan
# @File : 76_bubble_sort
# @Software : PyCharm

# def bubble_sort( lists ):
#     # 获取列表长度
#     count = len( lists ) - 1
#     # n 个元素遍历 n 次
#     for index in range( count , 0 , -1 ):
#         # 第 i 个和第 i＋1 个进行对比
#         # print(index)
#         print( 'yayaya:' , lists )
#         for sub_index in range( index ):
#             print( sub_index )
#             if lists[ sub_index ] > lists[ sub_index + 1 ]:
#                 lists[ sub_index ] , lists[ sub_index + 1 ] = lists[ sub_index + 1 ] , lists[ sub_index ]
#                 print( '呵呵哒：' , lists )
#
#     return lists
#
#
# # alist = [ 0 , 10 , 88 , 19 , 9 , 1 ]
# alist = [ 'A' , 'Z' , 'K' , 'C' , 'F' , 'B' ]
#
# print( bubble_sort( alist ) )


def bubble_sorts( lists ):
    count = len( lists ) - 1
    for i in range( 0 , count ):
        for j in range( i + 1 , count ):
            if lists[ i ] > lists[ j ]:
                lists[ i ] , lists[ j ] = lists[ j ] , lists[ i ]
                print( 'lists=' , lists )
    
    return lists


alist = [ 0 , 10 , 88 , 19 , 9 , 1 ]
print( 'bubble_sorts==' , bubble_sorts( alist ) )
