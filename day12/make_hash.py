import getpass
import sys

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"])


def main():
    password = getpass.getpass("Password: ")
    if not password:
        sys.exit("Empty password, aborting.")
    if getpass.getpass("Confirm: ") != password:
        sys.exit("Passwords do not match.")
    print(pwd_context.hash(password))


if __name__ == "__main__":
    main()
