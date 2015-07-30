#!/usr/local/bin/python
"""
Using existing framework to active following requirements:

When an area occupied by Frame 1 or Frame 2 is clicked with mouse button 1, the program
should print which frame was clicked and the X and Y coordinates (relative to the Frame).

Frame 3 should contain an Entry and a Text widget. When the button now labeled "Open" 
is clicked, the content of the Entry should be used as a file name, and the content of 
the file (if any) displayed in the Text widget.

The Entry and Text widgets should completely fill Frame 3 and continue to do so even as 
the application window is resized.

The color of the text displayed in Frame 3's Text widget should change appropriately when 
the "Red," "Blue," "Green," or "Black" buttons are clicked.
"""
from tkinter import *
from tkinter.messagebox import showerror

def colorgen():
    while True:
        yield "red"
        yield "yellow"

ALL = N+S+W+E


class Application(Frame):

    def createWidgets(self):
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)

        colors = colorgen()
        for r in range(1, 3):
            self.rowconfigure(r, weight=1)
            frame = Label(self, text="Frame {0}".format(r), bg=next(colors))
            frame.grid(row=r, column=1, columnspan=2, sticky=ALL)
            def handler(event, self=self, num=r):
                return self.handler_Frame_1_2(event, num)
            frame.bind("<Button-1>", handler)
            frame.focus()

        frame3 = Frame(self)
        frame3.grid(row=1, column=3, rowspan=2, columnspan=3, sticky=ALL)

        self.entry = Entry(frame3)
        self.entry.pack(side=TOP, fill=BOTH, expand=True)

        self.text = Text(frame3, width=1, wrap=WORD)
        self.text.pack(side=TOP, fill=BOTH, expand=True)

        self.columnconfigure(1, weight=1)
        Button(self, text="Red", command=lambda color="Red": self.set_font_color(color))\
            .grid(row=3, column=1, sticky=E+W)

        self.columnconfigure(2, weight=1)
        Button(self, text="Blue", command=lambda color="Blue": self.set_font_color(color))\
            .grid(row=3, column=2, sticky=E+W)

        self.columnconfigure(3, weight=1)
        Button(self, text="Green", command=lambda color="Green": self.set_font_color(color))\
            .grid(row=3, column=3, sticky=E+W)

        self.columnconfigure(4, weight=1)
        Button(self, text="Black", command=lambda color="Black": self.set_font_color(color))\
            .grid(row=3, column=4, sticky=E+W)

        self.columnconfigure(5, weight=1)
        Button(self, text="Open", command=self.open_handler).grid(row=3, column=5, sticky=E+W)

    def set_font_color(self, color):
        self.text.configure(fg=color)
        self.open_handler()


    def handler_Frame_1_2(self, event, frame_num):
        """ Event handler: Print the coordinates of click point on the Frame widget for
        Frame 1 and Frame 2 """
        print ('Frame clicked at %s, %s on Frame %s' % (event.x, event.y, frame_num))


    def open_handler(self):
        """Handle a click of the Open button by reading the text the
        user has placed in the Entry widget and use it as the file
        name to open."""
        self.text.configure(state='normal')
        file_path = self.entry.get()
        try:
            file = open(file_path, 'r')
        except:
            self.text.delete(0.0, END)
            self.text.configure(state='disabled')
            print("error", showerror("Error", "***Cannot open the file: %s ***" % file_path))
            return
        try:
            content = file.read()
            print ("content=", content)
        except:
            self.text.delete(0.0, END)
            self.text.configure(state='disabled')
            print("error", showerror("Error", "***Cannot read the file: %s ***" % file_path))
            return

        self.text.delete(0.0, END)
        self.text.insert(0.0, content)
        self.text.configure(state='disabled')


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
