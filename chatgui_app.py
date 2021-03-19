import tkinter as tk
import client
import threading 
from tkinter import ttk
from time import strftime

class Gui:
	def __init__(self):
		self.window = tk.Tk()
		self.window.geometry("600x385")
		self.window.maxsize(600, 385)
		self.window.minsize(600, 385)
		self.window.title('  Chat_Room')

		self.p1 = tk.PhotoImage(file = 'python_logo.png')
		self.window.iconphoto(False, self.p1)
		
		self.count = 1
		self.True_msg = []

		self.msg_x = 10
		self.msg_y = 10
		self.msg_send_x = 400

		self.window.rowconfigure(0,weight= 1)
		self.window.columnconfigure(0,weight =1)

		'''self.frame12 = tk.LabelFrame(self.window)
		self.frame12.grid(row = 0,column =0,sticky ='nsew',pady= 40)'''
			

		self.frame1 = tk.Frame(self.window)
		self.frame1.grid(row =0,column =0,sticky ='nsew')

		def clock():
			tme = strftime("%A, %d-%m-%Y\t\t\t\t\t\t\t     %I:%M %p")
			label.config(text=tme)
			label.after(ms=1000,func=clock)
			
		label = tk.Label(self.frame1, width=600, font = ('calibri', 12, 'bold'),background='blue',foreground = 'white',anchor='ne')
		label.pack()
		clock()


		self.frame12 = tk.LabelFrame(self.window,bg = 'cyan')
		self.frame12.grid(row = 0,column =0,sticky ='ew')
		

		self.canvas1f1 = tk.Canvas(self.frame1, width = 600, height = 315, background = 'cyan', relief = 'raised')
		
		self.lbx = tk.Listbox(self.canvas1f1,bg = "white" , fg = "black", height = 18 , width = 96)
		
		self.scrollbar1 =tk.Scrollbar(self.canvas1f1)
		self.scrollbar1.pack(side ='right',fill = 'y')
		self.lbx.config(yscrollcommand = self.scrollbar1.set)
		self.scrollbar1.config(command = self.lbx.yview)

		self.scrollbar1 =tk.Scrollbar(self.canvas1f1, orient = 'horizontal')
		self.scrollbar1.pack(side ='bottom',fill = 'x')
		self.lbx.config(xscrollcommand = self.scrollbar1.set)
		self.scrollbar1.config(command = self.lbx.xview)

		#self.scrollbar2 =tk. Scrollbar(self.canvas1f1,orient = 'horizontal')
		#self.scrollbar1.pack(side ='right',fill = 'y')
		#self.scrollbar2.grid(sticky = "s")
		#self.lbx.config(xscrollcommand = self.scrollbar2.set)
		#self.scrollbar2.config(command = self.lbx.xview)


		self.lbx.pack()
		self.lbx.insert(0, "                               **************************START OF THE CHAT*******************************")
		


		self.canvas1f1.pack()
		self.canvas2f1 = tk.Canvas(self.frame1, width = 600, height = 46, background = 'blue', relief = 'raised')
		self.canvas2f1.pack()

		self.m  = tk.Entry(self.frame1)

		self.canvas2f1.create_window(320, 25, width = 400, height = 20, window=self.m)

		self.button4 = tk.Button(self.frame1, text='Send',bg='light grey', fg='black',font=('helvetica', 9, 'bold'), command = self.send)
		self.canvas2f1.create_window(570, 25, window=self.button4)

		self.frame3 = tk.Frame(self.window)
		self.frame3.grid(row =0,column =0,sticky ='nsew')
		
		#Help window
		def clock0():
			tme = strftime("%A, %d-%m-%Y\t\t\t\t\t\t\t     %I:%M %p")
			label0.config(text=tme)
			label0.after(ms=1000,func=clock0)
		label0 = tk.Label(self.frame3, width=600, font = ('calibri', 12, 'bold'),background='green',foreground = 'white',anchor='ne')
		label0.pack()
		clock0()
	

		self.canvas1f3 = tk.Canvas(self.frame3, width = 600, height = 315, background = 'lime', relief = 'raised')
		self.canvas1f3.pack()
		self.canvas2f3 = tk.Canvas(self.frame3, width = 600, height = 45, background = 'green', relief = 'raised')
		self.canvas2f3.pack()

		self.button_b = tk.Button(self.canvas2f3, text='Back',bg='light grey', fg='black',font=('helvetica', 9, 'bold'), command = self.call_back)
		self.canvas2f3.create_window(570, 20, window=self.button_b)

		word = "  ***To start chatting***  "
		word1 = " Please enter the username you wish to display and click on SUBMIT..."
		word2 = " You will be taken to an interface where you have to enter a unique code\n to either create a room or join one, press the corresponding button to proceed."
		word3 = " This forwards you to the chatting interface where you can enjoy you chatting experience..."
		word4 = " Click on the BACK button in lower right corner to return to the main screen..."
		self.title6 = tk.Label(self.frame3, text = word, bg = 'yellow', borderwidth = 4, relief = 'ridge')
		self.title6.config(font=('helvetica', 11, 'bold'))
		self.canvas1f3.create_window(300, 70, window=self.title6)

		self.title6 = tk.Label(self.frame3, text = word1, borderwidth = 4, relief = 'ridge')
		self.title6.config(font=('helvetica', 11))
		self.canvas1f3.create_window(300, 110, window=self.title6)

		self.title6 = tk.Label(self.frame3, text = word2, borderwidth = 4, relief = 'ridge')
		self.title6.config(font=('helvetica', 11))
		self.canvas1f3.create_window(300, 160, window=self.title6)

		self.title6 = tk.Label(self.frame3, text = word3, borderwidth = 4, relief = 'ridge')
		self.title6.config(font=('helvetica', 11))
		self.canvas1f3.create_window(300, 210, window=self.title6)

		self.title6 = tk.Label(self.frame3, text = word4, borderwidth = 4, relief = 'ridge')
		self.title6.config(font=('helvetica', 11))
		self.canvas1f3.create_window(300, 250, window=self.title6)






		self.frame2 = tk.Frame(self.window)
		self.frame2.grid(row =0,column = 0,sticky ='nsew')
		def clock1():
			tme = strftime("%A, %d-%m-%Y\t\t\t\t\t\t\t     %I:%M %p")
			label1.config(text=tme)
			label1.after(ms=1000,func=clock1)
		
		label1 = tk.Label(self.frame2, width=600, font = ('calibri', 12, 'bold'),background='brown',foreground = 'white',anchor='ne')
		label1.pack()
		clock1()
		

		self.canvas1f2 = tk.Canvas(self.frame2, width = 600, height = 315, background = 'pink', relief = 'raised')
		self.canvas1f2.pack()
		self.canvas2f2 = tk.Canvas(self.frame2, width = 600, height = 45, background = 'brown', relief = 'raised')
		self.canvas2f2.pack()
		
		self.title5 = tk.Label(self.frame2, text='   Enter code:   ', borderwidth = 4, relief = 'ridge')
		self.title5.config(font=('helvetica', 15))
		self.canvas1f2.create_window(300, 70, window=self.title5)
		
		self.code = tk.Entry (self.frame2)
		self.canvas1f2.create_window(300, 110, height = 20, window=self.code)
		self.button1 = tk.Button(self.canvas1f2, text='Create Room', bg='brown', fg='white', font=('helvetica', 9, 'bold'), command = self.create)
		self.canvas1f2.create_window(255, 150, window=self.button1)
		self.button2 = tk.Button(self.canvas1f2, text='Join Room', bg='brown', fg='white', font=('helvetica', 9, 'bold'), command = self.join)
		self.canvas1f2.create_window(345, 150, window=self.button2)


		self.frame0 = tk.Frame(self.window)
		self.frame0.grid(row = 0,column =0,sticky= 'nsew')
		def clock2():
			tme = strftime("%A, %d-%m-%Y\t\t\t\t\t\t\t     %I:%M %p")
			label2.config(text=tme)
			label2.after(ms=1000,func=clock2)
	
		label2 = tk.Label(self.frame0, width=600, font = ('calibri', 12, 'bold'),background='red',foreground = 'white',anchor='ne')
		label2.pack()
		clock2()		

		def emoji():
			a=tk.Toplevel(width=200,height=200)
			canvas_e0=tk.Canvas(a,width=200,height=200,background='white')
			canvas_e0.pack()
			def e1():
				self.m.insert(600,'\U0001f600')
				return
			def e2():
				self.m.insert(600,'\U0001f603')
				return
			def e3():
				self.m.insert(600,'\U0001f604')
				return
			def e4():
				self.m.insert(600,'\U0001f601')
				return
			def e5():
				self.m.insert(600,'\U0001f606')
				return
			def e6():
				self.m.insert(600,'\U0001f605')
				return
			def e7():
				self.m.insert(600,'\U0001f923')
				return
			def e8():
				self.m.insert(600,'\U0001f602')
				return
			def e9():
				self.m.insert(600,'\U0001f642')
				return
			def e10():
				self.m.insert(600,'\U0001f643')
				return
			def e11():
				self.m.insert(600,'\U0001f609')
				return
			def e12():
				self.m.insert(600,'\U0001f60A')
				return
			def e13():
				self.m.insert(600,'\U0001f607')
				return
			def e14():
				self.m.insert(600,'\U0001f60D')
				return
			def e15():
				self.m.insert(600,'\U0001f61C')
				return
			def e16():
				self.m.insert(600,'\U0001f910')
				return
			def e17():
				self.m.insert(600,'\U0001f610')
				return
			def e18():
				self.m.insert(600,'\U0001f611')
				return
			def e19():
				self.m.insert(600,'\U0001f636')
				return
			def e20():
				self.m.insert(600,'\U0001f644')
				return
			def e21():
				self.m.insert(600,'\U0001f62C')
				return
			def e22():
				self.m.insert(600,'\U0001f614')
				return
			def e23():
				self.m.insert(600,'\U0001f912')
				return
			def e24():
				self.m.insert(600,'\U0001f915')
				return
			def e25():
				self.m.insert(600,'\U0001f92F')
				return
			def e26():
				self.m.insert(600,'\U0001f973')
				return
			def e27():
				self.m.insert(600,'\U0001f60E')
				return
			def e28():
				self.m.insert(600,'\U0001f9D0')
				return
			def e29():
				self.m.insert(600,'\U0001f62E')
				return
			def e30():
				self.m.insert(600,'\U0001f628')
				return
			def e31():
				self.m.insert(600,'\U0001f630')
				return
			def e32():
				self.m.insert(600,'\U0001f62D')
				return
			def e33():
				self.m.insert(600,'\U0001f648')
				return
			def e34():
				self.m.insert(600,'\U0001f649')
				return
			def e35():
				self.m.insert(600,'\U0001f64A')
				return
			def e36():
				self.m.insert(600,'\U0001f620')
				return
			def e37():
				self.m.insert(600,'\U0001f624')
				return
			def e38():
				self.m.insert(600,'\U0001f621')
				return
			def e39():
				self.m.insert(600,'\U0001f480')
				return
			def e40():
				self.m.insert(600,'\U0001f47F')
				return


			b1=tk.Button(canvas_e0,text="\U0001f600", bg='white',fg='black',command=e1)
			b2=tk.Button(canvas_e0,text="\U0001f603", bg='white',fg='black',command=e2)
			b3=tk.Button(canvas_e0,text="\U0001f604", bg='white',fg='black',command=e3)
			b4=tk.Button(canvas_e0,text="\U0001f601", bg='white',fg='black',command=e4)
			b5=tk.Button(canvas_e0,text="\U0001f606", bg='white',fg='black',command=e5)
			b6=tk.Button(canvas_e0,text="\U0001f605", bg='white',fg='black',command=e6)
			b7=tk.Button(canvas_e0,text="\U0001f923", bg='white',fg='black',command=e7)
			b8=tk.Button(canvas_e0,text="\U0001f602", bg='white',fg='black',command=e8)
			b9=tk.Button(canvas_e0,text="\U0001f642", bg='white',fg='black',command=e9)
			b10=tk.Button(canvas_e0,text="\U0001f643", bg='white',fg='black',command=e10)
			b11=tk.Button(canvas_e0,text="\U0001f609", bg='white',fg='black',command=e11)
			b12=tk.Button(canvas_e0,text="\U0001f60A", bg='white',fg='black',command=e12)
			b13=tk.Button(canvas_e0,text="\U0001f607", bg='white',fg='black',command=e13)
			b14=tk.Button(canvas_e0,text="\U0001f60D", bg='white',fg='black',command=e14)
			b15=tk.Button(canvas_e0,text="\U0001f61C", bg='white',fg='black',command=e15)
			b16=tk.Button(canvas_e0,text="\U0001f910", bg='white',fg='black',command=e16)
			b17=tk.Button(canvas_e0,text="\U0001f610", bg='white',fg='black',command=e17)
			b18=tk.Button(canvas_e0,text="\U0001f611", bg='white',fg='black',command=e18)
			b19=tk.Button(canvas_e0,text="\U0001f636", bg='white',fg='black',command=e19)
			b20=tk.Button(canvas_e0,text="\U0001f644", bg='white',fg='black',command=e20)
			b21=tk.Button(canvas_e0,text="\U0001f62C", bg='white',fg='black',command=e21)
			b22=tk.Button(canvas_e0,text="\U0001f614", bg='white',fg='black',command=e22)
			b23=tk.Button(canvas_e0,text="\U0001f912", bg='white',fg='black',command=e23)
			b24=tk.Button(canvas_e0,text="\U0001f915", bg='white',fg='black',command=e24)
			b25=tk.Button(canvas_e0,text="\U0001f92F", bg='white',fg='black',command=e25)
			b26=tk.Button(canvas_e0,text="\U0001f973", bg='white',fg='black',command=e26)
			b27=tk.Button(canvas_e0,text="\U0001f60E", bg='white',fg='black',command=e27)
			b28=tk.Button(canvas_e0,text="\U0001f9D0", bg='white',fg='black',command=e28)
			b29=tk.Button(canvas_e0,text="\U0001f62E", bg='white',fg='black',command=e29)
			b30=tk.Button(canvas_e0,text="\U0001f628", bg='white',fg='black',command=e30)
			b31=tk.Button(canvas_e0,text="\U0001f630", bg='white',fg='black',command=e31)
			b32=tk.Button(canvas_e0,text="\U0001f62D", bg='white',fg='black',command=e32)
			b33=tk.Button(canvas_e0,text="\U0001f648", bg='white',fg='black',command=e33)
			b34=tk.Button(canvas_e0,text="\U0001f649", bg='white',fg='black',command=e34)
			b35=tk.Button(canvas_e0,text="\U0001f64A", bg='white',fg='black',command=e35)
			b36=tk.Button(canvas_e0,text="\U0001f620",bg='white',fg='black',command=e36)
			b37=tk.Button(canvas_e0,text='\U0001f624',bg='white',fg='black',command=e37)
			b38=tk.Button(canvas_e0,text='\U0001f621',bg='white',fg='black',command=e38)
			b39=tk.Button(canvas_e0,text='\U0001f480',bg='white',fg='black',command=e39)
			b40=tk.Button(canvas_e0,text='\U0001f47F',bg='white',fg='black',command=e40)
			b1.grid(column=0,row=0)
			b2.grid(column=1,row=0)
			b3.grid(column=2,row=0)
			b4.grid(column=3,row=0)
			b5.grid(column=4,row=0)
			b6.grid(column=5,row=0)
			b7.grid(column=6,row=0)
			b8.grid(column=7,row=0)
			b9.grid(column=0,row=1)
			b10.grid(column=1,row=1)
			b11.grid(column=2,row=1)
			b12.grid(column=3,row=1)
			b13.grid(column=4,row=1)
			b14.grid(column=5,row=1)
			b15.grid(column=6,row=1)
			b16.grid(column=7,row=1)
			b17.grid(column=0,row=2)
			b18.grid(column=1,row=2)
			b19.grid(column=2,row=2)
			b20.grid(column=3,row=2)
			b21.grid(column=4,row=2)
			b22.grid(column=5,row=2)
			b23.grid(column=6,row=2)
			b24.grid(column=7,row=2)
			b25.grid(column=0,row=3)
			b26.grid(column=1,row=3)
			b27.grid(column=2,row=3)
			b28.grid(column=3,row=3)
			b29.grid(column=4,row=3)
			b30.grid(column=5,row=3)
			b31.grid(column=6,row=3)
			b32.grid(column=7,row=3)
			b33.grid(column=0,row=4)
			b34.grid(column=1,row=4)
			b35.grid(column=2,row=4)
			b36.grid(column=3,row=4)
			b37.grid(column=4,row=4)
			b38.grid(column=5,row=4)
			b39.grid(column=6,row=4)
			b40.grid(column=7,row=4)
		self.canvas1f0 = tk.Canvas(self.frame0, width = 600, height = 315, background = 'orange', relief = 'raised')
		self.canvas1f0.pack()
		self.canvas2f0 = tk.Canvas(self.frame0 , width = 600, height = 45, background = 'red', relief = 'raised')
		
		self.button0=tk.Button(self.frame1,text='Emoji',bg='yellow',fg='black',font=('helvetica', 9, 'bold'),command=emoji)
		self.canvas2f1.create_window(35,25,window=self.button0)
		self.canvas2f0.pack()

		self.label1 = tk.Label(self.frame0, text=" Welcome to Chat Room ", bg = "yellow", borderwidth = 3, relief = 'ridge', padx=20)
		self.label1.config(font=('colonna mt', 25))
		self.canvas1f0.create_window(300, 70, window=self.label1)

		self.title4 = tk.Label(self.frame0, text='   Enter your Name:   ', borderwidth = 4, relief = 'ridge')
		self.title4.config(font=('helvetica', 15))
		self.canvas1f0.create_window(300, 140, window=self.title4)
		
		self.name = tk.Entry(self.frame0)
		self.canvas1f0.create_window(300, 180, width = 150, height = 20, window=self.name)
		
		self.button1 = tk.Button(self.frame0, text='Submit', bg='brown', fg='white', font=('helvetica', 9, 'bold'), command = self.ask_name)
		self.canvas1f0.create_window(300, 220, window=self.button1)

		self.button3 = tk.Button(self.frame0, text='Help',bg='light grey', fg='black',font=('helvetica', 9, 'bold'), command = self.call_help1)
		self.canvas2f0.create_window(570, 20, window=self.button3)

		self.client = client.Client()

		
	def ask_name(self):
		self.n = self.name.get()
		self.client.name = self.n
		self.client.ask_name()
		self.frame2.tkraise()
		
	def call_help1(self):
		self.frame3.tkraise()

	def call_back(self):
		self.frame0.tkraise()


	def join(self):
		self.c = str(self.code.get())
		
		self.client.ask_room(2,self.c)
		self.make_thread()	
		
		self.frame1.tkraise()


	def create(self):
		self.c = str(self.code.get())

		print(type(self.c))
		
		self.client.ask_room(1,self.c)
		self.make_thread()

		self.frame1.tkraise()


	def send(self):
		msg = self.m.get()
		self.m.delete(0,'end')
		print(msg)
		self.client.send_msg(str(msg))
		p = str(strftime("%I:%M %p"))
		self.lbx.insert("end",p+"  "+"you: " + str(msg))
 

	def show_msg(self):
		self.l = self.client.msg[len(self.client.msg)-1]
		p = str(strftime("%I:%M %p"))
		self.lbx.insert("end",p+"  "+str(self.l))
		self.count += 1


	def auto_refresh(self):
		while True:
			if(self.count == len(self.client.msg)):
				self.show_msg()


	def make_thread(self):
		self.client.make_thread()


	def main_loop(self):
		self.window.mainloop()



	def make_threads(self):
		self.t1 = threading.Thread(target = self.auto_refresh)
		self.t1.start()


G = Gui()
G.make_threads()
G.main_loop()