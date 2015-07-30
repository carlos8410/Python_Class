"""Write a GUI-based program that provides two Entry fields, a button and a label.
When the button is clicked, the value of each Entry should (if possible) be converted into a float.
If both conversions succeed, the label should change to the sum of the two numbers.
Otherwise it should read "***ERROR***."""


from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        top_frame = Frame(self)
        top_frame.pack(side=TOP)
        self.entry_1 = Entry(top_frame)
        self.entry_2 = Entry(top_frame)
        self.entry_1.pack(side=LEFT)
        self.entry_2.pack(side=LEFT)

        bottom_frame = Frame(self)
        bottom_frame.pack(side=TOP)
        Button(bottom_frame, text='Summation', command=self.handle).pack(side=LEFT)
        self.label = Label(bottom_frame)
        self.label.pack(side=LEFT)

    def handle(self):
        """Handle a click of the button by converting the text the
        user has placed in the two Entry widgets and summing them
        to show in the label"""
        print ("hanler")
        entry_1 = self.entry_1.get()
        entry_2 = self.entry_2.get()
        try:
            output = float(entry_1) + float(entry_2)
        except:
            output = "***ERROR***"
        self.label.config(text=output)


root = Tk()
app = Application(master=root)
app.mainloop()
#app.destroy()
