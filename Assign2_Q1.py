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


def encrypt_text(input_file, output_file, n, m):
    
    # Encrypts the content of the input file and writes to the output file.
    
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
                return chr((ord(char) - ord('A') + m**2) % 26 + ord('A'))
        else:  # Special characters and numbers
            return char

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        raw_text = infile.read()
        encrypted_text = ''.join(encrypt_char(c) for c in raw_text)
        outfile.write(encrypted_text)


def decrypt_text(input_file, output_file, n, m):
    
    # Decrypts the content of the input file and writes to the output file (reverse logic).

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
                return chr((ord(char) - ord('A') - m**2) % 26 + ord('A'))
        else:  # Special characters and numbers
            return char

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        encrypted_text = infile.read()
        decrypted_text = ''.join(decrypt_char(c) for c in encrypted_text)
        outfile.write(decrypted_text)


def check_correctness(original_file, decrypted_file):
    
    # Compares the content of the original file with the decrypted file to check correctness.
    
    with open(original_file, 'r') as orig, open(decrypted_file, 'r') as decrypted:
        original_text = orig.read()
        decrypted_text = decrypted.read()
        return original_text == decrypted_text


# Main program
def main():
    raw_file = "raw_text.txt"
    encrypted_file = "encrypted_text.txt"
    decrypted_file = "decrypted_text.txt"

    # Take user inputs for n and m
    n = int(input("Enter the value of n: "))
    m = int(input("Enter the value of m: "))

    # Encrypt the content of raw_text.txt
    encrypt_text(raw_file, encrypted_file, n, m)
    print(f"Content encrypted and saved to {encrypted_file}")

    # Decrypt the content of encrypted_text.txt
    decrypt_text(encrypted_file, decrypted_file, n, m)
    print(f"Content decrypted and saved to {decrypted_file}")

    # Check correctness of decryption
    if check_correctness(raw_file, decrypted_file):
        print("Decryption is correct. The decrypted text matches the original.")
    else:
        print("Decryption failed. The decrypted text does not match the original.")


main()
