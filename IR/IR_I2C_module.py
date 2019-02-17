# I2c_IRremote_controllerにコードを送信するプログラム

import smbus                #I2C通信するためのモジュールsmbusをインポートする
from time import time                 #sleepするためにtimeモジュールをインポートする
from ir_list import ir_list as il

class IrI2cSend:
    def __init__(self, adress):
        self.bus = smbus.SMBus(1)    ##I2C通信するためのモジュールsmbusのインスタンスを作成
        self.adress = adress          #arduinoのサンプルプログラムで設定したI2Cチャンネル
        self.buf = []

    def irsend(self, code):
        for i in code:
            self.buf.append(i >> 8)                          # 16ビットの数値を8ビットずつに分ける
            self.buf.append(i & 0b11111111)
            self.bus.write_i2c_block_data(self.adress, 0x80, self.buf)     # bufに入った2つのbyteを送信   
            self.buf = []

        self.bus.write_byte_data(self.adress, 0x00, 0x01)     # I2C機器(arduino)の赤外線を光らせる命令  

if __name__ == "__main__":
    ir = IrI2cSend(0x04)
    ir.irsend(il().LED_ON)