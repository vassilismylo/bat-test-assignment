import pytest
from bat_functions import calculate_bat_power, signal_strength


# Task 1: Basic test for calculate_bat_power
def test_calculate_bat_power():
    assert calculate_bat_power(1) == 42
    assert calculate_bat_power(2) == 84
    assert calculate_bat_power(0) == 0
    assert calculate_bat_power(-1) == -42  # Testing negative input


# Task 2: Parametrized test for signal_strength
@pytest.mark.parametrize("distance, expected", [
    (0, 100),  # At source: full strength
    (5, 50),  # 5km away: 50% strength
    (10, 0),  # 10km away: 0% strength
    (12, 0),  # 12km away: still 0% (not negative)
    (-1, 110)  # Negative distance (edge case): 110% strength
])
def test_signal_strength(distance, expected):
    assert signal_strength(distance) == expected
