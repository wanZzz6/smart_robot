import requests
import json
from config.Error import robot_error

api = 'http://openapi.tuling123.com/openapi/api/v2'


def chat_robot(info):
    """返回图灵机器人回答信息,只解析普通对话文本，
    若参考图灵机器人接口实现其他复杂信息查询，请自行设计
    """
    if not info:
        # print('请讲话')
        return "请讲话"

    data = {
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": info
            },
        },
        "userInfo": {
            "apiKey": "223c42bc52c44147a91637355eba211c",
            "userId": "291736"
        }
    }

    result = requests.post(api, data=json.dumps(data))
    result.encoding = result.apparent_encoding

    if result.status_code == 200:
        result = result.json()
        if result['intent']['code'] not in robot_error.keys():
            text = result['results'][0]['values'].get('text')
            return text
        else:
            print(result)
            return robot_error[result['code']]
    else:
        return '网络错误，机器人连接失败！'


if __name__ == '__main__':
    # 与图灵机器人对话
    print(chat_robot('123'))
