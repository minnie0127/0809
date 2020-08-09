from client import *

def test_geteventlist01(get):
    '''无查询条件'''
    client = Client(url='/get_eventlist/', method=METHOD.GET)
    client.set_header('uid', get('uid'))
    client.set_header('key', get('key'))
    client.send()
    client.check_status_code_is_200()
    client.check_json_value('error_code', 0)

def test_geteventlist02(get):
    '''按照分类检索'''
    client = Client(url='/get_eventlist/', method=METHOD.GET)
    client.set_header('uid', get('uid'))
    client.set_header('key', get('key'))
    client.set_param('type', '互联网技术')
    client.send()
    client.check_status_code_is_200()
    client.check_json_value('error_code', 0)
