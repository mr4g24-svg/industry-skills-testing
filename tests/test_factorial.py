import pytest
import math
from mymath.factorial import factorial

def test_3():
    assert factorial(3) == 6

def test_5():
    assert factorial(5) == 120

def test_0():
    assert factorial(0) == math.factorial(0)

def test_1():
    assert factorial(1) == 1

def test_42():
    assert factorial(42) == math.factorial(42)

def test_negative1():
    pytest.raises(ValueError, factorial, -1)