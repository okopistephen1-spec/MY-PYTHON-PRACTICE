from safe_divide import safe_divide
from normalize_search import normalize_search

def test_safe_divide():
    assert safe_divide(10, 2) == 5
    assert safe_divide(5, 0) is None

def test_normalize_search():
    assert normalize_search("  HeLLo  ") == "hello"
    assert normalize_search(None) == ""
    assert normalize_search("   ") == ""
