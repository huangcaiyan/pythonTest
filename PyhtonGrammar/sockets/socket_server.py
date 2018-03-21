#@Time :18/3/21 下午4:19
#@Author :huangcaiyan
#@File : socket_server
#@Software : PyCharm

import socket

# 创建 socket 对象
sk = socket.socket()

# 绑定端口
sk.bind( ('localhost' , 9008) )
sk.listen( 5 )
#
while True:
    conn , addr = sk.accept()
    while True:
        accept_data = str( conn.recv( 1024 ) , encoding='utf-8' )
        # print( ''.join( [ '接收内容：' , accept_data , '     客户端口：' , str( addr[ 1 ] ) ] ) )
        print( '服务端 接收内容：' , accept_data )
        if accept_data == 'bye':
            break
        send_data = input( '输入发送内容：' )
        conn.sendall( bytes( send_data , encoding='utf-8' ) )
    conn.close()