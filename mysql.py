import pymysql


def read_quesion():
    """查询所有问题"""
    global curser
    sql = 'select question from QA_list;'
    curser.execute(sql)
    result = [i[0] for i in curser.fetchall()]
    return result


def read_answer(q_id):
    """返回答案"""
    global curser
    sql = 'select answer from QA_list where id = {}'.format(q_id)
    curser.execute(sql)
    return curser.fetchone()[0]


print('正在连接数据库。。。', __name__)
try:
    connection = pymysql.connect('127.0.0.1', 'root', '123456', 'QA', charset='utf8')
except Exception as e:
    print('连接失败！', e)
    curser = None
else:
    curser = connection.cursor()
