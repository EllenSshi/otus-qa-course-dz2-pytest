import pytest


@pytest.mark.lst
@pytest.mark.parametrize("itm", ["apple", "pineapple", "watermelon"])
def test_appended_item(itm):
    testlist = ["item1", "item2", "item3", "item4"]
    list_len = len(testlist)
    testlist.append(itm)
    print(testlist)
    assert testlist[-1] == itm


@pytest.mark.lst
def test_copied_list():
    oldlist = ["flowers", "trees", "bushes"]
    newlist = oldlist.copy()
    assert oldlist == newlist


@pytest.mark.lst
def test_extended_list():
    lst1 = ["a1", "a2", "b1", "b2"]
    lst1_len = len(lst1)
    lst2 = ["c1", "c2"]
    lst1.extend(lst2)
    assert lst1[lst1_len] == lst2[0]


@pytest.mark.lst
def test_cleared_list():
    testlist = ["one", "two", "three", "four", "five"]
    testlist.clear()
    assert len(testlist) == 0


@pytest.mark.lst
def test_item_count():
    testlist = ["one", "two", "three", "one"]
    assert testlist.count("one") == 2
