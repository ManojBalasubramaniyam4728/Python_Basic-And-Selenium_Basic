import pytest

@pytest.mark.skip # This will allows to skip the execution
def test_Verification():
    message="Hello Hi All"
    assert "Hi" == message, "The String is not matching"

@pytest.mark.Smoke #This will all to group the things
def test_addition():
    a=10
    assert a+10==20, "The Addition is wrong"