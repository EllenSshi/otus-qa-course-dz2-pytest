import pytest


@pytest.mark.set
@pytest.mark.parametrize("newitem", ["swimming", "knitting", "snowboarding"])
def test_check_item_in_set(newitem):
    testset = {"reading", "dancing", "skiing"}
    testset.add(newitem)
    assert newitem in testset


@pytest.mark.set
def test_updated_set():
    testset = {"reading", "dancing", "skiing"}
    lst = ["swimming", "knitting", "snowboarding"]
    testset.update(lst)
    assert lst[1] in testset


@pytest.mark.set
def test_cleared_set():
    testset = {"reading", "dancing", "skiing"}
    testset.clear()
    assert len(testset) == 0


@pytest.mark.set
def test_difference_update_method():
    testset1 = {"reading", "dancing", "skiing"}
    testset2 = {"reading", "swimming", "skiing"}
    testset1.difference_update(testset2)
    assert "reading" not in testset1


@pytest.mark.set
def test_sets_union():
    testset1 = {"reading", "dancing", "skiing"}
    testset2 = {"swimming", "knitting", "snowboarding"}
    testset3 = testset1.union(testset2)
    assert testset2.issubset(testset3)
