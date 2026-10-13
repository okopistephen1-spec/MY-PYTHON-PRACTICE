import pytest
from grade_from_score import grade_from_score
from sum_positive_numbers import sum_positive_numbers

@pytest.mark.parametrize("score, expected", [(100,"A"),(70,"A"),(69,"B"),(60,"B"),(59,"C"),(50,"C"),(49,"D"),(45,"D"),(44,"F"),(0,"F")])
def test_grade_from_score(score, expected):
    assert grade_from_score(score) == expected

@pytest.mark.parametrize("score", [-1, 101])
def test_grade_invalid_score(score):
    with pytest.raises(ValueError):
        grade_from_score(score)

def test_sum_positive_numbers():
    values = [-3, 0, 2, 4, -1]
    original = values.copy()
    assert sum_positive_numbers(values) == 6
    assert values == original
    assert sum_positive_numbers([]) == 0
