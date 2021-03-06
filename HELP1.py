import tkinter as tk
from time import strftime


def GUI1(Frame):
    
   
    Frame.geometry("733x434")
    Frame.maxsize(733,434)
    Frame.minsize(733,434)
    Frame.title("***HELP***")

    def clock():
        tme = strftime("%A, %d-%m-%Y\t\t\t\t\t\t\t\t     %H:%M %p")
        label.config(text=tme) 
        label.after(1000, clock) 

    label = tk.Label(Frame,width=600, font = ('calibri', 12, 'bold'),background='red',foreground = 'white',anchor='ne')
    label.pack()
    clock()


    canvash = tk.Canvas(Frame,width=733,height=434,background="cyan")
    canvash.pack()
    label1 = tk.Label(Frame,text="About createroom!",font="comicsansms",bg="blue",fg="white",padx=250,pady=6,borderwidth=6,relief='ridge')
    label1.pack(fill='x',padx=200,pady=100)
    canvash.create_window(360,120,window = label1)
    label2 = tk.Label(Frame,text="About join room!",font = "comicsansms",bg="blue",fg="white",padx=250,pady=6,borderwidth=6,relief='ridge')
    label2.pack(fill='x',padx=200)
    canvash.create_window(360,240,window = label2)
    return
    
if __name__ == "__main__":
    hsc = tk.Tk()
    GUI1(hsc)
    hsc.mainloop()


