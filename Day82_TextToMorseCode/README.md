# Morse Code Encoder/Decoder

This is a basic command line tool that takes input text or morse code and encodes it or decodes it depending on the mode.


## Usage 
### Interactive
The application has the ability to run in interactive mode that prompts the user step by step.
1. Run the app with `python main.py` in the project folder.

2. Enter either a `D` or `E` whether you would rather decode or encode the message.

3. Enter plain-text if encoding, or morse code if decoding.

4. If you chose to encode, then you will be prompted whether you want to hear the morse code be played for you.

4. Enjoy your encoded/decoded message!


### Silent 
The application can also run silently, taking in options and the message as command line arguments and printing only the output, making the application felxible for simply speedier use, with scripts, or other forms of automation.

1. Move to the project root directory in the Terminal

2. Run the main application file with python, and provide nececssary argument: `-d` for decode, and `-e` for encode, followed by the message surrounded in quotes if there are spaces. Use `-h` or `--help` to display the available options on the command line. ex: `python main.py -e "Hello World"` or `python main.py -h`

3. Optionaly you can use the '-b' option with encode mode to have the app play the morse code after encoding.

4. Enjoy your encoded/decoded message printed to the Terminal!


## Thoughts

In short, I created a command line translator as requested for day 82 of the 100 Days of Code, but I added a few more features.

1. It not only encodes plain text to morse code, but decodes given morse code to plain text.

2. I added command line options to allow a user to give all options when running the app which doubles as a silent mode.

3. I added features to play the morse code using windows sounds via the winsound library.

The hardest part was figuring out where to stop I suppose. I knew these projects were coming up and was excited with how much I wanted to go all out, but what started as an assignment I was able to complete in an hour, turned into 3 days of brainstorming, debugging, and fine tuning. Aside from that, I wanted to start laying out my project in a more "professional" manner, but instructions for doing that wasn't as simple as I expected, and it doesn't seem like many tutorials cover it. Everywhere I looked pointed to large textbooks to really understand the convention for layout, naming, etc of a python program.

One of my favorite things is how much I ended up learning just by wanting to do something. I indirectly ended up watching a video about "dunder methods", learned a few new libraries for the features I wanted to add, and got a lot of practice.
