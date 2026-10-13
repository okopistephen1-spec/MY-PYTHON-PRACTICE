import pytest
from greet import greet
from rectangle_area import rectangle_area

def test_greet():
    assert greet("Ada") == "Hello, Ada!"
    assert greet("Stephen") == "Hello, Stephen!"

def test_rectangle_area():
    assert rectangle_area(3, 4) == 12
    assert rectangle_area(2.5, 4) == 10.0
