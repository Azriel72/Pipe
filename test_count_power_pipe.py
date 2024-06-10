import pytest
from count_pipe import counter
from power_pipe import power

# Test cases for the counter function
def test_counter():
    assert counter(5) == [1,2,3,4,5]

def test_counter2():
    assert counter(3) == [1,2,3]

def test_counter3():
    assert counter(1) == [1]

# Test cases for the power function
def test_power():
    assert power(5) == 25

def test_power2():
    assert power(3) == 9

def test_power3():
    assert power(1) == 1

def test_power4():
    assert power(0) == 0

def test_power5():
    assert power(2) == 4

def test_power6():
    assert power(4) == 16

def test_power7():
    assert power(6) == 36
