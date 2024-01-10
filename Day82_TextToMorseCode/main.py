# This application takes morse code or plain-text and translates it to the other
#
# Author: me ;)

#imports
import argparse
import winsound
from time import sleep


#globals
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ',':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', '\'':'.----.',
                      ' ':'/'}

PLAIN_TEXT_DICT = {'.-': 'A', '-...': 'B', '-.-.': 'C',
                    '-..': 'D', '.': 'E', '..-.': 'F',
                    '--.': 'G', '....': 'H', '..': 'I',
                    '.---': 'J', '-.-': 'K', '.-..': 'L',
                    '--': 'M', '-.': 'N', '---': 'O',
                    '.--.': 'P', '--.-': 'Q', '.-.': 'R',
                    '...': 'S', '-': 'T', '..-': 'U',
                    '...-': 'V', '.--': 'W', '-..-': 'X',
                    '-.--': 'Y', '--..': 'Z', '.----': '1',
                    '..---': '2', '...--': '3', '....-': '4',
                    '.....': '5', '-....': '6', '--...': '7',
                    '---..': '8', '----.': '9', '-----': '0',
                    '--..--': ', ', '.-.-.-': '.', '..--..': '?',
                    '-..-.': '/', '-....-': '-', '-.--.': '(',
                    '-.--.-': ')', '.----.':'\'', '/': ' '}

msg="Encodes plain text to morse code or decodes morse code to plain text.\n" \
    "Runs in silent mode if given -de and messag (in quotes if there are spaces)"

frequency = 825
dit = 200
dah = 500
space_rest = .1
letter_rest = .3
word_rest = .6

# param arguments
parser = argparse.ArgumentParser(usage='Usage: main.py [-b] [-MODE TEXT]')

parser.add_argument("-d", "--decode", help = "Sets decode mode", metavar='CODE')
parser.add_argument("-e", "--encode", help = "Sets encode mode", metavar='TEXT')
parser.add_argument("-b", "--beep", help = "Plays morse code beeps. Only usable with encode", action='store_true')

args = parser.parse_args()

#functions

## function in charge decoding or encoding input message
def convert(code, mode):
    
    ## decides whether to encode or decode
    if mode == 'E':
        if code[0].upper() not in MORSE_CODE_DICT:
            raise Exception(f"Untranslatable character. Available characters: {MORSE_CODE_DICT.keys()}")
        elif len(code) == 1:
            return f"{MORSE_CODE_DICT[code[0].upper()]}"
        else:
            return f"{MORSE_CODE_DICT[code[0].upper()]} {convert(code[1:], mode)}"
    elif mode == 'D':
        if type(code) == str:
            code = code.split(' ')

        if code[0].upper() not in PLAIN_TEXT_DICT:
            raise Exception(f"Untranslatable character. Available characters: {PLAIN_TEXT_DICT.keys()}")
        elif len(code) == 1:
            return f"{PLAIN_TEXT_DICT[code[0].upper()]}"
        else:
            return f"{PLAIN_TEXT_DICT[code[0]]}{convert(code[1:], mode)}"
    else:
        return f"Error: incorrect value for mode. Use either E for encode or D for decode."

def code_beep(code):
    for word in code.split(' '):
        for symbol in word:
            if symbol == '.':
                winsound.Beep(frequency, dit)
            elif symbol == '-':
                winsound.Beep(frequency, dah)
            elif symbol == '/':
                sleep(word_rest)
            sleep(space_rest)
        sleep(letter_rest)

def secure_choice(msg, opt):
    inp = input(msg)[0].upper()
    if inp not in opt:
        return secure_choice(f"That is not a valid option, please select from: {opt}: ", opt)
    else:
        return inp


if args.decode:
    encoded_message = convert(args.decode, 'D')
    print(encoded_message)
elif args.encode:
    encoded_message = convert(args.encode, 'E')
    print(encoded_message)
    if args.beep:
        code_beep(encoded_message)
else:
    ## get mode and message from user
    set_mode = secure_choice("Do you want to (E)ncode or (D)ecode a message?: ", ('E', 'D'))
    
    text_to_convert = input("Text to Convert: ")

    ## convert it
    encoded_message = convert(text_to_convert, set_mode)

    ## output morse code
    print(f"Your {'decoded' if set_mode == 'D' else 'encoded'} message: \n{encoded_message}")

    ## request beeps
    if set_mode == 'E':
        beep = secure_choice("Would you like to hear your message? (Y or N): ", ('Y', 'N'))

        if beep == 'Y':
            code_beep(encoded_message)