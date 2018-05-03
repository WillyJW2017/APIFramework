
import smtplib
from email.mime.text import MIMEText

class SendEmail:
    # global send_user
    # global emial_host
    # global password


    def send_email(self, user_list, sub, content):
        # global send_user
        # global email_host
        # global password
        send_user = 'whistler.j@163.com'
        email_host = 'smtp.163.com'
        password = 'JIANG123wei,'
        user = 'Willy<' + send_user +'>'
        message = MIMEText(content, _subtype='plain', _charset='utf-8')
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ';'.join(user_list)

        server = smtplib.SMTP(email_host, port=25)
        # server.connect(email_host)
        server.login(send_user, password)
        server.sendmail(user, user_list, message.as_string())
        server.close()

if __name__ == '__main__':
    sen = SendEmail()
    user_list = ['54800782@qq.com']
    sub = '这个是测试邮件'
    content = '这个是第一封测试邮件'
    sen.send_email(user_list, sub, content)