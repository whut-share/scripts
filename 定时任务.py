#coding=utf-8 

import time
import datetime
import requests
from dingtalkchatbot.chatbot import DingtalkChatbot

def send_msg(msg):
    # WebHook地址
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=d344ab8611f2a97d2ed20ad25b1d6f1acc6f0d4ea08dd13ee6085736bf30a472'
    # 初始化机器人小丁
    xiaoding = DingtalkChatbot(webhook)
    # Text消息@所有人
    xiaoding.send_text(msg=msg, is_at_all=True)

def check_work_day():
    t = time.strftime('%Y%m%d',time.localtime(time.time()))
    url = "http://api.goseek.cn/Tools/holiday"

    querystring = {"date":t}

    headers = {
        'Cache-Control': "no-cache",
        'Postman-Token': "f5002250-6b6e-46ae-9cda-df9bd015a6dd"
        }

    response = requests.request("POST", url, headers=headers, params=querystring)

    code = response.text[-2]
    return code

def main():
    print("Start run the py")
    while True:
        now_time = time.strftime('%H%M',time.localtime(time.time()))
        localtime = time.localtime(time.time())
        if now_time == '2200':
            code = check_work_day()
            if int(code) == 0:
                send_msg("Don't forget to log in!")
            time.sleep(70)
        
        if localtime.tm_wday == 4 and now_time == '2100':
            send_msg("Prepare a weekly report!")
            time.sleep(70)
        if localtime.tm_wday == 6 and now_time == '2100':
            send_msg("Submit a weekly report!")
            time.sleep(70)
        time.sleep(45)

if __name__ == "__main__":
    main()


