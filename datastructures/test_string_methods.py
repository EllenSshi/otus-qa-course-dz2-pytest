import pytest


@pytest.mark.str
@pytest.mark.parametrize("input_string, expected_result",
                         [("hello", 5), ("testing", 7), ("course", 6)])
def test_len_of_str(input_string, expected_result):
    assert len(input_string) == expected_result


@pytest.mark.str
def test_substring_in_string():
    greeting = "Hi, Jane! Nice to meet you"
    assert "Jane" in greeting


@pytest.mark.str
def test_string_is_in_appercase():
    teststr = "This string should be in uppercase"
    teststr = teststr.upper()
    assert teststr.isupper()


@pytest.mark.str
def test_string_without_spaces():
    teststr = "  This_string_should_be_without_any_whitespaces    "
    teststr = teststr.strip()
    assert " " not in teststr


@pytest.mark.str
def test_only_digits_string():
    teststr = "3567543245"
    assert teststr.isdigit()
