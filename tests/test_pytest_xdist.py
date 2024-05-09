import pytest
import time

## Initializing 10 tests with 1s intentional delay

def test_with_xdist_01():
    time.sleep(1)
    assert True

def test_with_xdist_02():
    time.sleep(1)
    assert True

def test_with_xdist_03():
    time.sleep(1)
    assert True

def test_with_xdist_04():
    time.sleep(1)
    assert True

def test_with_xdist_05():
    time.sleep(1)
    assert True

def test_with_xdist_06():
    time.sleep(1)
    assert True

def test_with_xdist_07():
    time.sleep(1)
    assert True

def test_with_xdist_08():
    time.sleep(1)
    assert True

def test_with_xdist_09():
    time.sleep(1)
    assert True

def test_with_xdist_10():
    time.sleep(1)
    assert True


