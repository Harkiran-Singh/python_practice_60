import random

passwd_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*'


def passwd_generator(len_of_passwd):
    passwd = "".join(random.sample(passwd_str, len_of_passwd))
    print(f"You can use the password {passwd}")


def validate_and_execute(passwd_len):
    try:
        passwd_len = int(passwd_len)
        if passwd_len > 0:
            passwd_generator(passwd_len)
        elif passwd_len == 0:
            print("Please enter a number greater than 0")
        else:
            print("Please enter a positive integer")
    except ValueError:
        print("Please enter a valid value")


def main():
    user_input = ""
    while user_input != "exit":
        user_input = (input("Enter the length of the password you want to generate\n"))
        if user_input == 'exit':
            break
        else:
            validate_and_execute(user_input)


if __name__ == "__main__":
    main()
