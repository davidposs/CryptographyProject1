""" Defines the RowTransposition class """

class RowTransposition():
    """ Class to perform a row transposition cipher """
    def __init__(self, key):
        self.key = [int(i) for i in key]
        self.text_length = 0
    def populate_matrix(self, input_text, len_pt, len_key):
        k = 0
        for i in range (0, len_pt / len_key):
           for j in range(0, len_key): #number of columns
               self.text[i].append(input_text[k])
               k += 1
               if k > len_pt:
                   return
        return

    def set_matrix(self, input_file): # sets the plaintext matrix
        with open(input_file) as text:
            plaintext = text.read().rstrip()
        i = 97
        self.text = [[] for _ in self.key]
        if len(plaintext) % len(self.key) != 0:
            while len(plaintext) % len(self.key) != 0: #fill remaining spots in matrix
                plaintext += chr(i)   # appends new letter starting from a
                i += 1
        self.populate_matrix(plaintext, len(plaintext), len(self.key))
        self.text_length = len(plaintext)
        self.text = filter(None, self.text)

    def encrypt(self, input_file):
        self.set_matrix(input_file)
        ciphertext = ""
        num_rows = self.text_length / len(self.key)
        num_columns = len(self.key)
        for i in self.key:
            i -= 1
            for j in range(0, num_rows):
                ciphertext += self.text[j][i]
        encrypted_file = open('rts-encrypted.txt', 'w')
        encrypted_file.write(ciphertext)
        print "Created file: rts-encrypted.txt"

    def decrypt(self, input_file):
        with open(input_file) as text:
            ciphertext.read().rstrip()
        plaintext = ""
        for i in range(0, len(ciphertext)):
            
        

#end
