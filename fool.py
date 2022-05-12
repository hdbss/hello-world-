import pytest

@pytest.fixture(scope='function', name='1')
def func():
    print(1)
    yield 2

@pytest.mark.usefixtures('func')
def test_123():
    print(2)

if __name__ == "__main__":
    pytest.main(['-sv'])

