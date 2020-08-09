import requests
import jsonpath
import allure
import json
import traceback
import pytest
import csv as CSV



def params(*args, **kwargs):
    data = args[1]
    ids = [i[0] for i in data]
    kwargs['ids'] = ids
    return pytest.mark.parametrize(*args, **kwargs)

def csv(name):
    with open('./data/{name}.csv'.format(name=name), 'r', encoding='utf-8') as f:
        data_list = []
        for d in CSV.reader(f):
            data_list.append(d)
        return data_list

class Client(object):
    base_url = 'http://123.56.99.53:9000/event/api'
    def __init__(self, url, method, body_type=None, timeout=3, params=None):
        self.url = Client.base_url + url
        self.method = method
        if params is None:
            self.params = {}
        else:
            self.params = params
        self.body_type = body_type
        self.timeout = timeout
        self.headers = {}
        self.data = {}
        self.res = None

    def set_header(self, key, value):
        self.headers[key] = value

    def set_headers(self, data):
        if isinstance(data, dict):
            self.headers = data
        else:
            raise Exception('请求头信息请以字典形式传递!')

    def set_param(self, key, value):
        self.params[key] = value

    def set_params(self, data):
        if isinstance(data, dict):
            self.params = data
        else:
            raise Exception('URL参数信息请以字典形式传递!')

    def set_body(self, key, value):
        self.data[key] = value

    def set_bodys(self, data):
        if isinstance(data, dict):
            self.data = data
        else:
            raise Exception('请求正文信息请以字典形式传递!')

    def send(self):
        if self.method == 'GET':
            self.res = requests.get(url=self.url, headers=self.headers,
                                    params=self.params, timeout=self.timeout)
        elif self.method == 'POST':
            if self.body_type == 'form':
                self.set_header('Content-Type', 'application/x-www-form-urlencoded')
                self.res = requests.post(url=self.url, headers=self.headers, params=self.params,
                                    data=self.data, timeout=self.timeout)
            elif self.body_type == 'files':
                self.res = requests.post(url=self.url, headers=self.headers, params=self.params,
                                         files=self.data, timeout=self.timeout)
            elif self.body_type == 'json':
                self.set_header('Content-Type', 'application/json')
                self.res = requests.post(url=self.url, headers=self.headers, params=self.params,
                                    json=self.data, timeout=self.timeout)
            else:
                raise Exception('请求正文格式错误!')


    @property
    def status_code(self):
        if self.res is not None:
            return self.res.status_code
        else:
            print('响应内容为空，状态码获取失败')
            return None

    @property
    def res_times(self):
        if self.res is not None:
            return round(self.res.elapsed.total_seconds()*1000)
        else:
            print('响应内容为空，响应时间获取失败')
            return None

    @property
    def res_text(self):
        if self.res is not None:
            return self.res.text
        else:
            print('响应内容为空，响应内容获取失败')
            return None

    @property
    def res_to_json(self):
        if self.res is not None:
            return self.res.json()
        else:
            print('响应内容为空，响应内容获取失败')
            return None

    @property
    def cookies(self):
        if self.res is not None:
            return self.res.cookies
        else:
            print('响应内容为空，cookies获取失败')
            return None

    def json_path_value(self, path):
        if not path.startswith('$.'):
            path = '$.' + path
        result = jsonpath.jsonpath(self.res_to_json, path)
        if self.res_to_json is not None:
            if result:
                return result[0]
            else:
                print('json字段取值失败: {path}'.format(path=path))
                return None
        else:
            print("响应内容为空，响应内容获取失败")

    def check_status_code_is_200(self):
        assert self.status_code == 200, '响应状态码错误。实际结果【{a}】，预期结果【{b}】'.format(
            a=self.status_code, b=200
        )

    def check_status_code(self, status_code):
        assert self.status_code == status_code, '响应状态码错误。实际结果【{a}】，预期结果【{b}】'.format(
            a=self.status_code, b=status_code
        )

    def check_res_times_less_than(self, times):
        assert self.res_times < times, '响应超时。实际结果【{a} ms】，预期结果【小于 {b} ms】'.format(
            a=self.res_times, b=times
        )

    def check_res_equal(self, b):
        assert self.res_text == b, '响应内容不一致。实际结果【{a}】，预期结果【{b}】'.format(
            a=self.res_text, b=b
        )

    def check_res_contains(self, b):
        assert b in self.res_text, '响应内容未包含关键信息。实际结果【{a}】，关键信息为【{b}】'.format(
            a=self.res_text, b=b
        )

    def check_json_value(self, path, b):
        value = self.json_path_value(path)
        assert str(value) == str(b), '响应json节点检查失败。实际结果【{a}】，预期结果【{b}】， json节点的路径【{path}】'.format(
            a=value, b=b, path=path
        )

class METHOD(object):
    POST = 'POST'
    GET = 'GET'

class BODY_TYPE(object):
    FORM = 'form'
    FILES = 'files'
    JSON = 'json'


