import string
from random import randrange


def encrypt_char(char, key):
    """
    Encrypts a single character using Caesar cipher.

    :param char: The character to encrypt.
    :param key: The shift key for encryption.
    :returns: Encrypted character.
    """
    lower_char = string.ascii_lowercase
    upper_char = string.ascii_uppercase
    if char in lower_char:
        char_index = lower_char.index(char)
        return lower_char[(char_index + key) % 26]
    elif char in upper_char:
        char_index = upper_char.index(char)
        return upper_char[(char_index + key) % 26]
    return char


def decrypt_char(char, key):
    """
    Decrypts a single character using Caesar cipher.

    :param char: The character to decrypt.
    :param key: The shift key for decryption.
    :returns: Decrypted character.
    """
    lower_char = string.ascii_lowercase
    upper_char = string.ascii_uppercase
    if char in lower_char:
        char_index = lower_char.index(char)
        return lower_char[(char_index - key) % 26]
    elif char in upper_char:
        char_index = upper_char.index(char)
        return upper_char[(char_index - key) % 26]
    return char


def encrypt_caesar(text, key):
    """
    Encrypts a string using Caesar cipher.

    :param text: The text to encrypt.
    :param key: The shift key for encryption.
    :returns: Encrypted string.
    """
    caesar_text = ""
    for char in text:
        caesar_text += encrypt_char(char, key)
    return caesar_text


def decrypt_caesar(ciphertext, key):
    """
    Decrypts a string using Caesar cipher.

    :param ciphertext: The text to decrypt.
    :param key: The shift key for decryption.
    :returns: Decrypted string.
    """
    decipher_text = ""
    for char in ciphertext:
        decipher_text += decrypt_char(char, key)
    return decipher_text


def decrypt_with_unknown_key(text):
    """
    Decrypts text by trying all possible Caesar cipher keys.

    :param text: The text to decrypt.
    :returns: The key that successfully decrypts the text.
    """
    for key in range(26):
        print(decrypt_caesar(text, key))
        verification = input("Is it decrypted (Y/N)? ")
        if verification == "Y":
            return key


def encrypt_with_unknown_key(text):
    """
    Encrypts text using a random Caesar cipher key.

    :param text: The text to encrypt.
    :returns: Encrypted text using a randomly chosen key.
    """
    key = randrange(0, 26)
    encrypted_text = encrypt_caesar(text, key)
    return encrypted_text



def main():
    """
    Main function to interact with the user for encryption and decryption.

    :returns: None
    """
    while True:
        modus = input("Do you want to encrypt or decrypt? ")
        if modus == "stop":
            break
        elif modus.lower().strip() == "encrypt":
            text = input("Enter the text to encrypt: ")
            key = int(input("Enter the key for encryption (0 for unknown): "))
            if key == 0:
                print(encrypt_with_unknown_key(text))
            else:
                print(encrypt_caesar(text, key))
        elif modus.lower().strip() == "decrypt":
            text = input("Enter the text to decrypt: ")
            key = int(input("Enter the key for decryption (0 for unknown): "))
            if key == 0:
                unknown_key = decrypt_with_unknown_key(text)
                print(f"The key was {unknown_key}")
            else:
                print(decrypt_caesar(text, key))
        else:
            print("Please enter 'encrypt' or 'decrypt'")


if __name__ == "__main__":
    main()
