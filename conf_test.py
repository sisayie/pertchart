import pytest

@pytest.fixture()
def setup():
    from pertchart import PertChart
    pc = PertChart()
    return pc
