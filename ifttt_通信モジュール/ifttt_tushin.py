# iftttと通信するためのモジュール

import paho.mqtt.client as mqtt     # インストールされてない場合は、"$sudo pip3 install paho-mqtt"でインストール
import json
import os

class IftttTushin:
    def __init__(self, token, topic, cacert, meirei):
        self.TOKEN = str(token)    # ifttと同じトークンナンバー
        self.HOSTNAME = "mqtt.beebotte.com"
        self.PORT = 8883
        self.TOPIC = str(topic)           # Beebotteのチャンネル/リソース
        self.CACERT = cacert
        self.meirei = meirei

       
        client = mqtt.Client()
        client.username_pw_set("token:%s"%self.TOKEN)
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.tls_set(self.CACERT)
        client.connect(self.HOSTNAME, port=self.PORT, keepalive=60)
        client.loop_forever()



    def on_connect(self, client, userdata, flags, respons_code):
        print("起動しました。" + 'status {0}'.format(respons_code))
        client.subscribe(self.TOPIC)

    def on_message(self, client, userdata, msg):
        # print(msg.topic + " " + str(msg.payload))
        data = json.loads(msg.payload.decode("utf-8"))["data"][0]
        data = {key:value.strip() for key, value in data.items()}

        # ここに、LPRCの処理を書き込む
        for command in self.meirei:
            # print(i)
            # print(self.meirei[i])
            action = self.meirei[command]
            # print(action[0])
            # print(action[1])

            if data["device"] == "led":
                if data["action"] == command:
                    print(action[0])
                    os.system(action[1])
            else:
                print("設定されてません。")


if __name__ == "__main__":
    meirei ={"on": ("ライトを点けます", "echo light on"), "off": ("ライトを消します", "echo light off")}
    IftttTushin("token_3EXsGJPRpa4Jb9mo", "GoogleHome/data", "/home/takayuki/py/module/ifttt_通信モジュール/mqtt.beebotte.com.pem", meirei)

    #　IftttTushin(token="トークン番号", topic="チャンネル名/リソース名", cacert="mqtt.beebotte.com.pemファイルの場所", meirei=命令の辞書)
    

    

   
        

    