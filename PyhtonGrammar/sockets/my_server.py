#@Time :18/3/21 下午4:20
#@Author :huangcaiyan
#@File : my_server
#@Software : PyCharm

import socketserver


class MyServer( socketserver.BaseRequestHandler ):
    def handle( self ):
        while 1:
            conn = self.request
            addr = self.client_address
            '''
            以上两行代码等同于 conn, addr = socket.accept()，
            只不过socketserver模块中已经替我们包装好了，
            还替我们包装了bind()、listen()、accept()方法

            '''
            
            while 1:
                accept_data = str( conn.recv( 1024 ) , encoding='utf8' )
                print( accept_data )
                if accept_data == 'bye':
                    break
                send_data = bytes( input( '>>>>>' ) , encoding='utf8' )
                conn.sendall( send_data )
            conn.close


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer( ('127.0.0.1' , 8888) , MyServer )
    server.serve_forever()