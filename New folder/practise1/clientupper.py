import socket

def main():
	host = "10.10.9.44"
	port = 3128

	scket = socket.socket()
	scket.connect((host, port))

	message = input("->")
	while message != 'q':
		scket.send(message.encode())
		data = scket.recv(1024).decode()
		print("Received from server " + data)
		message = input("->")
	socket.close()


if __name__ == '__main__':
	main()