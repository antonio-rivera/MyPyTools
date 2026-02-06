from utils import security


class TestSecurity:
    def test_valid_password(self):
        p1 = "Pa$$word"  # Every condition except number
        p2 = "1@Pa"  # Every condition except length
        p3 = "ma&vimip1"  # Every condition except uppercase
        p4 = "ASDASD3#"  # Every condition except lowercase
        p5 = "Myname123456"  # Every condition except special

        p6 = ";lm4<KMb"
        p7 = "mZ^D88]6"
        p8 = "Xzi_Y\"=0"

        passwords_fail = [p1, p2, p3, p4, p5]
        passwords_pass = [p6, p7, p8]
        for p in passwords_fail:
            assert security.valid_password(p) == False

        for p in passwords_pass:
            assert security.valid_password(p) == True
