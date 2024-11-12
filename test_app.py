import pytest
from app import add
import os

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(10, 10) == 20