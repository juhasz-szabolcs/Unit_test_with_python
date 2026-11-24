import pytest
from calculator import sum, subtract, multiply, divide

# AAA
def test_sum_AAA():
    number1 = 2
    number2 = 3       # Arrange - bemenő adatok megadása

    result = sum(number1, number2)      # Act - függvény meghívása

    assert result == 5


def test_sum():
    assert sum(2,3) == 5
    assert sum(2,-3) == -1
    assert sum(-2,-3) == -5
    assert sum(0,-3) == -3
    assert sum(0,3) == 3

def test_subtract():
    assert subtract(3,2) == 1
    assert subtract(2,3) == -1
    assert subtract(2,-3) == 5
    assert subtract(-2,-3) == 1
    assert subtract(0,-3) == 3

