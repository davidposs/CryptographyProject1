#!/usr/bin/python2.7
""" Program implementing various cryptographic ciphers """

from Railfence import RailfenceCipher
from vigenre import Vigenre
from playfair import Play
from caesar import CaesarCipher
from RowTransposition import RowTransposition
import sys

def main():
    args = str(sys.argv)
    cipher = sys.argv[1].lower()
    key = sys.argv[2]
    mode = sys.argv[3].upper()
    input_file = sys.argv[4]
    output_file = sys.argv[5]

    if mode == "ENC":
            if cipher == 'vig':
                vig = Vigenre()
                vig.setKey(key)
                vig.encrypt(input_file, output_file)

            elif cipher == 'ces':
                ces = CaesarCipher()
                ces.encrypt(key, input_file, output_file)

            elif cipher == 'rts':
                rts = RowTransposition()
                rts.encrypt(key, input_file, output_file)

            elif cipher == 'rfc':
                rfc = RailfenceCipher()
                rfc.encrypt(key, input_file, output_file)

            elif cipher == 'plf':
                plf = Play()
                plf.setKey(key)
                plf.encrypt(input_file, output_file)

    elif mode == "DEC":
            if cipher == 'vig':
                vig = Vigenre()
                vig.setKey(key)
                vig.decrypt(input_file, output_file)
            elif cipher == 'ces':
                ces = CaesarCipher()
                ces.decrypt(key, input_file, output_file)
            elif cipher == 'rts':
                rts = RowTransposition()
                rts.decrypt(key, input_file, output_file)
            elif cipher == 'rfc':
                rfc = RailfenceCipher()
                rfc.decrypt(key, input_file, output_file)
            elif cipher == 'plf':
                plf = Play()
                plf.setKey(key)
                plf.decrypt(input_file, output_file)

    else:
        print "Invalid mode: use DEC/ENC"

    exit()

if __name__ == "__main__":
    main()

