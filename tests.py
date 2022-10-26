import pytest

@pytest.mark.usefixtures("setup")
class TestAbc:
    def test_class(self):
        print("test class 1")

    def test_demo1(self):
        print("test class 2")
