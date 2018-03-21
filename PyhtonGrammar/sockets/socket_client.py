#@Time :18/3/21 下午4:19
#@Author :huangcaiyan
#@File : socket_client
#@Software : PyCharm

import socket

# 创建 socket 对象
sk = socket.socket()
sk.connect( ('127.0.0.1' , 9008) )

while True:
    send_data = input( '输入发送内容：' )
    sk.sendall( bytes( send_data , encoding='utf-8' ) )
    if send_data == 'bye':
        break
    accept_data = str( sk.recv( 1024 ) , encoding='utf-8' )
    # print(''.join(('接收内容：',accept_data)))
    print( '客户端 接收内容：' , accept_data )
sk.close()
