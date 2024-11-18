# P04 – Functions

## 1.2 Caesar cipher
[Link to ceaserCypher.py](./ceaserCypher.py)

```python
# Function to encrypt a message using the Caesar cipher
def encrypt(message, shift):
    encrypted_message = ""
    for char in message.lower():  # Ensure the message is in lowercase
        if char.isalpha():  # Only encrypt alphabetic characters
            # Convert character to its ASCII value, shift it, and ensure it wraps around
            encrypted_char = chr(((ord(char) - 97 + shift) % 26) + 97)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char  # Keep non-alphabetic characters unchanged
    return encrypted_message

# Function to decrypt a message using the Caesar cipher
def decrypt(message, shift):
    decrypted_message = ""
    for char in message.lower():  # Ensure the message is in lowercase
        if char.isalpha():  # Only decrypt alphabetic characters
            # Convert character to its ASCII value, shift it backward, and ensure it wraps around
            decrypted_char = chr(((ord(char) - 97 - shift) % 26) + 97)
            decrypted_message += decrypted_char
        else:
            decrypted_message += char  # Keep non-alphabetic characters unchanged
    return decrypted_message

# Example usage
shift = 3  # Example shift value
plain_text = "hello world"
encrypted_text = encrypt(plain_text, shift)
decrypted_text = decrypt(encrypted_text, shift)

print("Original message:", plain_text)
print("Encrypted message:", encrypted_text)
print("Decrypted message:", decrypted_text)

```

## 2.2 Gender Detection in Text
[Link to genderDetection.py](./genderDetection.py)

```python
import re

# 2.2.1 Function to count first-person singular pronouns
def count_first_person_pronouns(text):
    pronouns = ['i', 'me', 'my']
    # Split text into words and convert to lowercase for case-insensitive matching
    words = re.findall(r'\b\w+\b', text.lower())
    count = sum(1 for word in words if word in pronouns)
    return count

# 2.2.2 Function to compute the number of words in the text
def document_length(text):
    words = re.findall(r'\b\w+\b', text)
    return len(words)

# 2.2.3 Function to compute the average number of words per sentence
def average_words_per_sentence(text):
    sentences = re.split(r'[.!?]', text)  # Split text by sentence-ending punctuation
    sentences = [sentence for sentence in sentences if sentence.strip()]  # Remove empty sentences
    num_words = document_length(text)
    return num_words / len(sentences) if sentences else 0

# 2.2.4 Function to detect gender based on rules
def gender_detection(text):
    pronoun_count = count_first_person_pronouns(text)
    word_count = document_length(text)
    avg_words_per_sentence = average_words_per_sentence(text)

    # Basic rule of thumb for gender detection
    if pronoun_count > 10 or word_count > 150:
        return "female"
    elif avg_words_per_sentence > 20 and word_count < 100:
        return "male"
    else:
        return "unknown"
        
# Example usage
sample_text = """
I think that my experiences have shaped who I am today. My opinions and thoughts are deeply personal.
I believe that every journey starts with a step.
"""

print("Number of first-person singular pronouns:", count_first_person_pronouns(sample_text))
print("Document length (number of words):", document_length(sample_text))
print("Average number of words per sentence:", average_words_per_sentence(sample_text))
print("Gender detection result:", gender_detection(sample_text))


```