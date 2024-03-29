import pytest

@pytest.fixture()
def setup():
        from pertchart.pertchart import PertChart
        pc = PertChart()
        tasks = pc.getInput('tests/input/sample_test_cases.json')
        pc.create_pert_chart(pc.calculate_values(tasks))
        return "Sucess"
