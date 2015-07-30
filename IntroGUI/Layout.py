__author__ = 'zwx'

from tkinter import *

def colorgen():
    while True:
        yield "red"
        yield "yellow"
        yield "Green"

ALL = N+S+W+E

class Application(Frame):
    def __init__(self, master=None):
        colors = colorgen()
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)

        for r in range(1, 3):
            self.rowconfigure(r, weight=1)
            Label(self, text="Frame {0}".format(r), bg=next(colors)).grid(row=r, column=1, columnspan=2, sticky=ALL)

        self.rowconfigure(3, weight=0)
        for c in range(1, 3):
            self.columnconfigure(c, weight=1)
            Button(self, text="Button {0}".format(c)).grid(row=3, column=c, sticky=E+W)

        self.rowconfigure(1, weight=1)
        Frame(self)
        Label(self, text="Frame 3", bg=next(colors)).grid(row=1, column=3, rowspan=2, columnspan=3, sticky=ALL)

        for c in range(3, 6):
            self.columnconfigure(c, weight=1)
            Button(self, text="Button {0}".format(c)).grid(row=3, column=c, sticky=E+W)


root = Tk()
app = Application(master=root)
app.mainloop()
