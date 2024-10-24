import pytest

@pytest.mark.usefixtures("setUP")
class TestExample:
    def test_fixture_demo(self):
        print("I will run in b/w")

    def test_fixture_demo1(self):
        print("I will run in b/w 1")

    def test_fixture_demo2(self):
        print("I will run in b/w 2")

    def test_fixture_demo3(self):
        print("I will run in b/w 3")

    def test_fixture_demo4(self):
        print("I will run in b/w 4")
