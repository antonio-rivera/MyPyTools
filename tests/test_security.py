from utils import security
import pytest


class TestSecurity:
    @pytest.mark.parametrize("password, expected", [
        ("Pa$$word", False),
        ("1@Pa", False),
        ("ma&vimip1", False),
        ("ASDASD3#", False),
        ("Myname123456", False),
        (";lm4<KMb", True),
        ("mZ^D88]6", True),
        ("Xzi_Y\"=0", True)
    ])
    def test_valid_password(self, password, expected):
        assert security.valid_password(password) == expected

    @pytest.mark.parametrize("text_input, result", [
        ("\" or \"\"=\"", " or "),
        ("; DROP global.users",
         " DROP globalusers"),
        ("; cat /etc/passwd",
         " cat etcpasswd"),
        ("<script location=\"http://attack.com\"> <script/>",
         "script locationhttpattackcom script")
    ])
    def test_sanitize_input(self, text_input, result):
        assert security.sanitize_input(text_input) == result

    @pytest.mark.parametrize("string, maxLen, expected", [
        ("14t34tr13t4134r14t134t134t", len("14t34tr13t4134r314t134t134t"), False),
        ("r"*400, 401, False),
        ("`"*20, 19, True)
    ])
    def test_string_is_too_large(self, string, maxLen, expected):
        assert security.string_is_too_large(string, maxLen) == expected
