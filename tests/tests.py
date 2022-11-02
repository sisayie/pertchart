import pytest

@pytest.mark.usefixtures("setup")
class TestAbc:
    def test_class1(self):
        print("test class 1")

    def test_class2(self):
        print("test class 2")
