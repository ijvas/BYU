from names import make_full_name, extract_family_name, extract_given_name
import pytest


def test_make_full_name():
    assert make_full_name('Marie','Toussaint') == 'Toussaint; Marie'
    assert make_full_name('Olivier','Toussaint') == 'Toussaint; Olivier'
    assert make_full_name('George', 'Washington') == 'Washington; George'
    assert make_full_name('Martha','Washington') == 'Washington; Martha'
    assert make_full_name('Ismael','Vasconcel') == 'Vasconcel; Ismael'



def test_extract_family_name():
    assert extract_family_name('Toussaint; Marie') == 'Toussaint'
    assert extract_family_name('Toussaint; Olivier') == 'Toussaint'
    assert extract_family_name('Washington; George') == 'Washington'
    assert extract_family_name('Washington; Martha') == 'Washington'
    assert extract_family_name('Vasconcel; Ismael') == 'Vasconcel'



def test_extract_given_name():
    assert extract_given_name('Toussaint; Marie') == 'Marie'
    assert extract_given_name('Toussaint; Olivier') == 'Olivier'
    assert extract_given_name('Washington; George') == 'George'
    assert extract_given_name('Washington; Martha') == 'Martha'
    assert extract_given_name('Vasconcel; Ismael') == 'Ismael'



pytest.main(["-v", "--tb=line", "-rN", __file__])