from borrow_resource import borrow_resource
from summarize_inventory import summarize_inventory

def test_borrow_resource():
    item = {"total": 5, "available": 3}
    assert borrow_resource(item, 2) is True
    assert item["available"] == 1
    assert borrow_resource(item, 2) is False
    assert item["available"] == 1
    assert borrow_resource(item, 0) is False
    assert borrow_resource(item, -1) is False

def test_summarize_inventory():
    resources = [
        {"total": 10, "available": 7},
        {"total": 5, "available": 4},
    ]
    assert summarize_inventory(resources) == {
        "total_units": 15,
        "available_units": 11,
        "borrowed_units": 4,
    }

def test_summarize_empty_inventory():
    assert summarize_inventory([]) == {
        "total_units": 0,
        "available_units": 0,
        "borrowed_units": 0,
    }
