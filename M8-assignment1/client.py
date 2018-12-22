"""socket has to be imported"""
import socket

def main():
	host = "127.0.0.1"
	port = 5000
    # s is socket object
	s = socket.socket()
	"""connect accepts only one argument
	so host and port are given as tuple """
	s.connect((host, port))
    #message takes input
	message = input("->")
	# if message is q then quit
	while message != 'q':
		s.send(message.encode())
		#recieve a max of 1024 bytes
		data = s.recv(1024).decode()
		# prints data that is recieved
		print("Received from server " + data)
		message = input("->")
		#socket is closed
	socket.close()


if __name__ == '__main__':
	main()