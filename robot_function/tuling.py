import requests
from config.Error import robot_error

api = 'http://www.tuling123.com/openapi/api'


def chat_robot(info):
    '''返回图灵机器人回答信息'''
    if not info:
        print('请讲话')
        return

    data = {
        'key': '223c42bc52c44147a91637355eba211c',
        'info': info,
        'userid': 291736
    }
    result = requests.post(api, data=data)
    result.encoding = result.apparent_encoding

    if result.status_code < 400:
        result = result.json()
        if result['code'] > 50000:
            result.pop('code')
            text = result.pop('text')
            other_text = '\n'.join([i for i in result.values()])
            return  (text,other_text)
        else:
            return  (robot_error[result['code']])
    else:
        return ('网络错误，机器人连接失败！')
if __name__ == '__main__':

    print(chat_robot('你好'))