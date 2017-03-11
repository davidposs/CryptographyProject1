#!/usr/bin/python2.7

class Vigenre:

	def __init__(self):
		self.key = None
		return

	def setKey(self, key):
		if(any(char.isdigit() for char in key) == False):
			self.key = key
			return True
		else:
			return False
			
		
		
	def encrypt(self, input_file, output_file):
		ct = ''
		with open(input_file) as plaintext:
            		text = plaintext.read().replace("\n", "")


        	print text
		modKey = self.key
		size = len(modKey)
		if(len(text) > len(modKey)):
			for i in range(0,len(text) + 1):
				if(i > size):
					modKey += modKey[i - size - 1]
		for i in range(len(text)):
			ct += chr((((ord(text[i]) + (ord(modKey[i]) - 97)) - 97) % 26) + 97)

		encrypted_file = open(output_file, 'w')
        	encrypted_file.write(ct)
        	print "Created file: " + output_file
		
			

	def decrypt(self, input_file, output_file):
		pt = ''
        	with open(input_file) as ciphertext:
            		text = ciphertext.read().replace("\n", "")
	

        	print text
		modKey = self.key
		size = len(modKey)
		if(len(text) > len(modKey)):
			for i in range(0,len(text) + 1):
				if(i > size):
					modKey += modKey[i - size - 1]
		for i in range(len(text)):
			pt += chr((((ord(text[i]) - (ord(modKey[i]) - 97)) - 97) % 26) + 97)
		        encrypted_file = open(output_file, 'w')
        	encrypted_file.write(pt)
       		print "Created file: " + output_file
	
