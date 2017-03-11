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
                if(vig.setKey(key)):
                	vig.encrypt(input_file, output_file)
		else:
			print "Key Error"

            elif cipher == 'ces':
                ces = CaesarCipher()
		if(ces.setKey(key)):
                	ces.encrypt(input_file, output_file)
		else:
			print "Key Error"

            elif cipher == 'rts':
                rts = RowTransposition()
		if(rts.setKey(key)):
                	rts.encrypt(input_file, output_file)
		else:
			print "Key Error"

            elif cipher == 'rfc':
                rfc = RailfenceCipher()
		if(rfc.setKey(key)):
                	rfc.encrypt(input_file, output_file)
		else:
			print "Key Error"

            elif cipher == 'plf':
                plf = Play()
                if(plf.setKey(key)):
                	plf.encrypt(input_file, output_file)
		else:
			print "Key Error"

    elif mode == "DEC":
            if cipher == 'vig':
                vig = Vigenre()
                if(vig.setKey(key)):
                	vig.decrypt(input_file, output_file)
		else:
			print "Key Error"

            elif cipher == 'ces':
                ces = CaesarCipher()
		if(ces.setKey(key)):
                	ces.decrypt(input_file, output_file)
		else:
			print "Key Error"

            elif cipher == 'rts':
                rts = RowTransposition()
		if(rts.setKey(key)):
                	rts.decrypt(input_file, output_file)
		else:
			print "Key Error"

            elif cipher == 'rfc':
                rfc = RailfenceCipher()
		if(rfc.setKey(key)):
                	rfc.decrypt(input_file, output_file)
		else:
			print "Key Error"

            elif cipher == 'plf':
                plf = Play()
                if(plf.setKey(key)):
                	plf.decrypt(input_file, output_file)
		else:
			print "Key Error"

    else:
        print "Invalid mode: use DEC/ENC"

    exit()

if __name__ == "__main__":
    main()

