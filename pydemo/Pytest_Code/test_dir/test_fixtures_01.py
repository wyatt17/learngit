import pytest
def multiply(a, b):
    return a * b

# =====Fixture========
def setup_module(module):
    print("setup_module================>")
def teardown_module(module):
    print("teardown_module=============>")

def setup_function(function):
    print("setup_function------>")
def teardown_function(function):
    print("teardown_function--->")

def setup():
    print("setup-----1111111111>")
def teardown():
    print("teardown--22222222>")

# =====测试用例========
def test_multiply_3_4():
    print('test_numbers_3_4')
    assert multiply(3, 4) == 12

def test_multiply_a_3():
    print('test_strings_a_3')
    assert multiply('a', 3) == 'aaa'

if __name__ == "__main__":
    pytest.main(["./test_dir/test_fixtures_01.py::test_multiply_3_4"])