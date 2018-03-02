# encoding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import sys
from datetime import datetime
import json
"""
入门级水平，把以前想的东西整合一下
"""
class ATTACK(object):
    def __init__(self,user,passed,server,server_port):
        '''
        :param user: 用户名
        :param passed:密码
        :param server:服务器
        :param server_port:端口
        '''
        self.user=user
        self.server=smtplib.SMTP_SSL(server,int(server_port))
        #self.server = smtplib.SMTP(server, server_port)
        try:
            #self.server.starttls()
            self.server.login(user,passed)
            pass
        except Exception,e:
            print(e.args)
    def send_email(self,target,msg_data):
        """
        :param target: type:list 多个目标邮箱
        :param message: 邮件内容
        :return:
        """
        try:
            self.server.sendmail(from_addr=self.user,to_addrs=target,msg=msg_data.as_string())
            self.server.quit()
            self.server.close()
        except Exception,e:
            print(e.args)
class PARSER(object):
    def __init__(self,path,url):
        """
        :param path:相对路径
        """
        try:
            with open(path) as f:
                self.msg = MIMEText(f.read().decode('utf-8').replace("{url}",url), "html", "utf-8")
        except Exception,e:
            print(e.args)
    def create_message(self,fromaddress,subject):
        """
        构造发送请求
        :param fromaddress: 伪造来自哪里
        :param subject: 默认主题
        :return:
        """
        self.msg["From"]=Header(fromaddress,"utf-8")
        self.msg["Subject"]=Header(subject,"utf-8")
        return self.msg
def parser():
    server=user=_pass=path=fromaddress=sub=target=url=""
    server_port=0
    argv=sys.argv[1:]
    if len(argv)%2!=0:
        print("error argvs")
        return
    for e in xrange(0,len(argv),2):
        if argv[e]=="-s":server=argv[e+1]
        elif argv[e]=="-p":server_port=argv[e+1]
        elif argv[e]=="-u":user=argv[e+1]
        elif argv[e]=="-pass":_pass=argv[e+1]
        elif argv[e]=="-path":path=argv[e+1]
        elif argv[e] == "-from":fromaddress = argv[e + 1]
        elif argv[e]=="-sub":sub=argv[e+1]
        elif argv[e]=="-target":target=argv[e+1]
        elif argv[e] == "-url":url = argv[e + 1]
    return dict(server=server,server_port=server_port,user=user,_pass=_pass,path=path,fromaddress=fromaddress.decode('gbk'),sub=sub.decode('gbk'),target=target,url=url)
def help():
    print("""
-s SMTP server e.g:stmp.qq.com
-p SMTP server port e.g:465
-u username e.g:admin@qq.com
-pass password e.g:admin
-path html content e.g: ./index.html
-from show who send email e.g:News<news_push@qq.com>
-sub the subject of email e.g:Amazing!Chinses.... 
-target the target emails split by , e.g:XX@admin.com,XXX@admin.com
-url url to replace the {url} in path html e.g:http://xx....
    """)
if __name__ == '__main__':
    help()
    result=parser()
    try:
        with open("./server.json") as f:
            config=json.loads(f.read())
        for i in result.keys():
            if result.get(i)==0 or result.get(i)=="":
                result[i]=config.get(i)
        content=PARSER(result.get("path"),result.get("url"))
        content.create_message(result.get("fromaddress"),result.get("sub"))
        SERVER=ATTACK(user=result.get("user"),passed=result.get("_pass"),server=result.get("server"),server_port=result.get("server_port"))
        SERVER.send_email(target=result.get("target").split(","),msg_data=content.msg)
        print('''You send hack email successfully!''')
    except Exception,e:
        print e.args