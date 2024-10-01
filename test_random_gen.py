from collections import Counter
from math import isclose

import pytest

from random_gen import RandomGen


def test_correct_initialization():
    random_numbers = [1, 2, 3]
    probabilities = [0.2, 0.5, 0.3]

    gen = RandomGen(random_numbers, probabilities)

    assert gen._random_numbers == random_numbers
    assert isclose(sum(gen._probabilities), 1)
    assert gen._cumulative_prob[-1] == 1


def test_invalid_initialization_length_mismatch():
    random_numbers = [1, 2, 3]
    probabilities = [0.5, 0.5]

    with pytest.raises(ValueError):
        RandomGen(random_numbers, probabilities)


def test_invalid_initialization_negative_probabilities():
    random_numbers = [1, 2, 3]
    probabilities = [-0.1, 0.6, 0.5]

    with pytest.raises(ValueError):
        RandomGen(random_numbers, probabilities)


def test_invalid_initialization_zero_probabilities():
    random_numbers = [1, 2, 3]
    probabilities = [0.0, 0.0, 0.0]

    with pytest.raises(ValueError):
        RandomGen(random_numbers, probabilities)


def test_probabilities_correctly_normalized():
    random_numbers = [1, 2, 3]
    probabilities = [2, 3, 5]

    gen = RandomGen(random_numbers, probabilities)

    assert isclose(sum(gen._probabilities), 1)
    assert gen._cumulative_prob[-1] == 1



def test_next_num_distribution():
    random_numbers = [-1, 0, 1, 2, 3]
    probabilities = [0.01, 0.3, 0.58, 0.1, 0.01]

    number_of_calls = 10_000

    r = RandomGen(random_numbers=random_numbers, probabilities=probabilities)
    result = [r.next_num() for _ in range(number_of_calls)]

    c = dict(Counter(result))

    for k, v in c.items():
        c[k] = v / number_of_calls

    assert isclose(c[-1], 0.01, abs_tol=0.005)
    assert isclose(c[0], 0.3, abs_tol=0.03)
    assert isclose(c[1], 0.58, abs_tol=0.05)
    assert isclose(c[2], 0.1, abs_tol=0.01)
    assert isclose(c[3], 0.01, abs_tol=0.005)
