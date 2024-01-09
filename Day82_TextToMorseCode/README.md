# Morse Code Encoder/Decoder

This is a basic command line tool that takes input text or morse code and encodes it or decodes it depending on the mode.


## Usage 
### Interactive
The application has the ability to run in interactive mode that prompts the user step by step.
1. Run the app with `python main.py` in the project folder.

2. Enter either a `D` or `E` whether you would rather decode or encode the message.

3. Enter plain-text if encoding, or morse code if decoding.

4. Enjoy your encoded/decoded message!


### Silent 
The application can also run silently, taking in options and the message as command line arguments and printing only the output, making the application felxible for simply speedier use, with scripts, or other forms of automation.

1. Move to the project root directory in the Terminal

2. Run the main application file with python, and provide nececssary argument: -d for decode, and -e for encode, followed by the message surrounded in quotes if there are spaces. Use -h or --help to display the available options on the command line. ex: `python main.py -e "Hello World"` or `python main.py -h`

3. Enjoy your encoded/decoded message printed to the Terminal!
