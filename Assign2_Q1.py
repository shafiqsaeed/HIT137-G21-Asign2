# HIT 137 Software Now 

# Assignment 2

# Group: CAS/DAN 21
# Abu Saeed Md Shafiqur Rahman (Shafiq Rahman) - S386795
# Annafi Bin Alam (Rafin Alam) - S387086
# Neville James Doyle (Nev Doyle) - S371207
# Yuvraj Singh (Yuvraj Singh) - S383324

# GitHub Repository: https://github.com/shafiqsaeed/HIT137-G21-Assign2

# Submitted: 17 January 2025


# Question 1 - Simple encryption/ decryption 
# This program encrypts file contents using rules and user shift key input 
# and writes the encrypted text to a new file. It also can decrypt 
# the content and check the correctness of decrypted text.


import string


def display_raw_text(input_file):
    
    # Reads and prints the raw text from the input file to the console.
    
    with open(input_file, 'r') as infile:
        raw_text = infile.read()
    print("Raw Text:")
    print(raw_text)
    return raw_text


def encrypt_text(raw_text, n, m):
    
    # Encrypts the given raw text using the specified n and m values.
    # Prints the encrypted text to the console and returns it.
    
    def encrypt_char(char):
        if char in string.ascii_lowercase:  # Lowercase letters
            if char <= 'm':
                return chr((ord(char) - ord('a') + n * m) % 26 + ord('a'))
            else:
                return chr((ord(char) - ord('a') - (n + m)) % 26 + ord('a'))
        elif char in string.ascii_uppercase:  # Uppercase letters
            if char <= 'M':
                return chr((ord(char) - ord('A') - n) % 26 + ord('A'))
            else:
                return chr((ord(char) - ord('A') + m^2) % 26 + ord('A'))
        else:  # Special characters and numbers
            return char

    encrypted_text = ''.join(encrypt_char(c) for c in raw_text)
    print("\nEncryption complete! Encrypted Text:")
    print(encrypted_text)
    return encrypted_text


def save_to_file(text, output_file):
    
    # Saves the given text to the specified output file.
    
    with open(output_file, 'w') as outfile:
        outfile.write(text)
    print(f"\nThe encrypted text has been saved to {output_file}")


def decrypt_text(encrypted_text, n, m):
    
    # Decrypts the given encrypted text using the reverse logic of the specified n and m values.
    # Prints the decrypted text to the console and returns it.
    
    def decrypt_char(char):
        if char in string.ascii_lowercase:  # Lowercase letters
            if char <= 'm':
                return chr((ord(char) - ord('a') - n * m) % 26 + ord('a'))
            else:
                return chr((ord(char) - ord('a') + (n + m)) % 26 + ord('a'))
        elif char in string.ascii_uppercase:  # Uppercase letters
            if char <= 'M':
                return chr((ord(char) - ord('A') + n) % 26 + ord('A'))
            else:
                return chr((ord(char) - ord('A') - m^2) % 26 + ord('A'))
        else:  # Special characters and numbers
            return char

    decrypted_text = ''.join(decrypt_char(c) for c in encrypted_text)
    print("\nDecryption complete! Decrypted Text:")
    print(decrypted_text)
    return decrypted_text


def check_correctness(raw_text, decrypted_text):
    
    # Compares the raw text and decrypted text to check if they match.
    # Prints the result to the console.
    
    if raw_text == decrypted_text:
        print("\nCorrectness Check: The decrypted text matches the original.")
    else:
        print("\nCorrectness Check: The decrypted text does NOT match the original.")


# Main program
def main():
    raw_file = "raw_text.txt"
    encrypted_file = "encrypted_text.txt"

    # User inputs for n and m
    n = int(input("Enter the value of n: "))
    m = int(input("Enter the value of m: "))

    # Step 1: Display raw text
    raw_text = display_raw_text(raw_file)

    # Step 2: Encrypt the raw text
    encrypted_text = encrypt_text(raw_text, n, m)

    # Step 3: Save the encrypted text to a file
    save_to_file(encrypted_text, encrypted_file)

    # Step 4: Decrypt the encrypted text
    decrypted_text = decrypt_text(encrypted_text, n, m)

    # Step 5: Check the correctness of the decrypted text
    check_correctness(raw_text, decrypted_text)


main()
