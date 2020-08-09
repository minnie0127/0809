from client import *
import pytest


# data = [('正常登录', 'zhangsan', 'MTIzMTIzNDU2', 0),
#         ('密码错误', 'zhangsan', '123456', 10000),
#         ('密码为空', 'zhangsan', '', 10001)]
# @params('desc, username, password, error_code', csv('login'))
# def test_login01(desc, username, password, error_code):
#     client = Client(url='/login/', method=METHOD.POST, body_type=BODY_TYPE.FORM)
#     client.set_body('username', username)
#     client.set_body('password', password)
#     client.send()
#     client.check_status_code_is_200()
#     client.check_json_value('error_code', error_code)

def test_login02(api, set):
    client = api('admin')
    client.set_body('username', 'admin')
    client.set_body('password', 'MTIzYWRtaW4=')
    client.send()
    set('uid', client.json_path_value('uid'))
    set('key', client.json_path_value('token'))
    client.check_status_code_is_200()
    client.check_json_value('error_code', 0)

#
# def test_login03():
#     '''密码为空'''
#     client = Client(url='/login/', method=METHOD.POST, body_type=BODY_TYPE.FORM)
#     client.set_body('username', 'zhangsan')
#     client.set_body('password', '')
#     client.send()
#     client.check_status_code_is_200()
#     client.check_json_value('error_code', 10001)