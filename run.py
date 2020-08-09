import pytest
import time
import subprocess
from dingtalkchatbot.chatbot import DingtalkChatbot
import yaml
if __name__ == '__main__':
    tmp = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
    pytest.main(['./cases/', '-s', '--alluredir=./report/json', '--clean-alluredir'])
    subprocess.call('allure generate ./report/json -o ./report/html/' + tmp, shell=True)


    # webhook = 'https://oapi.dingtalk.com/robot/send?access_token=f021392bde0168121fb42b113bd825f60513dd49c525888c38ca3c45e4d4138b'
    # xiaoding = DingtalkChatbot(webhook)
    # xiaoding.send_text(msg='接口测试结果：执行{total}，成功{passed}， 失败{failed}，报告地址:xxxxxx'.format(
    #     total=10, passed=8, failed=2
    # ), is_at_all=False,
    #     at_mobiles=['xxxxxx'])



