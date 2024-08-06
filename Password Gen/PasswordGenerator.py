import random
import string
import time
import os

def generate_password(length, strength):
    """Generates a password with specified length and strength."""
    if strength == "weak":
        characters = string.ascii_lowercase
    elif strength == "strong":
        characters = string.ascii_letters + string.digits
    elif strength == "super strong":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Invalid strength choice")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

ascii_art = r"""
________                                __        __                      __                  __        __           
/        |                              /  |      /  |                    /  |                /  |      /  |          
$$$$$$$$/  _______    ______    _______ $$ |____  $$ |  ______    ______  $$ |____    ______  $$ |____  $$/   ______  
$$ |__    /       \  /      \  /       |$$      \ $$ | /      \  /      \ $$      \  /      \ $$      \ /  | /      \ 
$$    |   $$$$$$$  |/$$$$$$  |/$$$$$$$/ $$$$$$$  |$$ |/$$$$$$  |/$$$$$$  |$$$$$$$  |/$$$$$$  |$$$$$$$  |$$ | $$$$$$  |
$$$$$/    $$ |  $$ |$$ |  $$ |$$ |      $$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ | /    $$ |
$$ |_____ $$ |  $$ |$$ \__$$ |$$ \_____ $$ |  $$ |$$ |$$ \__$$ |$$ |__$$ |$$ |  $$ |$$ \__$$ |$$ |__$$ |$$ |/$$$$$$$ |
$$       |$$ |  $$ |$$    $$/ $$       |$$ |  $$ |$$ |$$    $$/ $$    $$/ $$ |  $$ |$$    $$/ $$    $$/ $$ |$$    $$ |
$$$$$$$$/ $$/   $$/  $$$$$$/   $$$$$$$/ $$/   $$/ $$/  $$$$$$/  $$$$$$$/  $$/   $$/  $$$$$$/  $$$$$$$/  $$/  $$$$$$$/ 
                                                                $$ |                                                  
                                                                $$ |                                                  
                                                                $$/                                                   
"""

while True:
    print(ascii_art)
    print("Choose a strength:")
    print("1. Weak")
    print("2. Strong")
    print("3. Super Strong")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice in ['1', '2', '3']:
        try:
            length = int(input("Enter desired password length (minimum 8): "))
            if length < 8:
                raise ValueError("Password length must be at least 8 characters.")

            if choice == '1':
                password = generate_password(length, "weak")
            elif choice == '2':
                password = generate_password(length, "strong")
            else:
                password = generate_password(length, "super strong")

            print("\nYour generated password is:", password)
            with open("generated_passwords.txt", "a") as f:
                f.write(password + "\n")

        except ValueError as e:
            print(f"Error: {e}")

    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
        continue

    time.sleep(3)
    clear_screen()
