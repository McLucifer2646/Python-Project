import socket
import threading
import time


class Server:
	def __init__(self):
		self.soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.addr = "127.0.0.1"
		self.clients = []
		self.rooms = []
		self.soc.bind((self.addr,9999))



	def recv_name(self,conn,addr):
		name = conn.recv(1024).decode('utf-8')
		return name



	def recv_room(self,conn,addr):
		name = self.recv_name(conn,addr)
		val1 = '0'
		val2 = '1'

		create_or_join = conn.recv(1024).decode('utf-8')
		print(create_or_join)
		if(create_or_join == "header:1"):
			room_code = conn.recv(1024).decode('utf-8')
			print(room_code)
			if room_code in self.rooms:
				conn.send(val1.encode('utf-8'))
			else:
				conn.send(val2.encode('utf-8'))
				self.rooms.append(room_code)
				self.clients.append([conn,room_code,name])

		elif(create_or_join == "header:2"):
			room_code = conn.recv(1024).decode('utf-8')
			if room_code in self.rooms:
				conn.send(val2.encode('utf-8'))
				self.clients.append([conn,room_code,name])
			else:
				conn.send(val1.encode('utf-8'))




	def recv_msg_and_broadcast(self,conn,addr):
		self.recv_room(conn,addr)
		room_code = 1 
		name = ""
		while True:
			msg = conn.recv(1024).decode('utf-8')

			for i in self.clients:
				if i[0] == conn:
					room_code = i[1]
					name = i[2]
					break


			msg_to_send = name+":"+msg

			if(len(msg)>0):
				for client in self.clients:
					if((client[0] != conn) and (client[1] == room_code)):
						print("forwording __ msg")
						client[0].send(msg_to_send.encode('utf-8'))




	def main_server_loop(self):
		self.soc.listen()
		while True:
			conn,add = self.soc.accept()

			self.thread2 = threading.Thread(target = self.recv_msg_and_broadcast, args = (conn,add))
			self.thread2.start()

			




s = Server()
s.main_server_loop()

