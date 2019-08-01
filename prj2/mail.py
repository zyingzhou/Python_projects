#! /usr/bin/env python
# coding='utf-8'
"""
用Python发送带html形式的E-mail
Author: zhiying
URL: https://www.zhouzying.cn
Date: 2019-08-01
"""
import smtplib
from email.header import Header
from email.mime.text import MIMEText
import math
import time
import datetime


def send_mail(content, theme):
    # 设置信息
    from_addr = '******@126.com'
    # 授权码
    password = '******'
    to_addr = "******@qq.com"
    # 邮件服务器地址
    smtp_server = 'smtp.126.com'

    # 邮件信息,文本类型：1.文本--‘plain’, 2.网页--‘html’
    msg = MIMEText(content, 'html', 'utf-8')
    msg['From'] = from_addr
    msg['To'] = to_addr

    # msg['Subject'] = Header('这里填写邮件的主题', 'utf-8').encode()
    msg['Subject'] = Header(theme, 'utf-8').encode()
    # 连接邮件服务器
    server = smtplib.SMTP_SSL(smtp_server, 465)
    # 登录邮件
    server.login(from_addr, password)
    print("登录成功!")
    # 开始发送邮件
    server.send_message(msg, from_addr, to_addr)
    # 退出服务器
    server.quit()
    print("邮件发送成功!")


def countdown():
    # math.trunc()是取整函数
    now = time.time()
    now_time = math.trunc(now)
    # 结束时间为:2019-12-21 09:00:00
    end = datetime.datetime(2019, 12, 21, 9, 0, 0)
    end_time = time.mktime(end.timetuple())
    delta_time = end_time - now_time
    # 天
    d = delta_time // 3600 // 24
    # 时
    h = delta_time // 3600 % 24
    # 分
    m = delta_time // 60 % 60
    # 秒
    s = delta_time % 60
    # print('时间差为{}s'.format(delta_time))
    print('今天距离2020年考研还有:{}天{}小时{}分{}秒'.format(math.trunc(d), math.trunc(h), math.trunc(m), math.trunc(s)))
    return d, h, m, s


def main():
    d, h, m, s = countdown()
    script = """
    <html xmlns="http://www.w3.org/1999/xhtml" lang="en">
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>考研倒计时日历_距离2020年研究生考试</title>
    </head>
    <body>
            <div class="timer" style="background:#37543a;width: 300px;height: 240px;border: 20px solid #e5be6b; 
            text-align: center">
                <!--考研倒计时开始-->
                <div class="time1 timeActive">
                    <h3>2020年考研倒计时</h3>
                        <br />2020考研初试时间：
                        <br />2019年12月21日-12月23日<br />
                        <br />目前距离2020年考研还有:<br />
                    <DIV id="CountMsg" class="HotDate">
                        <strong>
                        <span id="t_d" style="color: red" >%d 天</span>
                        <span id="t_h" style="color: aquamarine">%d 时</span>
                        <span id="t_m" style="color: chartreuse">%d 分</span>
                        <span id="t_s" style="color: gold">%d 秒</span>
                        <br />任何值得梦想的地方都没有捷径！
                        </strong>
                    </DIV>
                </div>
                <!--考研倒计时结束-->
            </div>
            <p><font size="5">测试：</font><br />&emsp;&emsp;测试内容！<br /><br />&emsp;&emsp;
            &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<a href="https://www.zhouzying.cn">
            志颖博客</a><br />&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;%s</p>
</body>
</html>
""" % (d, h, m, s, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    # &emsp; 一个空白（2个字符宽度）
    # &ensp; 半个空白（1个字符宽度）
    content = script
    theme = '考研倒计时'
    send_mail(content, theme)


if __name__ == '__main__':
    main()
