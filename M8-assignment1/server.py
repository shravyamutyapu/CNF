"""socket has to be imported"""
import socket
 #currency conversion
def conversion(data):
	# tokenize the data then convert
	tokens = data.split()
	"""for example , i/p :
	FROM INR 67 To Dollar
	here INR is in index 1
	Dollar in index 4
	67 is converted to USD """
	if (tokens[1] == "INR"):
		# the following are the respective formulae.
		if (tokens[4] == "Dollar"):
			return (int(tokens[2]) / 67)
		elif (tokens[4] == "Pounds"):
			return (int(tokens[2]) * 0.75) / 67
		elif (tokens[4] == "Yen"):
			return (int(tokens[2]) * 113.41) / 67
	#converion of USD to other currencies
	if (tokens[1] == "Dollar"):
		#the following are respective formulae
		if (tokens[4] == "INR"):
			return (int(tokens[2]) * 67)
		elif (tokens[4] == "Pounds"):
			return (int(tokens[2]) * 0.75)
		elif (tokens[4] == "Yen"):
			return (int(tokens[2]) * 113.41)
	#converion of pounds to other currencies
	if (tokens[1] == "Pounds"):
		#the following are respective formulae
		if (tokens[4] == "INR"):
			return (int(tokens[2]) * 67) / 0.75
		if (tokens[4] == "Dollar"):
			return (int(tokens[2]) / 0.75)
		if (tokens[4] == "Yen"):
			return (int(tokens[2]) * 113.41) / 0.75
	#converion of yen to other currencies
	if (tokens[1] == "Yen"):
		#the following are respective formulae
		if (tokens[4] == "INR"):
			return (int(tokens[2]) * 67) / 113.41
		if (tokens[4] == "Dollar"):
			return (int(tokens[2]) / 113.41)
		if (tokens[4] == "Pounds"):
			return (int(tokens[2]) * 0.75) / 113.41
# main function
def main():
	host = "127.0.0.1"
	#our port number
	port = 5000
    # socket creation
	s = socket.socket()
	"""bind accepts only one argument
	so host and port are given as tuple """
	s.bind((host, port))
	"""listens to one client"""
	s.listen(1)
	#accepting connection c and address addr
	c, addr = s.accept()

	print("Connection from " + str(addr))
	while True:
		data = c.recv(1024).decode()
		#if there is no data just break
		if not data:
			break
		#printing data
		print("from connected user " + str(data))

		data = str(conversion(data))
		print ("sending: " + str(data))
		c.send(data.encode())
		#connection is closed
	c.close()


if __name__ == '__main__':
	main()