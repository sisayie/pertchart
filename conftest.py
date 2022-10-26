import pytest

@pytest.fixture()
def setup():
        from pertchart import PertChart
        pc = PertChart()
        tasks = pc.getInput('sample_test_cases.json')
        pc.create_pert_chart(pc.calculate_values(tasks))
        return "Sucess"
