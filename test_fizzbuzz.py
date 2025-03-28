def test_pytest():
    assert 2+2 == 4

from fizzbuzz import num_checker

def test_fizz():
    assert num_checker (3) == "Fizz"

def test_buzz():
    assert num_checker (5) == "Buzz"
    assert num_checker (10) == "Buzz"

def test_fizzbuzz():
    assert num_checker (15) == "FizzBuzz"
    assert num_checker (30) == "FizzBuzz"