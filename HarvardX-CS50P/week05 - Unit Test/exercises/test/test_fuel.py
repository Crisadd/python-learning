from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("2/2") == 100
    assert convert("1/2") == 50
    assert convert("2/3") == 67
    with pytest.raises(ValueError):
        convert("-1/2")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"