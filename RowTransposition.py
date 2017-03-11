#!/usr/bin/python2.7
""" Defines the RowTransposition class """
import sys

class RowTransposition():
    """ Class to perform a row transposition cipher
        Key must be consecutive integers when sorted and start from 1 """
    def __init__(self):
        self.key = [] #length of key = number of columns
        self.text_length = 0
        self.text = [[]]

    def setKey(self, key):
	try:
		temp = sorted(key)
		""" Check if key has all consecutive values """
		for i in range (0, len(temp)):
		    if not i + 1 == int(temp[i]):
		        print "Invalid key"
		        sys.exit(1)
		self.key = [int(i) for i in key]
		return True
	except:
		return False


    def populate_matrix(self, input_text, len_pt, len_key):
        """ Adds values to the matrix if it does not not fill its rows """
        k = 0
        for j in range(0, len_pt / len_key + 1): #number of rows
            for i in range(0, len_key): #number of columns
                self.text[i].append(input_text[k])
                k += 1
                if k >= len_pt:
                    return
        return

    def set_matrix(self, input_file):
        """ Adds characters as needed to plaintext matrix to fill rows """
        with open(input_file) as text:
            plaintext = text.read().rstrip()
        i = 97
        self.text = [[] for _ in self.key]
        if len(plaintext) % len(self.key) != 0:
            while len(plaintext) % len(self.key) != 0: #fill remaining spots in matrix
                plaintext += chr(i)   # appends new letter starting from a
                i += 1
        self.populate_matrix(plaintext, len(plaintext), len(self.key))
        """ Set the length here to know number of rows needed in encryption """
        self.text_length = len(plaintext)

    def encrypt(self, input_file, output_file):
        """ Creates a ciphertext after setting the plaintext matrix """
        self.set_matrix(input_file)
        ciphertext = ""
        num_rows = self.text_length / len(self.key)
        for i in self.key:
            i -= 1 #subtract 1 for indexing purposes
            for j in range(0, num_rows):
                ciphertext += self.text[i][j]

        encrypted_file = open(output_file, 'w')
        encrypted_file.write(ciphertext)
        print "Created file: " + output_file

    def decrypt(self, input_file, output_file):
        """ Decrypts a string, not a list or matrix """
        with open(input_file) as text:
            ciphertext = text.read().rstrip()
        plaintext = ""
        num_rows = len(ciphertext) / len(self.key)
        for k in range(0, num_rows):
            for i in range(1, len(self.key) + 1):
                j = self.key.index(i)
                plaintext += ciphertext[j * num_rows + k]

        decrypted_file = open(output_file, 'w')
        decrypted_file.write(plaintext)
        print "Created file: " + output_file

#end
