import pytest

from Demo import add, divide

def test_add_pass():
    result = add(10, 13)
    assert result == 23 

def test_add_pass():
    result = divide(4, 2) 
    assert result == 2 

