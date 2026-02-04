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
