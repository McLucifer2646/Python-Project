import socket
import threading
import time

class Client:
	def __init__(self):
		self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.server_ip = "127.0.0.1"
		self.Format = 'utf-8'
		print(self.server_ip)
		self.client.connect((self.server_ip,9999))



	def ask_name(self):
		self.name = input("enter your name  : ")
		self.send = self.name
		self.client.send(self.send.encode(self.Format))


	def ask_room(self):
		choice = input("press 1 for creating room and 2 for joining room")

		if(choice == '1'):
			self.room_number = input("enter room number ")
			header = "header:1"
			self.client.send(header.encode(self.Format))
			time.sleep(0.1)
			self.client.send(self.room_number.encode('utf-8'))

		elif(choice == '2'):
			self.room_number = input("enter room number")
			header = "header:2"
			self.client.send(header.encode(self.Format))
			time.sleep(0.1)
			self.client.send(self.room_number.encode('utf-8'))

		value = self.client.recv(1024).decode('utf-8')
		print(type(value))
		print(value)

		if((choice == '1') and (value == '0')):
			print("room alredy exists")
			print("enter valid code")
			

		elif((choice == '2') and (value == '0')):
			print("room does not exists")
			print("enter_valid code")
			
			

		if((choice == '1') and (value == '1')):
			print(f"sucessfully created the room: {self.room_number}")

		elif((choice == '2') and (value == '1')):
			print(f"successfully entered the room {self.room_number}")




	def send_msg(self):
		while True:
			msg = input("msg>")
			self.client.send(msg.encode(self.Format))


	def recv_msg(self):
		while True:
			msg = self.client.recv(1024).decode(self.Format)
			if(len(msg)>0):
				print(f"{msg}")



	def make_thread(self):

		self.thread1 = threading.Thread(target = self.recv_msg)

		self.thread1.start()

		self.thread2 = threading.Thread(target = self.send_msg)

		self.thread2.start()


	def main_loop(self):
		self.ask_name()
		self.ask_room()
		self.make_thread()




c = Client()
c.main_loop()





