# 音乐播放器运行文件（ 我的是网易云）
music_exe = r'E:\CloudMusic\cloudmusic.exe'

# 本地音乐库，音乐库中没有的 歌曲自动打开百度搜索曲目，
# 也可以自己写爬虫去各大音乐网站下载到本地，然后播放，或者直接返回到前端
music_dir = r'D:\网易云音乐'

# 按照自己电脑的音乐播放器 设置快捷键，键盘映射对照表参照 keyboard.py
# 播放/暂停 快捷键
play_stop = ['alt', 'F5']
# 下一首/ 上一首
next_play = ['alt', 'right_arrow']
former_play = ['alt', 'left_arrow']
# 音量加/ 音量减
volume_up = ['alt','up_arrow']
volume_dowm = ['alt', 'down_arrow']

# 是否用本地音乐播放器 播放
play_local = True

# 截图保存路径，放桌面比较方便
capture_save_path = r'C:\Users\***\Desktop'

# 音频角色，音量，语速调节 参照百度云服务 文档
# https://cloud.baidu.com/doc/SPEECH/TTS-Online-Python-SDK.html#.E5.BF.AB.E9.80.9F.E5.85.A5.E9.97.A8
role_param = {'vol': '10', 'pit': '5', 'per': '3'}

# 文本相似度最低值
sim_degree = 0.6

