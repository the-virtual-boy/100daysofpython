from tkinter import *
import requests
from time import sleep

FONT = (10)

words = requests.get("https://random-word-api.vercel.app/api?words=50").text[2:-2].split('","')
print(words)


## app stuff
class TypingTest(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__()        
        self.title('Super Typing Tester!')
        self.geometry("400x350")  # Width x Height
        self.typed = []
        self.L = Label(self, text = "Type Here!")

        self.T = Text(self, height = 8, width = 52, font=FONT, wrap=WORD)
        self.T2 = Text(self, height = 4, width = 52, font=FONT, wrap=WORD, background='grey')
        self.B = Button(text="get", command=self.gettext)
        self.B2 = Button(text="2", command=self.gettext2)
        self.fillbox()
        # self.T2.insert('1.0', words)
        # self.gettext()
        # self.T2['state'] = 'disabled'
        self.L.pack()
        self.T2.pack()
        self.T.pack()
        self.B.pack()
        self.B2.pack()

    def fillbox(self):
         index = 0
         for word in words:
              self.T2.insert(f'1.{index}', word + ' ')              
              index += len(word) + 1
              sleep(.1)

    def gettext(self):
        print(self.T2.count('1.0', 'end','displaylines')[0])
        for i in range(1,self.T2.count('1.0', 'end','displaylines')[0] + 1):
            start_line = f'1.0 + {i - 1} display lines'
            print(self.T2.get(f'{start_line}', f'{start_line} + 1 display lines'))

    def gettext2(self):
                self.T2.see('1.0 + 8 display lines')

    
    def checktext(self):
        print('checking: ', self.T.get('1.0', '1.1') == 'O')
        return self.T.get('1.0', '1.1') == 'O'
    
    def key_press(self, e):
        print(e)
        print("key has been pressed")
         


app = TypingTest()
sleep(1)
app.T.get('1.0', '1.1')

app.bind('<KeyPress>',app.key_press)
if app.checktext():
    print(app.gettext())
app.mainloop()