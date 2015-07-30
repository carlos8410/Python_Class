__author__ = 'zwx'

from tkinter import *
from tkinter.messagebox import showerror

def colorgen():
    while True:
        yield "red"
        yield "yellow"
        yield "Green"

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

        self.columnconfigure(1, weight=1)
        Button(self, text="Red", command=self.set_font_color("Red")).grid(row=3, column=1, sticky=E+W)

        self.columnconfigure(2, weight=1)
        Button(self, text="Blue", command=self.set_font_color("Blue")).grid(row=3, column=2, sticky=E+W)



        frame3 = Frame(self)
        frame3.grid(row=1, column=3, rowspan=2, columnspan=3, sticky=ALL)

        self.entry = Entry(frame3)
        self.entry.pack(side=TOP, fill=BOTH, expand=True)
        
        self.text = Text(frame3, wrap=WORD)
        self.text.pack(side=TOP, fill=BOTH, expand=True)


        self.columnconfigure(3, weight=1)
        Button(self, text="Green", command=self.set_font_color("Green")).grid(row=3, column=3, sticky=E+W)

        self.columnconfigure(4, weight=1)
        Button(self, text="Black", command=self.set_font_color("Black")).grid(row=3, column=4, sticky=E+W)

        self.columnconfigure(5, weight=1)
        Button(self, text="Open", command=self.open_handler).grid(row=3, column=5, sticky=E+W)



    def set_font_color(self, color):
        #self.text.configure(fg=color)
        pass


    def handler_Frame_1_2(self, event, frame_num):
        print ('Frame clicked at %s, %s on Frame %s' % (event.x, event.y, frame_num))


    def open_handler(self):
        """Handle a click of the Open button by reading the text the
        user has placed in the Entry widget and use it as the file
        name to open."""
        file_path = self.entry.get()
        try:
            file = open(file_path, 'r')
        except:
            print("error", showerror("Error", "***Cannot open the file: %s ***" % file_path))
            return
        try:
            content = file.read()
            print ("content=", content)
        except:
            print("error", showerror("Error", "***Cannot read the file: %s ***" % file_path))
            return

        self.text.configure(state='normal')
        self.text.delete(0.0, END)
        self.text.insert(END, content)
        self.text.configure(state='disabled')


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
