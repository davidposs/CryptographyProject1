from vig import VigenereCipher
from caesar import CaesarCipher
from RowTransposition import RowTransposition
import argparse

# """ Main function for the cipher programs """

"""
def main():
#    main function
    parser = argparse.ArgumentParser(description = "Multi-cipher encryption program")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argumet('-e', dest = 'encrypt', action='store_true', help='Give a file to encrypt')
    group.add_argument('-d', dest = 'decrypt', action='store_true', help = 'Give a file to decrypt')
    parser.add_argument('key', type = str, nargs ='?', help = 'key for encoding')
    parser.add_argument('filename', type = str, help = 'The file to encrypt or decrypt')

    args = parser.parse_args()
"""

#vig = VigenereCipher('LEMON')
#vig.set_key('plaintext.txt')
#print vig.key + '\n'
#vig.encrypt('plaintext.txt')
#vig.decrypt('vig-encrypted.txt')

#ces = CaesarCipher(8)
#ces.encrypt('plaintext.txt')
#ces.decrypt('ces-encrypted.txt')

rtp = RowTransposition('4321')
rtp.encrypt('plaintext.txt')
