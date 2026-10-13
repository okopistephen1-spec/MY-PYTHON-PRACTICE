from find_resource import find_resource
from available_resource_names import available_resource_names

RESOURCES = [
    {"id": "R001", "name": "Laptop", "available": 2},
    {"id": "R002", "name": "Mouse", "available": 0},
    {"id": "R003", "name": "Keyboard", "available": 3},
]

def test_find_resource():
    assert find_resource(RESOURCES, "R002") == RESOURCES[1]
    assert find_resource(RESOURCES, "missing") is None

def test_available_resource_names():
    assert available_resource_names(RESOURCES) == ["Laptop", "Keyboard"]
