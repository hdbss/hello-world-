import pytest

@pytest.fixture(scope='function', name='1')
def func():
    print(1)
    yield 2

@pytest.mark.usefixtures('1')
def test_123():
    print(223)

def opo():
    return 123211

if __name__ == "__main__":
    pytest.main(['-s'])


