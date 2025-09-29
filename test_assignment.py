import pytest
import inspect
from assignment import max_min, list_with_reverse, count_target, index_of_max, squares_list

def check_contains_loop(function):
    source = inspect.getsource(function)
    return 'for' in source or 'while' in source


# Exercise 1: Largest and smallest elements
@pytest.mark.parametrize("lst, expected", [
    ([4, 9, 1, 7], [9, 1]),
    ([10, 5, 20], [20, 5]),
    ([3], [3, 3]),
    ([0, -5, 7, 2], [7, -5])
])
def test1(lst, expected):
    assert max_min(lst) == expected
    assert check_contains_loop(max_min)


# Exercise 2: List followed by its reverse
@pytest.mark.parametrize("lst, expected", [
    ([1, 2, 3], [1, 2, 3, 3, 2, 1]),
    (['a', 'b'], ['a', 'b', 'b', 'a']),
    ([5], [5, 5])
])
def test2(lst, expected):
    assert list_with_reverse(lst) == expected
    assert check_contains_loop(list_with_reverse)


# Exercise 3: Count occurrences of target number
@pytest.mark.parametrize("lst, target, expected", [
    ([1, 2, 2, 3, 4, 2], 2, 3),
    ([5, 5, 5, 5], 5, 4),
    ([10, 20, 30], 40, 0),
    ([1, 1, 2, 1], 1, 3)
])
def test3(lst, target, expected):
    assert count_target(lst, target) == expected
    assert check_contains_loop(count_target)


# Exercise 4: Index of largest element
@pytest.mark.parametrize("lst, expected", [
    ([4, 9, 1, 7], 1),
    ([10, 5, 20, 20], 2),
    ([3], 0),
    ([5, 9, 9, 2], 1)
])
def test4(lst, expected):
    assert index_of_max(lst) == expected
    assert check_contains_loop(index_of_max)


# Exercise 5: Squares of numbers from 1 to n
@pytest.mark.parametrize("n, expected", [
    (5, [1, 4, 9, 16, 25]),
    (3, [1, 4, 9]),
    (1, [1]),
    (0, [])
])
def test5(n, expected):
    assert squares_list(n) == expected
    assert check_contains_loop(squares_list)
