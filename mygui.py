from tkinter import *
import HELP1
import chat_room

class gui:
    
    def __init__(self):
        self.root= Tk()
        self.root.geometry("600x360")
        self.root.maxsize(600, 360)
        self.root.minsize(600, 360)

        namevalue = StringVar()
        hcodevalue = StringVar()
        Gcodevalue = StringVar()

        self.canvas1 = Canvas(self.root, width = 600, height = 315, background = 'orange', relief = 'raised')
        self.canvas1.pack()
        self.canvas2 = Canvas(self.root, width = 600, height = 45, background = 'red', relief = 'raised')
        self.canvas2.pack()

        self.label1 = Label(self.root, text="IIIT B Chat Room", bg = "yellow", borderwidth = 3, relief = 'ridge', padx=20)
        self.label1.config(font=('colonna mt', 25))
        self.canvas1.create_window(300, 40, window=self.label1)

        #self.title2 = Label(self.root, text=' Host Code: ', borderwidth = 4, relief = 'ridge')
        #self.title2.config(font=('helvetica', 15))
        #self.canvas1.create_window(200, 200, window=self.title2)

        self.title3 = Label(self.root, text=' Guest Code: ', borderwidth = 4, relief = 'ridge')
        self.title3.config(font=('helvetica', 15))
        self.canvas1.create_window(300, 200, window=self.title3)

        self.title4 = Label(self.root, text='   Enter your Name:   ', borderwidth = 4, relief = 'ridge')
        self.title4.config(font=('helvetica', 15))
        self.canvas1.create_window(300, 110, window=self.title4)

        self.entry3 = Entry (self.root, textvariable = namevalue) 
        self.canvas1.create_window(300, 150, width = 150, height = 20, window=self.entry3)

        #self.entry1 = Entry (self.root, textvariable = hcodevalue) 
        #self.canvas1.create_window(200, 240, height = 20, window=self.entry1)

        self.entry2 = Entry (self.root, textvariable = Gcodevalue) 
        self.canvas1.create_window(300, 240, height = 20, window=self.entry2)

        def call_GUI2():
            if (self.entry2 == "" or self.entry3 == ""):
                print("Please enter a value")
            else:
                win1 = Toplevel(self.root)
                chat_room.GUI2(win1)
            return

        self.button1 = Button(text='Create Room', bg='brown', fg='white', font=('helvetica', 9, 'bold'), command = call_GUI2)
        self.canvas1.create_window(255, 280, window=self.button1)

        self.button2 = Button(text='Join Room', bg='brown', fg='white', font=('helvetica', 9, 'bold'), command = call_GUI2)
        self.canvas1.create_window(345, 280, window=self.button2)        

        def call_GUI1():
            win1 = Toplevel(self.root)
            HELP1.GUI1(win1)
            return
        
        self.button3 = Button(text='Help',bg='light grey', fg='black',font=('helvetica', 9, 'bold'), command = call_GUI1)
        self.canvas2.create_window(570, 20, window=self.button3)

        self.root.mainloop()    
            
c = gui()