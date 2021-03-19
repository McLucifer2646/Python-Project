import socket
import threading
import time


class Client:
	def __init__(self):
		self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.server_ip = "3.131.207.170"
		self.Format = 'utf-8'
		self.msg = []
		self.prev_msg = []
		self.know = True
		print(self.server_ip)
		try:
			self.client.connect((self.server_ip,13865))
		except Exception as e:
			print("server not available")
		
		self.is_recv = False



	def ask_name(self):
		self.send = self.name
		self.client.send(self.send.encode(self.Format))


	def ask_room(self,code,value_room):
		choice = int(code)
		val = value_room

		print(choice,value_room)

		if(choice == 1):
			print("infor")
			self.room_number = value_room
			header = "header:1"
			self.client.send(header.encode(self.Format))
			time.sleep(0.1)
			self.client.send(self.room_number.encode('utf-8'))
			print("end for")

		elif(choice == 2):
			self.room_number = value_room
			header = "header:2"
			self.client.send(header.encode(self.Format))
			time.sleep(0.1)
			self.client.send(self.room_number.encode('utf-8'))

		else:
			print("Not any thing")

		value = self.client.recv(1024).decode('utf-8')
		#print(type(value))
		print(value)

		if((choice == 1) and (value == '0')):
			print("room alredy exists")
			print("enter valid code")
			

		elif((choice == 2) and (value == '0')):
			print("room does not exists")
			print("enter_valid code")
			
			

		if((choice == 1) and (value == '1')):
			print(f"sucessfully created the room: {self.room_number}")

		elif((choice == 2) and (value == '1')):
			print(f"successfully entered the room {self.room_number}")




	def send_msg(self,msg):
		self.client.send(msg.encode(self.Format))



	def recv_msg(self):
		while True:
			msg = self.client.recv(1024).decode(self.Format)
			if(len(msg)>0):
				for i in self.msg:
					self.prev_msg  = i
				self.msg.append(msg)
				self.know = True
				print(f"{msg}")



	def make_thread(self):
		self.thread1 = threading.Thread(target = self.recv_msg)
		self.thread1.start()
