import utils.strings as strings
import pytest


class TestStrings:
    @pytest.mark.parametrize("string, expected", [
        (" 2020-08-05 12:12:12 324 ERROR  Program execution - Test",
         "2020-08-05 12:12:12 324 ERROR Program execution - Test"),
        ("      ", ""),
        ("", "")

    ])
    def test_normalize_whitespace(self, string, expected):
        assert strings.normalize_whitespace(string) == expected

    @pytest.mark.parametrize("teststr, length, expected", [
        ("This is my test string for testing truncation.", 6, "This is"),
        ("This is my test string for testing truncation.", 0, ""),
        ("This is my test string for testing truncation.",
         46, "This is my test string for testing truncation.")
    ])
    def test_safe_truncate(self, teststr, length, expected):
        assert strings.safe_truncate(teststr, length) == expected
