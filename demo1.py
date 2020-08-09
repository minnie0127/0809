import pytest

def setup_module():
    print("整个.py模块开始前只执行一次")


def teardown_module():
    print("整个.py模块结束后只执行一次")


def setup_function():
    print("每个函数级别用例开始前都执行")


def teardown_function():
    print("每个函数级别用例结束后都执行")


def test_one():
    print("one")


def test_two():
    print("two")


class TestCase():
    def setup_class(self):
        print("整个测试类开始前只执行一次")

    def teardown_class(self):
        print("整个测试类结束后只执行一次")

    def setup_method(self):
        print("类里面每个用例执行前都会执行")

    def teardown_method(self):
        print("类里面每个用例结束后都会执行")

    def setup(self):
        print("=类里面每个用例执行前都会执行")

    def teardown(self):
        print("=类里面每个用例结束后都会执行teardown=")

    def test_three(self):
        print("three")

if __name__ == '__main__':
    pytest.main(["-q", "-s", "-ra", "demo1.py"])


