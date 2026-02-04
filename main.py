from utils import strings


def main():
    normal = strings.normalize_whitespace(
        " 2020-08-05 12:12:12 324 ERROR  Program execution - Test")
    print(normal)


if __name__ == "__main__":
    main()
