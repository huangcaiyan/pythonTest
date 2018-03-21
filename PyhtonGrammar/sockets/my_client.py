#@Time :18/3/21 下午4:20
#@Author :huangcaiyan
#@File : my_client
#@Software : PyCharm

import socket

sk = socket.socket()

sk.connect( ('127.0.0.1' , 8888) )
while True:
    send_data = input( '输入发送内容：' )
    sk.sendall( bytes( send_data , encoding='utf8' ) )
    if send_data == 'bye':
        break
    accept_data = str( sk.recv( 1024 ) , encoding='utf8' )
    print( ''.join( '接收内容：' , accept_data ) )
