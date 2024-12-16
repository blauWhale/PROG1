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
shift = 6  # Example shift value
plain_text = "hello world"
encrypted_text = encrypt(plain_text, shift)
decrypted_text = decrypt(encrypted_text, shift)

print("Original message:", plain_text)
print("Encrypted message:", encrypted_text)
print("Decrypted message:", decrypted_text)
