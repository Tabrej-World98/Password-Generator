import random
from pass_character import S_Letter, C_Letter, Symbol, number
from art import logo

def get_valid_input(prompt):
    """
    Prompt the user for a valid integer input.

    Args:
        prompt (str): The input prompt message.

    Returns:
        int: The validated integer input from the user.
    """
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number")

def customize_password(small_letters, capital_letters, symbols, digits):
    """
    Generate a customized password based on user specifications.

    Args:
        small_letters (int): The number of small letters in the password.
        capital_letters (int): The number of capital letters in the password.
        symbols (int): The number of symbols in the password.
        digits (int): The number of digits in the password.

    Returns:
        str: The generated customized password.
    """
    password = []

    for _ in range(small_letters):
        password.append(random.choice(S_Letter))
    for _ in range(capital_letters):
        password.append(random.choice(C_Letter))
    for _ in range(symbols):
        password.append(random.choice(Symbol))
    for _ in range(digits):
        password.append(str(random.choice(number)))

    random.shuffle(password)
    return "".join(password)

def password_generator(length):
    """
    Generate a random password of a specified length.

    Args:
        length (int): The length of the password to generate.

    Returns:
        str: The generated password.
    """
    password = []
    for _ in range(length):
        category = random.choice([S_Letter, C_Letter, Symbol, number])
        password.append(str(random.choice(category)))

    random.shuffle(password)
    return "".join(password)

def password_generator_with_category():
    """
    Interact with the user to generate a password, either customized or random.
    Ensures that the generated password has a minimum length of 8 characters.

    Returns:
        list: A list containing the generated password and a customization flag either "Yes", "No", and Auto.
    """
    print(logo)

    while True:
        customize = input("Do you want to customize your password? Y or N: ").lower()
        print()

        if customize == "y":
            while True:
                small_letters = get_valid_input("Enter how many SMALL letters do you want?: ")
                capital_letters = get_valid_input("Enter how many CAPITAL letters doyou want?: ")
                symbols = get_valid_input("Enter how many SPECIAL CHARACTERS do you want?: ")
                digits = get_valid_input("Enter how many DIGITS do you want?: ")

                total_length = small_letters + capital_letters + symbols + digits
                if total_length >= 8:
                    custom_pass = customize_password(small_letters, capital_letters, symbols, digits)
                    print("\nYour customized password: ", custom_pass, "\n")
                    return [custom_pass, "Yes"]
                else:
                    print("Please enter a total length of at least 8 characters.")
                    print()

        elif customize == "n":
            while True:
                length = get_valid_input("Enter the length of the password you want to generate: ")
                if length >= 8:
                    generated_pass = password_generator(length)
                    print("Generated password: ", generated_pass, "\n")
                    return [generated_pass, "No"]
                else:
                    print("Please enter a length of at least 8 characters.")
                    print()
        elif customize == "":
            generated_pass = password_generator(12)
            print("Auto Generated password: ", generated_pass, "\n")
            return [generated_pass, "Auto"]
        else:
            print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
            print()
def main():
    """
    Main function to run the password generator console application.
    """
    should_continue = True
    pass_list = []

    while should_continue:
        pass_list.append(password_generator_with_category())
        result = input("Do you want to continue? Y or N: ").lower()
        if result == "n":
            print("Your Generated Passwords...\n")
            print("|-----------------------------------------------------------------------------|")
            print("| Sr. No. | Password                            | Customize                   |")
            print("|-----------------------------------------------------------------------------|")
            for i, pass_data in enumerate(pass_list, start=1):
                print(f"| {i:<7} | {pass_data[0]:<35} | {pass_data[1]:<27} |")
                print("|-----------------------------------------------------------------------------|")
            print("\nThank you for using PASSWORD GENERATOR KIOSK")
            should_continue = False

if __name__ == "__main__":
    print("Welcome to PASSWORD GENERATOR KIOSK")
    main()
    
