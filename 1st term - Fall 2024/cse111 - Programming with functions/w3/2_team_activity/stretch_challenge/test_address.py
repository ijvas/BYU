import pytest
from address import extract_city, extract_state, extract_zipcode



def test_extract_city():
    assert extract_city('525 S Center St, Rexburg, ID 83460') == 'Rexburg'



def test_extract_state():
    assert extract_state('525 S Center St, Rexburg, ID 83460') == 'ID'






pytest.main(["-v", "--tb=line", "-rN", __file__])
