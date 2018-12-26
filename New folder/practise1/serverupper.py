import socket

def main():
	host = "10.10.9.44"
	port = 3128

	scket = socket.socket()
	scket.bind((host, port))

	scket.listen(1)
	conn, addr = scket.accept()
	print("Connection from " + str(addr))
	while True:
		data = conn.recv(1024).decode()
		if not data:
			break
		print("from connected user " + str(data))

		data = str(data).upper()
		print ("sending: " + str(data))
		conn.send(data.encode())
	conn.close()


if __name__ == '__main__':
	main()