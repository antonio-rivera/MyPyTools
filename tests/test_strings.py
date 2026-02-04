import re
import utils.strings as strings


class TestStrings:
    def test_normalize_whitespace(self):
        teststr1 = " 2020-08-05 12:12:12 324 ERROR  Program execution - Test"
        match = re.search(r"\s{2,}", teststr1)
        assert match is not None

        r1 = strings.normalize_whitespace(teststr1)
        match = re.search(r"\s{2,}", r1)
        assert match == None

        teststr2 = "      "
        r2 = strings.normalize_whitespace(teststr2)
        assert r2 == ""

        r3 = strings.normalize_whitespace("")
        assert r3 == ""

    def test_safe_truncate(self):
        teststr = "This is my test string for testing truncation."
        r1 = strings.safe_truncate(teststr, 6)
        assert r1 == "This is"

        r2 = strings.safe_truncate(teststr, 0)
        assert r2 == ""

        r3 = strings.safe_truncate(teststr, len(teststr))
        assert r3 == teststr
