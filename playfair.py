#!/usr/bin/python2.7
class Play:
    def __init__(self):
        self.key = None

    def setKey(self,key):
        if(any(char.isdigit() for char in key) == False):
            self.key = key
            s = []
            tableX = tableY = 0
            global matrix
            matrix = [[0 for x in range(0,5)] for y in range(0,5)]
            current = 0
            alphabet = key+"abcdefghiklmnopqrstuvwxyz"
            for i in range(0, len(alphabet)):
                if(alphabet[i] not in s):
                    s.insert(current,alphabet[i])
                    current += 1
            for i in range(0,len(s)):
                matrix[tableY][tableX] = s[i]
                if(tableX == 4):
                    tableY += 1
                    tableX = 0
                else:
                    tableX += 1
            return True
        else:
            return False

    def encrypt(self, input_file, output_file):
        cipherText = ""
        with open(input_file) as plaintext:
            text = plaintext.read().replace("\n", "")


        print text
        myList = [i for i in text]
        for i in range(0, len(text)-1,2):
            if(myList[i] == myList[i+1]):
                myList.insert(i+1,'x')
        if(len(myList) %2 != 0):
            myList.append('x')
        for i in range(0, len(myList),2):
            cipherText = self.checkPositionENC(myList[i], myList[i+1],cipherText)

        encrypted_file = open(output_file, 'w')
        encrypted_file.write(cipherText)
        print "Created file: " + output_file

    def decrypt(self, input_file, output_file):
        decryptedText = ""
        with open(input_file) as ciphertext:
            text = ciphertext.read().replace("\n", "")
        decList = [i for i in text]
        for i in range(0, len(text)-1,2):
            if(decList[i] == decList[i+1]):
                decList.insert(i+1,'x')
        if(len(decList) %2 != 0):
            decList.append('x')
        for i in range(0, len(decList),2):
            decryptedText = self.checkPositionDEC(decList[i], decList[i+1],decryptedText)
        if(decryptedText[-1:] == 'x'):
            decryptedText = decryptedText[:-1]

        decrypted_file = open(output_file, 'w')
        decrypted_file.write(decryptedText)
        print "Created file: " + output_file

    def checkPositionDEC(self, num1, num2, decryptedText):
        for i in range(5):
            for j in range(5):
                if(matrix[i][j] == num1):
                    num1R = i
                    num1C = j
                if(matrix[i][j] == num2):
                    num2R = i
                    num2C = j
        if(num1C == num2C):
            if(num1R == 0):
                decryptedText += matrix[4][num1C]
            elif(num1R > 0):
                decryptedText += matrix[num1R - 1][num1C]
            if(num2R == 0):
                decryptedText += matrix[4][num1C]
            elif(num2R > 0):
                decryptedText += matrix[num2R - 1][num2C]
        elif(num1R == num2R):
            if(num1C == 0):
                decryptedText += matrix[num1R][4]
            elif(num1C > 0):
                decryptedText += matrix[num1R][num1C - 1]
            if(num2C == 0):
                decryptedText += matrix[num2R][4]
            elif(num2C > 0):
                decryptedText += matrix[num2R][num2C - 1]
        else:
            decryptedText += matrix[num1R][num2C]
            decryptedText += matrix[num2R][num1C]
        return decryptedText



    def checkPositionENC(self, num1, num2, cipherText):
        for i in range(5):
            for j in range(5):
                if(matrix[i][j] == num1):
                    num1R = i
                    num1C = j
                if(matrix[i][j] == num2):
                    num2R = i
                    num2C = j
        if(num1C == num2C):
            if(num1R == 4):
                cipherText += matrix[0][num1C]
            elif(num1R < 4):
                cipherText += matrix[num1R + 1][num1C]
            if(num2R == 4):
                cipherText += matrix[0][num1C]
            elif(num2R < 4):
                cipherText += matrix[num2R + 1][num2C]
        elif(num1R == num2R):
            if(num1C == 4):
                cipherText += matrix[num1R][0]
            elif(num1C < 4):
                cipherText += matrix[num1R][num1C + 1]
            if(num2C == 4):
                cipherText += matrix[num2R][0]
            elif(num2C < 4):
                cipherText += matrix[num2R][num2C + 1]
        else:
            cipherText += matrix[num1R][num2C]
            cipherText += matrix[num2R][num1C]
        return cipherText
