from aip import AipNlp
from aip import AipSpeech
from config.Error import *
from change_type import anything2pcm
import time
import os
from robot_function.sc_capture import capture
from robot_function.broswer_search import search_kw
from robot_function.play_song import play_song
from config.config import music_exe, role_param


class BaiduApi(object):

    def __init__(self):
        """初始化百度云接口"""
        APP_ID = '11520791'
        APP_KEY = '2r2x4GG1xAlo48DzthXE1uEF'
        SECRET_KEY = 'WugQB8976d94RuoU6jWoVcO618Tq8si5 '

        self.speech_client = AipSpeech(APP_ID, APP_KEY, SECRET_KEY)
        self.nlp_client = AipNlp(APP_ID, APP_KEY, SECRET_KEY)

    def get_file_content(self, file_path):
        """读取二进制文件"""
        with open(file_path, 'rb') as fp:
            return fp.read()

    def text2audio(self, words, lang='zh'):
        """语音合成"""
        result = self.speech_client.synthesis(words, lang, 1, role_param)
        # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
        if not isinstance(result, dict):
            file_name = os.path.join('static', 'audio_file', '{}.mp3'.format(int(time.time()*1000)))
            with open(file_name, 'wb') as f:
                f.write(result)
                print('已合成音频！', file_name)
                # 合成完，返回mp3文件名，linux上 可能要修改 斜杠方向
                return file_name.rsplit('\\', 1)[-1]
            # 否则返回错误信息
        return self.text2audio('Sorry!' + mix_error[result['err_no']])

    def audio2text(self, audio_file):
        """百度语音识别接口
        https://cloud.baidu.com/doc/SPEECH/ASR-Online-Python-SDK.html#.E6.96.B0.E5.BB.BAAipSpeech"""

        # if not audio_file.endswith('.pcm'):
        #     anthing2pcm(audio_file, '/static/audio_file/audio.pcm')
        # 格式转换
        audio_file = anything2pcm(audio_file)

        print('正在识别。。。')
        result = self.speech_client.asr(
            self.get_file_content(audio_file), 'pcm', 16000, {
                'dev_pid': 1536,
            })
        if result['err_no'] == 0:
            # 返回音频内的文本
            return ' '.join(result['result'])

        return 'Sorry！' + recog_error.get(result['err_no'])

    def nlp_simnet(self, doc_index, key_world='百度'):
        if doc_index == 0:
            return '马冬梅'
        elif doc_index == 1:
            return '我今年两万五千岁'
        elif doc_index == 2:
            return '我喜欢程序员小哥哥！'
        elif doc_index == 3:
            return '我会说英文，sorry,the number you dailed is busy now \
            The subscriber you dialed is busy now. Please redial later'
        elif doc_index == 4:
            # 等待一秒调整截图屏幕，转到要截图的界面
            time.sleep(1)
            capture()
            return '截图完成'
        elif doc_index == 5:
            os.system(music_exe)  # 网易云运行路径
            return '好的'
        elif doc_index == 6:
            os.system('subl')  # 打开 shublime Text 前提是，安装目录添加到换件变量
            return '好的'
        elif doc_index == 7:
            search_kw(key_world)
            return '好的'
        elif doc_index == 8:
            song_name = play_song(key_world)
            if song_name:
                return '好的', song_name
            else:
                return search_kw(key_world)
        elif doc_index == 9:
            os.system('notepad')
        else:
            return '没有回答'


baidu_API = BaiduApi()

if __name__ == '__main__':
    bd = BaiduApi()
    bd.text2audio('欢迎使用！')
