# P07 – Dictionaries

## Vocabulary Trainer
[Link to voci.py](./voci.py)

```python
import random

def load_dictionary(file_path):
    """Load translations from a file into a dictionary."""
    translations = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) > 1:
                translations[parts[0]] = parts[1:]
    return translations

def quiz_user(translations):
    """Quiz the user until all translations are known."""
    while translations:
        word, answers = random.choice(list(translations.items()))
        user_input = input(f"Translate '{word}' into German: ").strip()
        if user_input in answers:
            print("Correct!")
            del translations[word]
        else:
            print(f"Incorrect. Possible translations: {', '.join(answers)}")

file_path = "dictionary.txt"
translations = load_dictionary(file_path)
print("Welcome to the English-to-German memorization quiz!")
quiz_user(translations)
print("Congratulations! You memorized all the words.")


```

## Phone Book
[Link to phonebook.py](./phonebook.py)

```python
def print_numbers(numbers):
    for name, number in numbers.items():
        print(f"{name}: {number}")


def add_number(numbers, name, number):
    numbers[name] = number
    print(f"Added {name}: {number}")


def lookup_number(numbers, name):
    return numbers.get(name, "Not found")


def remove_number(numbers, name):
    if name in numbers:
        del numbers[name]
        print(f"Removed {name}")
    else:
        print("Name not found")


def load_numbers(numbers, filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, number = line.strip().split(',')
                numbers[name] = number
        print("Phone numbers loaded successfully")
    except FileNotFoundError:
        print("File not found")


def save_numbers(numbers, filename):
    with open(filename, 'w') as file:
        for name, number in numbers.items():
            file.write(f"{name},{number}\n")
    print("Phone numbers saved successfully")


def print_menu():
    print('1. Print Phone Numbers')
    print('2. Add a Phone Number')
    print('3. Remove a Phone Number')
    print('4. Lookup a Phone Number')
    print('5. Load numbers')
    print('6. Save numbers')
    print('7. Quit')
    print()


phone_book = {}
menu_choice = 0
print_menu()
while True:
    try:
        menu_choice = int(input("Type in a number (1-7): "))
        if menu_choice == 1:
            print_numbers(phone_book)
        elif menu_choice == 2:
            name = input("Name: ")
            phone = input("Number: ")
            add_number(phone_book, name, phone)
        elif menu_choice == 3:
            name = input("Name: ")
            remove_number(phone_book, name)
        elif menu_choice == 4:
            name = input("Name: ")
            print(lookup_number(phone_book, name))
        elif menu_choice == 5:
            filename = input("Filename to load: ")
            load_numbers(phone_book, filename)
        elif menu_choice == 6:
            filename = input("Filename to save: ")
            save_numbers(phone_book, filename)
        elif menu_choice == 7:
            break
        else:
            print("Invalid choice, try again.")
            print_menu()
    except ValueError:
        print("Please enter a valid number.")

```