def fizzbuzz(int):
    if int % 3 == 0 and int % 5 != 0:
        return "Fizz"
    elif int % 3 != 0 and int % 5 == 0:
        return "Buzz"
    elif int % 3 == 0 and int % 5 == 0:
        return "FizzBuzz"
    else:
        return int



def test_fizzbuzz1():
    assert fizzbuzz(3) == "Fizz"

def test_fizzbuzz2():
    assert fizzbuzz(5) == "Buzz"

def test_fizzbuzz3():
    assert fizzbuzz(15) == "FizzBuzz"

def test_fizzbuzz4():
    assert fizzbuzz(4) == 4