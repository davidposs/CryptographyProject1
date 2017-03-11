#!/usr/bin/python2.7
""" Declares Railfence Class """

class RailfenceCipher():
    """ Preserves case. Uses an integer as a key """
    def __init__(self):
        """ Initializes with empty text and user given key """
        self.key = 0
        self.text = ""
        self.railLengths = []
        self.railStarts = []

    def setKey(self, key):
        try:
		self.key = int(key)
		return True
	except:
		return False

    def encrypt(self,input_file, output_file):
        """ Preserves case, spacing and punctuation """
        with open(input_file) as text:
            self.text = text.read()
        ciphertext = ""

        """ Used to jump to the next letter in the plaintext """
        offset = self.key

        for i in range(0, self.key + 1):
            for j in range(0, len(self.text) / self.key + 1):
                if offset * j + i >= len(self.text):
                    continue
                if len(ciphertext) >= len(self.text):
                    ciphertext = ciphertext.replace("\n", "")
                    encrypted_file = open(output_file, 'w')
                    encrypted_file.write(ciphertext)
                    print "Created file: " + output_file
                    return
                else:
                    ciphertext += self.text[offset*j + i]

        encrypted_file = open(output_file, 'w')
        encrypted_file.write(ciphertext)
        print "Created file: " + output_file

    def getRails(self):
        """ Used to facilitate decryption """
        text = self.text
        key = self.key
        """ Gets the location that each rail begins, and their lengths """

        """ Expected # of letters per rail """
        lettersPerRail = len(text) / key

        """ Number of rails with extra letters """
        extraLetters = len(text) % key

        """ List to store the lengths of each rail, including those with extra letters """
        railLengths = []
        startIndex = 0
        """ List storing where each new rail starts in the ciphertext """
        railStartIndexes = []
        currentRail = 0
        while currentRail < key:
            count = lettersPerRail
            railStartIndexes.append(startIndex)

            if 0 < extraLetters:
                """ Count keeps track of how many letters are in the longer rail """
                count += 1
                """ Decrement the count for each letter accounted for """
                extraLetters -= 1

            railLengths.append(count)
            startIndex += count
            currentRail += 1

        self.railLengths = railLengths
        self.railStarts = railStartIndexes

    def decrypt(self,input_file, output_file):
        """ Decrypts given ciphertext """
        with open(input_file) as text:
            self.text = text.read()#.replace('\n', "")
        self.getRails()
        """ Current letter in the ciphertext """
        currentLetter = 0

        """ String containing the plaintext """
        plaintext = ""

        """Current rail we are at """
        currentRailIndex = 0

        while currentRailIndex < self.railLengths[0]:
            currentRail = 0
            while currentRail < self.key:
                if not len(plaintext) == len(self.text):
                    plaintext += self.text[self.railStarts[currentRail] + currentRailIndex]

                currentRail += 1
            currentRailIndex += 1

        plaintext = plaintext.replace("\n", "")
        decrypted_file = open(output_file, 'w')
        decrypted_file.write(plaintext)
        print "Created file: " + output_file

