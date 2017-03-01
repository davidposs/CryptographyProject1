""" Declares and defines the Vigenere Cipher class """
import sys

class VigenereCipher():
    """ Defines viginere cipher class based off CipherInterface """
    def __init__(self, key):
        self.key = key
        self.text = ""

    def set_key(self, input_file):
        """ Validation: key must be equal length as the plain and cipher text"""
        with open(input_file) as text_to_match:
            self.text = text_to_match.read()
            if len(self.key) <= len(self.text) - 1:
                    i = 0
                    while len(self.key) != len(self.text) - 1:
                        self.key += self.key[i]
                        i += 1
                    return self.key
            else:
                raise ValueError("Your key is too large!")
                sys.exit(1)

    def encrypt(self, input_file):
        """ Applies vigenere cipher to the plaintext given """
        self.set_key(input_file)
        ciphertext = ""
        i = 0
        for char in self.text:
            if char.isalpha(): # if letter belongs to a..z
                if 65 <= ord(char) <= 90:
                    if ord(self.key[i]) + ord(char) <= 90:
                        ciphertext += chr(ord(self.key[i]) + ord(char))
                    elif ord(self.key[i]) + ord(char) > 90:
                        m = ord(self.key[i]) % 26 + ord(char) % 26
                        m %= 26
                        ciphertext += chr(m + ord('A'))
                        # Increment i here because if the plaintext contains
                        # punctation, we don't want to encrypt it and move to
                        # the next letter in the key
                    i += 1
            else:
                ciphertext += char
        encrypted_file = open('vig-encrypted.txt', 'w')
        encrypted_file.write(ciphertext)
        print "Created file: vig-encrypted.txt\n"

    def decrypt(self, input_file):
        self.set_key(input_file)
        plaintext = ""
        i = 0
        for char in self.text:
            if char.isalpha():
                ascii_val = ord(self.text[i]) - ord(self.key[i])
                if ascii_val >= 0:       # text[i] > key[i]
                    plaintext += chr(ascii_val + 65)
                elif ord(self.text[i]) - ord(self.key[i]) < 0:
                    plaintext += chr(ascii_val + 91)
                i += 1
            else:
                plaintext += char
        decrypted_file = open('vig-decrypted.txt', 'w')
        decrypted_file.write(plaintext)
        print "Created file: vig-decrypted.txt\n"

#end
