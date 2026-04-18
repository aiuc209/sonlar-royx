import pytest
import numpy as np

def replace_with_std_dev(numbers):
    result = []
    for num in numbers:
        digits = [int(d) for d in str(num)]
        std_dev = np.std(digits)
        result.append(round(std_dev))
    return result

def test_replace_with_std_dev():
    numbers = [123, 456, 789]
    expected = [0, 0, 0]
    assert replace_with_std_dev(numbers) == expected

def test_replace_with_std_dev_single_digit():
    numbers = [5, 5, 5]
    expected = [0, 0, 0]
    assert replace_with_std_dev(numbers) == expected

def test_replace_with_std_dev_zero():
    numbers = [0, 0, 0]
    expected = [0, 0, 0]
    assert replace_with_std_dev(numbers) == expected

def test_replace_with_std_dev_negative():
    numbers = [-1, -2, -3]
    expected = [0, 0, 0]
    assert replace_with_std_dev(numbers) == expected

def test_replace_with_std_dev_empty():
    numbers = []
    expected = []
    assert replace_with_std_dev(numbers) == expected
