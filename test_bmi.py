import bmi as bmi

def test_bmi_normal_weight():
    assert bmi.calculate_bmi(1.73, 60) == 0

def test_bmi_over_weight():
    assert bmi.calculate_bmi(1.73, 100) == 1

def test_bmi_under_weight():
    assert bmi.calculate_bmi(1.73, 40) == -1