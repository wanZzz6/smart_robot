# smart_robot
利用百度语音服务和图灵机器人，以及自定义的一系列功能，实现了一个语音助手，可以与其对话、屏幕截图、播放音乐、百度搜索、打开指定软件等功能

## 使用步骤
### 【注】只限Windows用户，python 版本 3.5 及以上
---
#### 1. 导入QA_list.sql数据文件，修改mysql.py文件中数据库的连接参数（地址、用户名、密码、数据库名）

#### 2. 解压ffmpe-win64-shared.zip ，将 其里面的bin 目录添加环境变量

#### 3. 修改 config/config.py 文件（看注释）

#### 4. 以flask方式运行目标文件 main.py

#### 5. 打开浏览器，访问localhost:5000（如有异常请尝试 127.0.0.1:5000)

#### 6. 点击按钮说话，说完后，再点击按钮结束，等待机器人回应
---
##  对话内容示例：

#### - 你叫什么名字
#### - 你会干什么
#### - 百度搜索图灵 （任意关键字都可）
#### - 播放音乐眉间雪
#### - 屏幕截图（大概一秒钟后，截图整个屏幕，到配置的文件夹）
#### - 我要敲代码（默认打开sublime Text，前提将该编辑器添加到环境变量）
#### - 打开记事本
#### - 成语接龙
#### - 天气
---
## 有问题请联系：QQ & 邮箱 1343837706@qq.com
### API参考
#### - [百度语音识别](https://cloud.baidu.com/doc/SPEECH/ASR-Online-Python-SDK.html#.E8.AF.B7.E6.B1.82.E8.AF.B4.E6.98.8E)
#### - [百度语音合成](https://cloud.baidu.com/doc/SPEECH/TTS-Online-Python-SDK.html#.E6.8E.A5.E5.8F.A3.E8.AF.B4.E6.98.8E)
#### - [图灵机器人](https://www.kancloud.cn/turing/www-tuling123-com/718227)
