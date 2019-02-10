# TCP/UDP 通信モジュール
import socket
from time import sleep
import concurrent.futures

class Tcp:
    def __init__(self, IPaddress, PORT):
        self.IPaddress = IPaddress
        self.PORT = PORT

    def tcp_client(self, data):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.IPaddress, self.PORT))
            data = str(data).encode()
            s.sendall(data)
            data2 = s.recv(1024)
            data2 = data2.decode()
            print(data2)
        return data2

if __name__ == "__main__":
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
    
    # tcpのサーバーは、tcp_Sloopの内容をコピーして使う
    def tcp_sloop():
        IPaddress = "127.0.0.1"
        PORT = 50000

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((IPaddress, PORT))
            s.listen(1)
            print("TCPサーバー起動中") 
            while True:
                conn, addr = s.accept()
                data = conn.recv(1024)
                data2 = data.decode()
                
                # ここから処理を書く


                print("data : {}, addr: {}".format(data2, addr))

                
                # ここまで処理を書く
                conn.sendall(b"Received: " + data)

    def tcp_cloop():
        while True:
            data = input("挨拶を入力してね:")
            tcp_c.tcp_client(data)

    executor.submit(tcp_sloop)
    tcp_c = Tcp("127.0.0.1", 50000)
    executor.submit(tcp_cloop)