from Railfence import RailfenceCipher
from vig import VigenereCipher
from caesar import CaesarCipher
from RowTransposition import RowTransposition
import argparse

# """ Main function for the cipher programs """


def main():
#    main function
    parser = argparse.ArgumentParser(description = "Multi-cipher encryption program")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-e', dest = 'encrypt', action='store_true', help='Give a file to encrypt')
    group.add_argument('-d', dest = 'decrypt', action='store_true', help = 'Give a file to decrypt')
    parser.add_argument('cipher', type = str, nargs = 1, help = 'cipher to use')
    parser.add_argument('key', type = str, nargs ='?', help = 'key for encoding')
    parser.add_argument('filename', type = str, help = 'The file to encrypt or decrypt')

    args = parser.parse_args()
    key = args.key
    cipher = args.cipher[0]
    filename = args.filename

    if args.encrypt:
            if cipher == 'vig':
                vig = VigenereCipher(key)
                vig.encrypt(filename)
            elif cipher == 'ces':
                ces = CaesarCipher(key)
                ces.encrypt(filename)
            elif cipher == 'rtc':
                rtc = RowTransposition(key)
                rtc.encrypt(filename)
            elif cipher == 'rfc':
                rfc = RailfenceCipher(key)
                rfc.encrypt(filename)
            elif cipher == 'pfc':
                print "I haven't done playfair yet"
                return

    elif args.decrypt:
            if cipher == 'vig':
                vig = VigenereCipher(key)
                vig.decrypt(filename)
            elif cipher == ['ces']:
                ces = CaesarCipher(key)
                ces.decrypt(filename)
            elif cipher == 'rtc':
                rtc = RowTransposition(key)
                rts.decrypt(filename)
            elif cipher == 'rfc':
                rfc = RailfenceCipher(key)
                rfc.decrypt(filename)
            elif cipher == 'pfc':
                print "Still haven't done playfair :( "
                return

    exit()

if __name__ == "__main__":
    main()

