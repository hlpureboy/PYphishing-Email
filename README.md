# PYphishing-Email

### 基本介绍
+ 环境：Linux Windows 
+ 语言：Python2.7
### 使用说明
+ 命令行形式（不推荐），可能会产生编码问题
    -s SMTP server e.g:stmp.qq.com

    -p SMTP server port e.g:465

    -u username e.g:admin@qq.com

    -pass password e.g:admin

    -path html content e.g: ./index.html

    -from show who send email e.g:News<news_push@qq.com>

    -sub the subject of email e.g:Amazing!Chinses.... 

    -target the target emails split by , e.g:XX@admin.com,XXX@admin.com

    -url url to replace the {url} in path html e.g:http:xx....

+ server.json形式推荐使用

  {
  "server":"smtp.exmail.qq.com",

  "server_port":465,

  "user":"",

  "_pass":"",

  "path":"./index.html",

  "sub":"test",

  "target":"",

  "url":"http://www.baidu.com",

  "fromaddress":""
  }
+ 相关重要参数解释

  target：可以配置多个邮箱，用逗号分开

  path：邮件按html格式，path指存放html文档的相对路径

  url：html中的{url}替换

  在框架中默认采用SSL，请按需修改第20或21行
### 注意问题
+ 命令行形式可能会出现编码问题，请自行修改第76行
+ 命令参数不完整时，将会从server.json文件中补充完整
### 使用实例
+  ![server.json](pic\server.json.jpg)
+  ![command](pic\command.png)
