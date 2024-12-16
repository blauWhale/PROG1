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
