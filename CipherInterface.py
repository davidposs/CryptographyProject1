""" Defines parent class for ciphers """

class CipherInterface(object):
    """ The abstract class others will inherit from"""

#    @abstractmethod
    def __init__(self, cipher, key, input_file):
        """ Initialize the class """
        self.key = key
        self.cipher = cipher
        self.input_file = input_file
        self.text = ""

    def set_key(self):
        """ Validate the key """
        raise NotImplementedError("Subclass must implement abstract method 'validateKey'")

    def encrypt(self):
        """ Parent function to encrypt the plaintext """
        raise NotImplementedError("Subclass must implement abstract method 'encrypt'")

    def decrypt(self):
        """ Parent function to decrypt the ciphertext """
        raise NotImplementedError("Subclass must implement abstract method 'decrypt'")

    def get_file_text(self):
        """ Returns the file given by the user as a string """
        with open(self.input_file, 'r') as file_to_read:
            self.text = file_to_read.read()

        return self.__text
