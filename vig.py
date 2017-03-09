""" Declares and defines the Vigenere Cipher class
    This program converts the plaintext or ciphertext to uppercase
    Does not work it plaintext or ciphertext has punctuation or non letters
"""

class VigenereCipher():
    """ Defines viginere cipher class based off CipherInterface """
    def __init__(self, key):
        self.key = key
        self.text = ""

    def set_key(self, input_file):
        """ Validation: key must be equal length as the plain and cipher text"""
        with open(input_file) as text_to_match:
            self.text = text_to_match.read()
        self.text = self.text.upper()
        if len(self.key) == len(self.text):
            return

        elif len(self.key) < len(self.text):
            i = 0
            while len(self.key) < len(self.text) - 1:
                self.key += self.key[i]
                i += 1
            return self.key
        else:
            raise ValueError("Your key is too large!")

    def encrypt(self, input_file):
        """ Applies vigenere cipher to the plaintext given """
        self.set_key(input_file)
        self.key = self.key.upper()
        ciphertext = ""
        i = 0
        for char in self.text:
            if char.isalpha(): # if letter belongs to a..z
                current_letter = self.key[i]
                if 65 <= ord(char) <= 90:
                    if ord(current_letter) + ord(char) <= 90:
                        ciphertext += chr(ord(current_letter) + ord(char))
                    elif ord(current_letter) + ord(char) > 90:
                        # Get the position of the current letter in the alphabet
                        pos_in_alphabet = ord(current_letter) % 26 + ord(char) % 26
                        pos_in_alphabet %= 26
                        ciphertext += chr(pos_in_alphabet + ord('A'))
                    i += 1
            else:
                ciphertext += char

        encrypted_file = open('vig-encrypted.txt', 'w')
        encrypted_file.write(ciphertext)
        print "Created file: vig-encrypted.txt"

    def decrypt(self, input_file):
        """ Decrypts the file, preserving text case and punctuation """
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
        print "Created file: vig-decrypted.txt"

#end
