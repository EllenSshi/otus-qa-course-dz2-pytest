import pytest


@pytest.mark.parametrize("input_string, expected_result", [("hello", 5), ("testing", 7), ("course", 6)])
def test_len_of_str(input_string, expected_result):
    assert len(input_string) == expected_result


def test_substring_in_string():
    greeting = "Hi, Jane! Nice to meet you"
    assert "Jane" in greeting


def test_string_is_in_appercase():
    s = "This string should be in uppercase"
    s = s.upper()
    assert s.isupper()


def test_string_without_spaces():
    s = "  This_string_should_be_without_any_whitespaces    "
    s = s.strip()
    assert " " not in s


def test_only_digits_string():
    s = "3567543245"
    assert s.isdigit()
