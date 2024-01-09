import argparse
 
msg = "This app is an encoder and decoder for morse code and plain text"



# Initialize parser
parser = argparse.ArgumentParser()
 
# Adding optional argument
parser.add_argument("-d", "--decode", help = "Sets decode mode")
parser.add_argument("-e", "--encode", help = "Sets encode mode")
 
# Read arguments from command line
args = parser.parse_args()
 
if args.encode:
    print(args.keys)

