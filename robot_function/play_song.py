import os
import re
from config.config import music_dir

def play_song(name):

    '''播放本地乐库下的音乐,遍历文件名，用本地默认播放器播放第一个找到的 mp3文件'''
    name = re.sub('[播放音乐\s]','' ,name)

    for i in os.listdir(music_dir):
        if name in i and i.endswith('.mp3'):
            p = os.path.join(music_dir, i)
            print(p)
            os.popen(p)
            print(i)
            return i
