#Basics
"""
from breezypythongui import EasyFrame

class MyApp(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Hello App")
        self.addLabel(text="Hello World", row=100, column=10)

def main():
    MyApp().mainloop()

main()
"""
#4Quadrants
"""
from breezypythongui import EasyFrame

class MyApp(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="4 QUADRANTS")
        self.addLabel(text="00", row=0, column=0)
        self.addLabel(text="10", row=1, column=0)
        self.addLabel(text="01", row=0, column=1)
        self.addLabel(text="11", row=1, column=1)

def main():
    MyApp().mainloop()

main()
"""
#Image
"""
from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font

class ImageDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,title="Image Demo")
        self.setResizable(False)


        ImageLabel = self.addLabel(text="",row=0,column=0)
        textLabel = self.addLabel("Pussy the Cat", row =1, column = 0)

        self.image = PhotoImage(file="giphy.gif")
        ImageLabel["image"] = self.image

        font = Font(family = "Verdana",size=20,slant="italic")
        textLabel["font"] = font
        textLabel["foreground"] = "black"
def main():
        ImageDemo().mainloop()
if __name__=="__main__":
        main()
"""

#GIF frame
"""
from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font

class ImageDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Animated GIF Demo")

        font = Font(family="Verdana", size=20, slant="italic")
        self.addLabel("Animated GIF", row=0, column=0, font=font)

        self.label = self.addLabel("", row=1, column=0)

        
        self.frames = []
        i = 0
        while True:
            try:
                frame = PhotoImage(file="giphy.gif", format=f"gif -index {i}")
                self.frames.append(frame)
                i += 1
            except:
                break

        self.frame_index = 0
        self.animate()

    def animate(self):
        self.label["image"] = self.frames[self.frame_index]
        self.frame_index = (self.frame_index + 1) % len(self.frames)
        self.after(100, self.animate) 

def main():
    ImageDemo().mainloop()

main()
"""
#GIF multiframe
"""
from breezypythongui import EasyFrame


class ButtonDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Button Demo")

        self.label = self.addLabel(text="Hello World",row=0,column=0,columnspan=2,sticky="NSEW")

        self.clearBtn = self.addButton(text="Clear",row=1,column=0,command=self.clearText)

        self.restoreBtn = self.addButton(text="Restore",row=1,column=1,state="disabled",command=self.restoreText)

    def clearText(self):
        self.label["text"] = ""
        self.clearBtn["state"] = "disabled"
        self.restoreBtn["state"] = "normal"

    def restoreText(self):
        self.label["text"] = "Hello World"
        self.clearBtn["state"] = "normal"
        self.restoreBtn["state"] = "disabled"


def main():
    ButtonDemo().mainloop()


if __name__ == "__main__":
    main()
"""
#try except
from breezypythongui import EasyFrame
import math

class SqrtApp(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Square Root")

        self.addLabel("Enter Number", 0, 0)
        self.inputField = self.addIntegerField(0, 0, 1)

        self.addLabel("Result", 1, 0)
        self.outputField = self.addFloatField(0.0, 1, 1)

        self.addButton("Compute", 2, 0, command=self.computeSqrt)

    def computeSqrt(self):
        try:
            number = self.inputField.getNumber()
            if number < 0:
                raise ValueError
            self.outputField.setNumber(math.sqrt(number))
        except ValueError:
            self.messageBox("ERROR", "Input must be ≥ 0")

SqrtApp().mainloop()


#
"""
"""
#
"""
"""
#
"""
"""
#
"""
"""
#
"""
"""
#
"""
"""
#
"""
"""
#
"""
"""
#
"""
"""
#
"""
"""
#
"""
"""
#
"""
"""
#
"""
"""
#
"""
"""
#
"""
"""
