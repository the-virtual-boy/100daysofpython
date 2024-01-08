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
                    '(':'-.--.', ')':'-.--.-', ' ':'/'}


#functions

## function in charge of converting text to morse code
def convert(code):
    global MORSE_CODE_DICT
    if len(code) == 1:
        return f"{MORSE_CODE_DICT[code[0].upper()]}"
    else:
        return f"{MORSE_CODE_DICT[code[0].upper()]} {convert(code[1:])}"

            
## take input as text
text_to_convert = input("Text to Convert: ")


## convert it
encoded_message = [convert(text_to_convert)]


## output morse code
print(f"Your message in Morse code is: {encoded_message}")