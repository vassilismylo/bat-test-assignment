import pytest
from bat_functions import calculate_bat_power, signal_strength, get_bat_vehicle, fetch_joker_info

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

# Fixture for bat vehicles
@pytest.fixture
def bat_vehicles():
    return {
        'Batmobile': {'speed': 200, 'armor': 80},
        'Batwing': {'speed': 300, 'armor': 60},
        'Batcycle': {'speed': 150, 'armor': 50}
    }

# Test get_bat_vehicle with known vehicles
def test_get_bat_vehicle_known(bat_vehicles):
    for vehicle_name, specs in bat_vehicles.items():
        result = get_bat_vehicle(vehicle_name)
        assert result == specs
        assert result['speed'] == specs['speed']
        assert result['armor'] == specs['armor']

# Test get_bat_vehicle with unknown vehicle
def test_get_bat_vehicle_unknown():
    with pytest.raises(ValueError, match="Unknown vehicle: Bat-Submarine"):
        get_bat_vehicle("Bat-Submarine")


# Test fetch_joker_info with monkeypatch
def test_fetch_joker_info(monkeypatch):
    """Test fetch_joker_info using monkeypatch to simulate fast response."""
    # Import the module inside the test
    import bat_functions

    # Mock data we want to return
    mock_joker_data = {'mischief_level': 0, 'location': 'captured'}

    # Create a mock function that returns our data without delay
    def mock_fetch_joker_info():
        return mock_joker_data

    # Replace the real function with our mock
    monkeypatch.setattr(bat_functions, 'fetch_joker_info', mock_fetch_joker_info)

    # Call the function from the module
    result = bat_functions.fetch_joker_info()

    # Assert we got our mock data
    assert result == mock_joker_data
    assert result['mischief_level'] == 0
    assert result['location'] == 'captured'

# Alternative approach using pytest-mock
def test_fetch_joker_info_with_mock(mocker):
    """Test fetch_joker_info using pytest-mock for simpler mocking."""
    import bat_functions  # Add this import

    # Define mock data
    mock_joker_data = {'mischief_level': 0, 'location': 'captured'}

    # Create the mock (use the module name in the patch)
    mock = mocker.patch('bat_functions.fetch_joker_info', return_value=mock_joker_data)

    # Call the function from the imported module
    result = bat_functions.fetch_joker_info()  # Change this line

    # Assertions
    assert result == mock_joker_data
    assert mock.called