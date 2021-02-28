from tkinter import *

def GUI2(Frame):    
    Frame.geometry("600x360")
    Frame.maxsize(600, 360)
    Frame.minsize(600, 360)

    canvas3 = Canvas(Frame, width = 600, height = 315, background = 'pink', relief = 'raised')
    canvas3.pack()

    canvas4 = Canvas(Frame, width = 600, height = 45, background = 'brown', relief = 'raised')
    canvas4.pack()
