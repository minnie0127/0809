import pytest

@pytest.fixture(scope='module')
def A():
    print('模块开始运行')

@pytest.fixture(scope='function')
def B():
    print('打开浏览器')
    yield 'haha'
    print('关闭浏览器')

# @pytest.fixture(scope='function')
# def C():
#     print('方法开始运行C')

def test_one(A,B):
    print("one")
    print(B)


def test_two(A,B):
    print("two")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "-ra", "demo2.py"])

