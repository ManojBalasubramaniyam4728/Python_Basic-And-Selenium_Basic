import pytest

@pytest.fixture
def setUP():
    print("I will run first")
    yield
    print("I will run last")

@pytest.fixture(scope="class")
def setUP1():
    print("I will run first")
    yield
    print("I will run last")

@pytest.fixture()
def dataLoad():
    print("The Data from The Data Load")
    return ["Rahul","Shetty","rahulshettyacademy.com"]

@pytest.fixture(params=["chrome","Firefox","Edge"])
def crossBrowser(request):
    return request.param

@pytest.fixture(params=[("chrome","Manoj"),("Firefox","Praveen"),("Edge","Sanjay")])
def crossBrowserDataSet(request):
    return request.param