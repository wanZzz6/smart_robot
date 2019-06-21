import datetime

from flask import Blueprint
from flask import request
from flask import jsonify
from Lsi_gensim import get_high_sim, index
from robot_function.tuling import chat_robot
from baidu_ai import baidu_API
import time

au_bp = Blueprint("a", __name__, static_folder='saudio_template')


@au_bp.route("/upload_audio", methods=["GET", "POST"])  # 上传音频文件(非PCM格式)
def upload():
    file_info = request.values.to_dict()
    # print(file_info)
    file_name = file_info["name"]  # 前端获取文件名
    user_id = file_info["user_id"]  # 前端获取User_id

    audio_file = request.files["file"]  # 历史录音文件
    # print(audio_file)
    audio_name = "static/audio_file/%s" % (file_name)
    audio_file.save(audio_name)

    # 进行语音识别
    audio_text = baidu_API.audio2text(audio_name)
    print('识别结果：', audio_text)
    other_info = ''

    if not audio_text.startswith('Sorry'):
        with open('../static/history.txt', 'a+', encoding='utf-8') as f:
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            f.write(timestamp+' 我>>>'+audio_text+'\n')
        doc_index = get_high_sim(audio_text, index)
        # print(doc_index,'-----------')
        if doc_index is not None:
            if doc_index == 9:
                try:
                    # 获取 歌曲名
                    keyword = audio_text[audio_text.rfind('播放') + 2:]
                    print('播放', keyword)
                    answer, other_info = baidu_API.nlp_simnet(doc_index, keyword)
                except Exception as e:
                    print(e)
                    answer = '播放失败'
            elif doc_index == 7:
                try:
                    keyword = audio_text[audio_text.rfind('搜索') + 2:]
                    answer = baidu_API.nlp_simnet(doc_index, keyword)
                except Exception as e:
                    print(e)
                    answer = '搜索失败'
            else:
                answer = baidu_API.nlp_simnet(doc_index)
        else:
            answer = chat_robot(audio_text)
            with open('../static/history.txt', 'a+', encoding='utf-8') as f:
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                f.write(timestamp + ' 机器人>>>' + audio_text + '\n')
            print('机器人回答:', answer)
    else:
        answer = audio_text
    play_audio = baidu_API.text2audio(answer)
    # print('--------------------',play_audio.rsplit('\\',1)[-1])
    if other_info:
        answer = other_info
    # 返回信息
    ret_str = {
        "play_type": "talk",
        "res_name": play_audio,  # 被播放的文件名
        "content1": audio_text,
        "content2": answer
    }

    return jsonify(ret_str)
