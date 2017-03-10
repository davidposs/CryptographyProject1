""" Declares and defines Caesar Cipher class
    Defines init, encrypt, and decrypt methods
    Preserves the case and punctuation of the original text
"""

class CaesarCipher():
    """ Class to perform a caesar cipher with user given key and file """
    def __init__(self, key):
        """ Initializes the class """
        self.key = 0
        self.text = ""

    def set_key(self, key):
        self.key = int(key)

    def encrypt(self, key, input_file):
        """ Encrypts given file, preserves punctuation and case """
        self.set_key(key)
        self.key %= 26
        ciphertext = ""
        with open(input_file) as plaintext:
            self.text = plaintext.read()
        for char in self.text:
            if char.isalpha():
                if 65 <= ord(char) <= 90: #char is between A and Z
                    if ord(char) + self.key <= 90:
                        ciphertext += chr(ord(char) + self.key)
                    elif ord(char) + self.key > 90:
                        ciphertext += chr(ord(char) + self.key - 26)
                if 97 <= ord(char) <= 122:
                    if ord(char) + self.key <= 122:
                        ciphertext += chr(ord(char) + self.key)
                    elif ord(char) + self.key > 122:
                        ciphertext += chr(ord(char) + self.key - 26)
            else:
                ciphertext += char
        encrypted_file = open("ces-encrypted.txt", 'w')
        encrypted_file.write(ciphertext)
        print "Created file: ces-encrypted.txt\n"

    def decrypt(self, key, input_file):
        """ Decrypts a given file """
        self.set_key(key)
        self.key %= 26
        plaintext = ""
        with open(input_file) as encrypted_text:
            self.text = encrypted_text.read()
        for char in self.text:
            if char.isalpha():
                if 65 <= ord(char) <= 90: #char is between A and Z
                    if ord(char) - self.key >= 65: #65 = ord('A')
                        plaintext += chr(ord(char) - self.key)
                    elif ord(char) - self.key < 65:
                        plaintext += chr(ord(char) - self.key + 26)
                if 97 <= ord(char) <= 122:
                    if ord(char) - self.key >= 97:
                        plaintext += chr(ord(char) - self.key)
                    elif ord(char) - self.key < 97:
                        plaintext += chr(ord(char) - self.key + 26)
            else:
                plaintext += char

        decrypted_file = open("ces-decrypted.txt", 'w')
        decrypted_file.write(plaintext)
        print "Created file: ces-decrypted.txt"

#end
