# This application takes morse code or plain-text and translates it to the other
#
# Author: me ;)

#imports


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
                    '(':'-.--.', ')':'-.--.-', '\'':'.----.', ' ':'/'}

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

#functions

## function in charge decoding or encoding input message
def convert(code, mode):
    global MORSE_CODE_DICT

    ## decides whether to encode or decode
    if mode == 'E':
        if len(code) == 1:
            return f"{MORSE_CODE_DICT[code[0].upper()]}"
        else:
            return f"{MORSE_CODE_DICT[code[0].upper()]} {convert(code[1:], mode)}"
    elif mode == 'D':
        if type(code) == str:
            code = code.split(' ')
        if len(code) == 1:
            return f"{PLAIN_TEXT_DICT[code[0].upper()]}"
        else:
            return f"{PLAIN_TEXT_DICT[code[0]]}{convert(code[1:], mode)}"
    else:
        return f"Error: incorrect value for mode. Use either E for encode or D for decode."

            
## take input as text
set_mode = input("Do you want to (E)ncode or (D)ecode a message?: ")[0].upper()
text_to_convert = input("Text to Convert: ")


## convert it
encoded_message = [convert(text_to_convert, set_mode)]


## output morse code
print(f"Your message in Morse code is: {encoded_message}")