#!/usr/bin/env python
# coding: utf-8

# In[1]:


import string  # Importing string module to work with ASCII letters (both lowercase and uppercase)

def encrypt_text(n, m):
    # This function will encrypt the text in the raw_text.txt file using a custom cipher
    def encrypt_char(char):
        if char in string.ascii_lowercase:  # Check if the character is a lowercase letter
            if char <= 'm':  # If the letter is from 'a' to 'm'
                # Shift by (n * m) positions forward, wrap around alphabet with modulo 26
                return chr((ord(char) - ord('a') + (n * m)) % 26 + ord('a'))
            else:
                # Shift by -(n + m) positions backward for letters from 'n' to 'z'
                return chr((ord(char) - ord('a') - (n + m)) % 26 + ord('a'))
        elif char in string.ascii_uppercase:  # If the character is an uppercase letter
            if char <= 'M':  # If the letter is from 'A' to 'M'
                # Shift by -n positions backward for letters in the first half of the alphabet
                return chr((ord(char) - ord('A') - n) % 26 + ord('A'))
            else:
                # Shift by m^2 positions forward for letters from 'N' to 'Z'
                return chr((ord(char) - ord('A') + m ** 2) % 26 + ord('A'))
        else:
            # If the character is neither uppercase nor lowercase, just return it unchanged
            return char

    # Open the raw text file to read the text that needs to be encrypted
    with open('raw_text.txt', 'r') as file:
        raw_text = file.read()

    # Encrypt each character in the raw text using the encrypt_char function
    encrypted_text = ''.join(encrypt_char(char) for char in raw_text)

    # Write the encrypted text to a new file called encrypted_text.txt
    with open('encrypted_text.txt', 'w') as file:
        file.write(encrypted_text)

    print("Encryption complete. Encrypted text written to 'encrypted_text.txt'.")

def decrypt_text(n, m):
    # This function will decrypt the encrypted text in the encrypted_text.txt file
    def decrypt_char(char):
        if char in string.ascii_lowercase:  # If the character is a lowercase letter
            if char <= 'm':  # If the letter is from 'a' to 'm'
                # Shift by -(n * m) positions backward to decrypt
                return chr((ord(char) - ord('a') - (n * m)) % 26 + ord('a'))
            else:
                # Shift by +(n + m) positions forward for letters from 'n' to 'z'
                return chr((ord(char) - ord('a') + (n + m)) % 26 + ord('a'))
        elif char in string.ascii_uppercase:  # If the character is an uppercase letter
            if char <= 'M':  # If the letter is from 'A' to 'M'
                # Shift by +n positions forward to decrypt
                return chr((ord(char) - ord('A') + n) % 26 + ord('A'))
            else:
                # Shift by -m^2 positions backward for letters from 'N' to 'Z'
                return chr((ord(char) - ord('A') - m ** 2) % 26 + ord('A'))
        else:
            # If the character is not a letter, return it unchanged (e.g., spaces, punctuation)
            return char

    # Open the encrypted text file and read the encrypted text
    with open('encrypted_text.txt', 'r') as file:
        encrypted_text = file.read()

    # Decrypt each character in the encrypted text
    decrypted_text = ''.join(decrypt_char(char) for char in encrypted_text)

    print("Decryption complete. Here's the decrypted text:")
    print(decrypted_text)  # Display the decrypted text
    print()
    return decrypted_text

def verify_decryption(n, m):
    # This function compares the original raw text with the decrypted text to verify correctness
    with open('raw_text.txt', 'r') as file:
        original_text = file.read()  # Read the original text from the raw file

    decrypted_text = decrypt_text(n, m)  # Decrypt the text using the given parameters

    # Check if the decrypted text matches the original text
    if original_text == decrypted_text:
        print("Verification successful: The decrypted text matches the original text.")
    else:
        print("Verification failed: The decrypted text does not match the original text.")
        print(f"Original Text: {original_text}")
        print()
        print(f"Decrypted Text: {decrypted_text}")

# Example usage:
# Set some example values for n and m
n = 1  # Shift value for encryption (this could be any integer)
m = 1  # Another shift value (this could also be any integer)

# First, encrypt the text with the given n and m values
encrypt_text(n, m)

# After encryption, check if the decryption process works correctly
verify_decryption(n, m)

