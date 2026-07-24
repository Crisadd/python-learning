from twttr import shorten
import pytest


def test_twttr():
    assert shorten('HELLO') == "HLL"
    assert shorten('hello') == "hll"
    assert shorten('FRIEND') == "FRND"
    assert shorten('friend') == "frnd"
    