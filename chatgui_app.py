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
			a=tk.Toplevel(width=350,height=200)
			canvas_e0=tk.Canvas(a,width=350,height=200,background='white')
			a.maxsize(350,200)
			a.minsize(350,200)
			canvas_e0.pack()
			def e1():
				self.m.insert(600,'\U0001f600')
				return
			def e2():
				self.m.insert(600,'\U0001f4AF')
				return
			def e3():
				self.m.insert(600,'\U0001f604')
				return
			def e4():
				self.m.insert(600,'\U0001f64F')
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


			self.b1=tk.Button(canvas_e0,text="\U0001f600", bg='white',fg='black',font=10,command=e1)
			self.b2=tk.Button(canvas_e0,text="\U0001f4AF", bg='white',fg='black',font=10,command=e2)
			self.b3=tk.Button(canvas_e0,text="\U0001f604", bg='white',fg='black',font=10,command=e3)
			self.b4=tk.Button(canvas_e0,text="\U0001f64F", bg='white',fg='black',font=10,command=e4)
			self.b5=tk.Button(canvas_e0,text="\U0001f606", bg='white',fg='black',font=10,command=e5)
			self.b6=tk.Button(canvas_e0,text="\U0001f605", bg='white',fg='black',font=10,command=e6)
			self.b7=tk.Button(canvas_e0,text="\U0001f923", bg='white',fg='black',font=10,command=e7)
			self.b8=tk.Button(canvas_e0,text="\U0001f602", bg='white',fg='black',font=10,command=e8)
			self.b9=tk.Button(canvas_e0,text="\U0001f642", bg='white',fg='black',font=10,command=e9)
			self.b10=tk.Button(canvas_e0,text="\U0001f643", bg='white',fg='black',font=10,command=e10)
			self.b11=tk.Button(canvas_e0,text="\U0001f609", bg='white',fg='black',font=10,command=e11)
			self.b12=tk.Button(canvas_e0,text="\U0001f60A", bg='white',fg='black',font=10,command=e12)
			self.b13=tk.Button(canvas_e0,text="\U0001f607", bg='white',fg='black',font=10,command=e13)
			self.b14=tk.Button(canvas_e0,text="\U0001f60D", bg='white',fg='black',font=10,command=e14)
			self.b15=tk.Button(canvas_e0,text="\U0001f61C", bg='white',fg='black',font=10,command=e15)
			self.b16=tk.Button(canvas_e0,text="\U0001f910", bg='white',fg='black',font=10,command=e16)
			self.b17=tk.Button(canvas_e0,text="\U0001f610", bg='white',fg='black',font=10,command=e17)
			self.b18=tk.Button(canvas_e0,text="\U0001f611", bg='white',fg='black',font=10,command=e18)
			self.b19=tk.Button(canvas_e0,text="\U0001f636", bg='white',fg='black',font=10,command=e19)
			self.b20=tk.Button(canvas_e0,text="\U0001f644", bg='white',fg='black',font=10,command=e20)
			self.b21=tk.Button(canvas_e0,text="\U0001f62C", bg='white',fg='black',font=10,command=e21)
			self.b21=tk.Button(canvas_e0,text="\U0001f62C", bg='white',fg='black',font=10,command=e21)
			self.b21=tk.Button(canvas_e0,text="\U0001f62C", bg='white',fg='black',font=10,command=e21)
			self.b22=tk.Button(canvas_e0,text="\U0001f614", bg='white',fg='black',font=10,command=e22)
			self.b23=tk.Button(canvas_e0,text="\U0001f912", bg='white',fg='black',font=10,command=e23)
			self.b24=tk.Button(canvas_e0,text="\U0001f915", bg='white',fg='black',font=10,command=e24)
			self.b25=tk.Button(canvas_e0,text="\U0001f92F", bg='white',fg='black',font=10,command=e25)
			self.b26=tk.Button(canvas_e0,text="\U0001f973", bg='white',fg='black',font=10,command=e26)
			self.b27=tk.Button(canvas_e0,text="\U0001f60E", bg='white',fg='black',font=10,command=e27)
			self.b28=tk.Button(canvas_e0,text="\U0001f9D0", bg='white',fg='black',font=10,command=e28)
			self.b29=tk.Button(canvas_e0,text="\U0001f62E", bg='white',fg='black',font=10,command=e29)
			self.b30=tk.Button(canvas_e0,text="\U0001f628", bg='white',fg='black',font=10,command=e30)
			self.b31=tk.Button(canvas_e0,text="\U0001f630", bg='white',fg='black',font=10,command=e31)
			self.b32=tk.Button(canvas_e0,text="\U0001f62D", bg='white',fg='black',font=10,command=e32)
			self.b33=tk.Button(canvas_e0,text="\U0001f648", bg='white',fg='black',font=10,command=e33)
			self.b34=tk.Button(canvas_e0,text="\U0001f649", bg='white',fg='black',font=10,command=e34)
			self.b35=tk.Button(canvas_e0,text="\U0001f64A", bg='white',fg='black',font=10,command=e35)
			self.b36=tk.Button(canvas_e0,text="\U0001f620",bg='white',fg='black',font=10,command=e36)
			self.b37=tk.Button(canvas_e0,text='\U0001f624',bg='white',fg='black',font=10,command=e37)
			self.b38=tk.Button(canvas_e0,text='\U0001f621',bg='white',fg='black',font=10,command=e38)
			self.b39=tk.Button(canvas_e0,text='\U0001f480',bg='white',fg='black',font=10,command=e39)
			self.b40=tk.Button(canvas_e0,text='\U0001f47F',bg='white',fg='black',font=10,command=e40)
			self.b1.grid(column=0,row=0)
			self.b2.grid(column=1,row=0)
			self.b3.grid(column=2,row=0)
			self.b4.grid(column=3,row=0)
			self.b5.grid(column=4,row=0)
			self.b6.grid(column=5,row=0)
			self.b7.grid(column=6,row=0)
			self.b8.grid(column=7,row=0)
			self.b9.grid(column=0,row=1)
			self.b10.grid(column=1,row=1)
			self.b11.grid(column=2,row=1)
			self.b12.grid(column=3,row=1)
			self.b13.grid(column=4,row=1)
			self.b14.grid(column=5,row=1)
			self.b15.grid(column=6,row=1)
			self.b16.grid(column=7,row=1)
			self.b17.grid(column=0,row=2)
			self.b18.grid(column=1,row=2)
			self.b19.grid(column=2,row=2)
			self.b20.grid(column=3,row=2)
			self.b21.grid(column=4,row=2)
			self.b22.grid(column=5,row=2)
			self.b23.grid(column=6,row=2)
			self.b24.grid(column=7,row=2)
			self.b25.grid(column=0,row=3)
			self.b26.grid(column=1,row=3)
			self.b27.grid(column=2,row=3)
			self.b28.grid(column=3,row=3)
			self.b29.grid(column=4,row=3)
			self.b30.grid(column=5,row=3)
			self.b31.grid(column=6,row=3)
			self.b32.grid(column=7,row=3)
			self.b33.grid(column=0,row=4)
			self.b34.grid(column=1,row=4)
			self.b35.grid(column=2,row=4)
			self.b36.grid(column=3,row=4)
			self.b37.grid(column=4,row=4)
			self.b38.grid(column=5,row=4)
			self.b39.grid(column=6,row=4)
			self.b40.grid(column=7,row=4)
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