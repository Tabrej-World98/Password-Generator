
# Password Generator Kiosk

Welcome to the Password Generator Kiosk! This project allows users to generate secure passwords either by specifying the desired components (small letters, capital letters, symbols, and digits) or by generating a random password of a specified length.

## Table of Contents

- [Project Overview](#project-overview)
- [Project Team](#project-team)
- [Project Technologies](#project-technologies)
- [Project Setup](#project-setup)
- [Project Resources/References](#project-resourcesreferences)
- [Project Risks](#project-risks)
- [Usage](#usage)
- [License](#license)

## Project Overview

The Password Generator Kiosk is a console application that helps users generate secure passwords. Users can choose to customize their password by specifying the number of small letters, capital letters, symbols, and digits, or they can generate a random password of a specified length. The application ensures that generated passwords have a minimum length of 8 characters for security purposes.

## Project Team

- [Tabrej rain]

## Project Technologies

- Python 3.x
- `random` module
- Custom modules: `pass_character`, `art`

## Project Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/password-generator-kiosk.git
    cd password-generator-kiosk
    ```

2. **Ensure Python is installed:**
    - This project requires Python 3.x. You can download it from [python.org](https://www.python.org/).

3. **Run the application:**
    ```bash
    python password_generator.py
    ```

## Project Resources/References

- **Human Resources:** Individual contributors or a development team.
- **Materials:** Python 3.x, any IDE or text editor.
- **Tools:** Git for version control.
- **Links:**
    - [Python Documentation](https://docs.python.org/3/)
    - [Random Module Documentation](https://docs.python.org/3/library/random.html)
    - [Run on Replit](https://replit.com/@HeloTabMu13/Password-generator){:target="_blank"}
        You can directly run this program on Replit by forking it.

## Project Risks

- **User Input Validation:** Ensuring the user inputs valid integers for password customization.
    - *Mitigation Strategy:* Implementing try-except blocks to handle invalid inputs.
- **Security Risks:** Ensuring the generated passwords are secure and not predictable.
    - *Mitigation Strategy:* Using the `random.shuffle` method to randomize the order of characters.

## Usage

1. Run the application.
2. Choose whether to customize the password by specifying "Y" or "N".
3. If customizing, enter the desired number of small letters, capital letters, symbols, and digits.
4. If not customizing, enter the desired password length.
5. The generated password will be displayed.
6. Choose whether to generate another password by specifying "Y" or "N".

### Example

```bash
Welcome to PASSWORD GENERATOR KIOSK

 ____                                     _
|  _ \ __ _ ___ _____      _____  _ __ __| |
| |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` |
|  __/ (_| \__ \__ \ V  V / (_) | | | (_| |
|_|___\__,_|___/___/ \_/\_/ \___/|_|  \__,_|
 / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __
| |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
| |_| |  __/ | | |  __/ | | (_| | || (_) | |
 \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|


Do you want to customize your password? Y or N: y

Enter how many SMALL letters do you want?: 6
Enter how many CAPITAL letters doyou want?: 3
Enter how many SPECIAL CHARACTERS do you want?: 2
Enter how many DIGITS do you want?: 5

Your customized password:  {svnK93zJ0;gUc07

Do you want to continue? Y or N: y

 ____                                     _
|  _ \ __ _ ___ _____      _____  _ __ __| |
| |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` |
|  __/ (_| \__ \__ \ V  V / (_) | | | (_| |
|_|___\__,_|___/___/ \_/\_/ \___/|_|  \__,_|
 / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __
| |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
| |_| |  __/ | | |  __/ | | (_| | || (_) | |
 \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|


Do you want to customize your password? Y or N: N

Enter the length of the password you want to generate: 15
Generated password:  jJp<k2FZjxT5yx_

Do you want to continue? Y or N: Y

 ____                                     _
|  _ \ __ _ ___ _____      _____  _ __ __| |
| |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` |
|  __/ (_| \__ \__ \ V  V / (_) | | | (_| |
|_|___\__,_|___/___/ \_/\_/ \___/|_|  \__,_|
 / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __
| |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
| |_| |  __/ | | |  __/ | | (_| | || (_) | |
 \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|


Do you want to customize your password? Y or N:

Auto Generated password:  2]hcME_Y,^"6

Do you want to continue? Y or N: n
Your Generated Passwords...

|-----------------------------------------------------------------------------|
| Sr. No. | Password                            | Customize                   |
|-----------------------------------------------------------------------------|
| 1       | {svnK93zJ0;gUc07                    | Yes                         |
|-----------------------------------------------------------------------------|
| 2       | jJp<k2FZjxT5yx_                     | No                          |
|-----------------------------------------------------------------------------|
| 3       | 2]hcME_Y,^"6                        | Auto                        |
|-----------------------------------------------------------------------------|

Thank you for using PASSWORD GENERATOR KIOSK
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
