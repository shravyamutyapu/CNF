import socket

def main():
	host = '127.0.0.1'
	port = 5000
	s = socket.socket()

	message = input("->")
	while message != 'q':
		s.send(message)
		data = s.rcv(1024)
		print("Recieved from server: " +str(data))
		message = input("->")
	s.close()
if __name__ == '__main__':
	main()

