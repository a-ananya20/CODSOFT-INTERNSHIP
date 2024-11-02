import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    """Generate a random password based on the specified criteria."""
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        print("Error: No character types selected. Please select at least one.")
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    try:
        # Get password length
        length = int(input("Enter the desired password length: "))

        # Get character type preferences
        use_letters = input("Include letters? (yes/no): ").strip().lower() == 'yes'
        use_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
        use_symbols = input("Include symbols? (yes/no): ").strip().lower() == 'yes'

        # Generate password
        password = generate_password(length, use_letters, use_numbers, use_symbols)

        # Display result
        if password:
            print(f"\nGenerated password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
