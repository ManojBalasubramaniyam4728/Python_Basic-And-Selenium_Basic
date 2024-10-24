#Any Pytest file should start with test_ or ends with _test
#Pytest methods name should start with test_
#Any code should be wrapped in method only
import pytest


def test_firstProgram():
    print("Hello")

@pytest.mark.Smoke #This will all to group the things
def test_great():
    print("Good Mornind")


@pytest.mark.xfail # this will run but it will not be logged or reported
def test_creditCardAPI():
    print("Credit Card API")
    print("Credit Card API")

def test_creditCardUI():
    print("credit card Ui")