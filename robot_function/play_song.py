import os
import re
from config.config import *
from config.keyboard import key_input


def play_song(name):
    """ 播放本地乐库下的音乐,遍历文件名，用本地默认播放器播放第一个找到的 mp3文件
    """
    name = re.sub(r'[播放音乐\s]', '', name)

    for i in os.listdir(music_dir):
        if name in i and i.endswith('.mp3'):
            p = os.path.join(music_dir, i)
            print(p)
            os.popen(p)
            print(i)
            return i


def play_function(func_code):
    """快捷键播放/暂停"""
    if func_code == 10:
        key_input(play_stop)
    elif func_code == 11:
        key_input(next_play)
    elif func_code == 12:
        key_input(former_play)
    elif func_code == 13:
        key_input(volume_up)
    elif func_code == 14:
        key_input(volume_dowm)
