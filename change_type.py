import os

def anything2pcm(input_file):
    '''将一切格式的音频转为 pcm 格式，需将ffmpeg 添加到环境变量'''
    # input_file = os.path.join(os.getcwd(), input_file)
    output_file = input_file.rsplit('.',1)[0] + '.pcm'
    cmd = 'ffmpeg -y  -i {}  -acodec pcm_s16le -f s16le -ac 1 -ar 16000 {}'.format(input_file, output_file)
    print(os.popen(cmd).read())
    # print('转换完成！')
    return output_file


if __name__ == '__main__':
    # 测试代码，如发现/static/audio_file下有auido.pcm，先删除 然后运行，发现生成 auido.pcm，证明 ffmpeg可用
    input_file = os.path.join('static', 'audio_file','auido.mp3')
    print(input_file)
    print(anything2pcm(input_file))