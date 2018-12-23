import socket

def main():

	host = '127.0.0.1'
	port = 5000
	#socket obj
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host,port))
	message = input("->")
	while message != 'q':
		s.sendto(str(message).encode(), ('127.0.0.1',5000))
		data, addr = s.recvfrom(1024)
		print("recieved from server: " + str(data.decode()))
		message = input("->")
	s.close()

if __name__ == '__main__':
	main()