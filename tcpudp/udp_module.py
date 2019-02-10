# UDP 通信モジュール
import socket
import concurrent.futures

class Udp:
    def __init__(self, IPaddress, PORT):
        self.IPaddress = IPaddress
        self.PORT = PORT

    def udp_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.bind((self.IPaddress, self.PORT))   
            # print("UDPサーバー起動中")
            data, addr = s.recvfrom(1024)
            data2 = data.decode()
            # print("data: {}, addr: {}".format(data, addr))
        return data2, addr

    def udp_client(self, data):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect((self.IPaddress, self.PORT))
            data2 = data.encode()    
            s.sendall(data2) 


if __name__ == "__main__":
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
    
    def udp_sloop():
        while True:
            data, addr = udp_s.udp_server()
            print("data: {}, addr: {}".format(data, addr))

    def udp_cloop():
        while True:
            data = input("挨拶を入力してね:")
            udp_c.udp_client(data)

    udp_s = Udp("127.0.0.1", 50000)
    executor.submit(udp_sloop)
    udp_c = Udp("127.0.0.1", 50000)
    executor.submit(udp_cloop)

            

    