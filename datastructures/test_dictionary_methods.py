import pytest


@pytest.mark.dict
@pytest.mark.parametrize("owner", ("Matt", "Kelly", "Ron"))
def test_expected_owners(owner):
    testdic = {
        "model": "Honda CRV",
        "year": 2010,
        "owner": owner
    }
    assert testdic["owner"] == owner


@pytest.mark.dict
def test_check_deleted_item():
    testdic = {
        "model": "Honda",
        "year": 2008,
        "owner": "Andrew"
    }
    testdic.pop("year")
    assert "year" not in testdic


@pytest.mark.dict
def test_cleared_dict():
    testdic = {
        "model": "Tesla Model X",
        "year": 2018,
        "owner": "Tom"
    }
    testdic.clear()
    assert testdic == {}


@pytest.mark.dict
def test_copied_dict_is_equivalent_initial_dict():
    tesla1 = {
        "model": "Tesla Cybertruck",
        "year": 2020,
        "owner": "John"
    }
    tesla2 = tesla1.copy()
    assert tesla1 == tesla2


@pytest.mark.dict
def test_len_decrease():
    testdic = {
        "bedroom": 14,
        "livingroom": 25,
        "pantry": 3,
        "diningroom": 10
    }
    testdic_len = len(testdic)
    testdic.popitem()
    assert len(testdic) == testdic_len-1
