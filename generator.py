import random

def generate_password(length):
    """Generates a random password of the specified length."""
    
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^*()"
    
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    
    return password

def main():
    """The main function of the password generator application."""
    
    length = int(input("How long do you want your password to be? "))
    
    password = generate_password(length)
    print("Your password is:", password)

if __name__ == "__main__":
    main()
