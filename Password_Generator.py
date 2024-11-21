# Task 3: Password Generator
import random


WEAK = 1
MODERATE = 2
STRONG = 3


def main():
    print(f"{20 * '='} Password Generator 🔑 {20 * '='}")
    while True:
        password_length = get_password_length()
        password_generator(password_length)
        next_try = input("Do you want to continue? (Y/N) ").lower()
        if next_try == "y":
            continue
        else:
            break


def get_password_length():
    try:
        password_length = int(input("Enter the password length: "))
        if password_length < 8:
            print("Password length should be at least 8 characters.")
            return get_password_length()
        return password_length
    except ValueError:
        print("Please, Enter an integer value")
        return get_password_length()


def get_password_complexity():
    try:
        complexity_of_password = int(
            input(
                "Enter the complexity of password? (1/2/3)\n1. Weak\n2. Moderate\n3. Strong\n "
            )
        )
        if not complexity_of_password in [WEAK, MODERATE, STRONG]:
            print("Invalid choice")
            return get_password_complexity()
        return complexity_of_password
    except ValueError:
        print("Invalid input")
        return get_password_complexity()


def password_generator(password_length):
    password = ""
    complexity_of_password = get_password_complexity()
    characters_list = [
        {
            WEAK: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
            MODERATE: "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            STRONG: "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_=+[{]}|;:'\",<.>/?",
        }
    ]

    for i in range(password_length):
        for chars in characters_list:
            password += chars[complexity_of_password][
                random.randint(0, len(chars[complexity_of_password]) - 1)
            ]

    print(f"Your password🔐 is : {password}")


if __name__ == "__main__":
    main()
