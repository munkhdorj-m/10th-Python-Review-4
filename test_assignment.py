import pytest
import inspect
from assignment import count_digits, factorial, primes_up_to, average_of_list


def check_contains_loop(function):
    source = inspect.getsource(function)
    return 'for' in source or 'while' in source


# Exercise 1: Number of digits
@pytest.mark.parametrize("num, expected", [
    (1234, 4),
    (7, 1),
    (0, 1),
    (987654, 6)
])
def test1(num, expected):
    assert count_digits(num) == expected
    assert check_contains_loop(count_digits)


# Exercise 2: Factorial using loop
@pytest.mark.parametrize("n, expected", [
    (5, 120),
    (0, 1),
    (6, 720),
    (1, 1),
    (3, 6)
])
def test2(n, expected):
    assert factorial(n) == expected
    assert check_contains_loop(factorial)


# Exercise 3: Prime numbers up to n (printed)
@pytest.mark.parametrize("n, expected", [
    (10, ["2", "3", "5", "7"]),
    (20, ["2", "3", "5", "7", "11", "13", "17", "19"]),
    (2, ["2"]),
    (1, []),
    (0, [])
])
def test3(capsys, n, expected):
    primes_up_to(n)
    captured = capsys.readouterr()
    output = captured.out.strip().split()
    assert output == expected
    assert check_contains_loop(primes_up_to)

# Exercise 4: Average of list
@pytest.mark.parametrize("lst, expected", [
    ([3, 5, 7], 5.0),
    ([10, 20, 30, 40], 25.0),
    ([1], 1.0),
    ([2, 2, 2, 2], 2.0),
])
def test4(lst, expected):
    assert average_of_list(lst) == expected
    assert check_contains_loop(average_of_list)
