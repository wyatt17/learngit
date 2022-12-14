import pytest
import math
# pytest 参数化
@pytest.mark.parametrize(
    "base, exponent, expected",
    [(2, 2, 4),
    (2, 3, 8),
    (1, 9, 1),
    (0, 9, 0)],
    ids=["case1", "case2", "case3", "case4"]
 )
def test_pow(base, exponent, expected):
    assert math.pow(base, exponent) == expected

if __name__ == "__main__":
    pytest.main(["./test_dir/test_parameterize.py"])