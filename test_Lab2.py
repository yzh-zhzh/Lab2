from Lab2 import find_min_max, calc_average, calc_median_temperature

# Test cases for find_min_max
def test_find_min_max():
    assert find_min_max([1.0, 2.5, 3.6, 0.5]) == (0.5, 3.6)
    assert find_min_max([]) == (0, 0)
    assert find_min_max([7.7]) == (7.7, 7.7)

# Test cases for calc_average
def test_calc_average():
    assert calc_average([2.0, 4.0, 6.0]) == 4.0
    assert calc_average([]) == 0

# Test cases for calc_median_temperature
def test_calc_median_temperature():
    assert calc_median_temperature([1.0, 3.0, 2.0]) == 2.0
    assert calc_median_temperature([1.0, 2.0, 3.0, 4.0]) == 2.5
    assert calc_median_temperature([5.0, 10.0, 15.0]) == 10.0