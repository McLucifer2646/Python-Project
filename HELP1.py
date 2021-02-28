#import tkinter as tk
from tkinter import *

def GUI1(Frame):    
    Frame.geometry("600x360")
    Frame.maxsize(600, 360)
    Frame.minsize(600, 360)
    canvas2 = Canvas(Frame, width = 600, height = 360, background = 'light grey', relief = 'raised')
    canvas2.pack()
    #label = tk.Label(Frame, text="About Create Room", bg = 'blue', fg ='white', borderwidth = 6, relief = 'sunken')
    #label.pack(padx=20, pady=20)
    title2 = Label(Frame, text=' HELP!! ', borderwidth = 4, relief = 'raised')
    title2.config(font=('helvetica', 10))
    canvas2.create_window(300, 25, window=title2)
    return

if __name__ == "__main__":
    h = Tk()
    GUI1(h)
    h.mainloop()

    