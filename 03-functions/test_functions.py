from calculate_priority import calculate_priority
from count_vowels import count_vowels

def test_calculate_priority():
    assert calculate_priority("high", 10) == "critical"
    assert calculate_priority("HIGH", 2) == "high"
    assert calculate_priority("low", 10) == "high"
    assert calculate_priority("medium", 2) == "medium"
    assert calculate_priority("low", 2) == "low"

def test_count_vowels():
    assert count_vowels("Hello World") == 3
    assert count_vowels("AEIOU") == 5
    assert count_vowels("rhythm") == 0
    assert count_vowels("") == 0
