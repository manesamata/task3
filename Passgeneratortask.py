import random
import string

def generate_password(length, complexity):
    if complexity == "weak":
        characters = string.ascii_lowercase
    elif complexity == "medium":
        characters = string.ascii_letters
    elif complexity == "strong":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid complexity level!")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    length = int(input("Enter the desired length of the password: "))
    print("Complexity level:")
    print("1. Weak (only lowercase letters)")
    print("2. Medium (letters)")
    print("3. Strong (letters, digits, and special characters)")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        complexity = "weak"
    elif choice == "2":
        complexity = "medium"
    elif choice == "3":
        complexity = "strong"
    else:
        print("Invalid choice!")
        return

    password = generate_password(length, complexity)
    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()


