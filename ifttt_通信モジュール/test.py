# iftttのモジュールテスト
from ifttt_tushin import IftttTushin as ifttt

meirei ={
        "on": ("ライトを点けます", "irsend SEND_ONCE led on"), 
        "off": ("ライトを消します", "irsend SEND_ONCE led off"),
        "mame": ("豆電球をつけます", "irsend SEND_ONCE led mame"),
        "dan": ("暖房を点けます", "irsend SEND_ONCE led dan"),
        "rei": ("冷房を点けます", "irsend SEND_ONCE led rei"),
        "stop": ("エアコンを止めます", "irsend SEND_ONCE led stop")
        }
ifttt("token_3EXsGJPRpa4Jb9mo", "GoogleHome/data", "/home/takayuki/py/module/ifttt_通信モジュール/mqtt.beebotte.com.pem", meirei)