import pytest

@pytest.mark.usefixtures("dataLoad")
class TestExample:
    def test_Login(self, dataLoad):
        print(dataLoad)
        print(dataLoad[1])
        print(dataLoad[2])
