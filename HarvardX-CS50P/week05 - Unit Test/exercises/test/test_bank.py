from bank import value
import pytest

def test_bank():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("hi") == 20
    assert value("can i help you?") == 100

     