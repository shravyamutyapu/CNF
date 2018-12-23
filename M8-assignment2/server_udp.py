"""socket has to be imported"""
import socket
 #currency conversion
def conversion(data):
	# tokenize the data then convert
	tokens = data.split(" ")
	"""for example , i/p :
	FROM INR 67 To Dollar
	here INR is in index 1
	Dollar in index 4
	67 is converted to USD """
	if (tokens[1] == "INR"):
		# the following are the respective formulae.
		if (tokens[4] == "Dollar"):
			return (int(tokens[2]) / 67)
		if (tokens[4] == "Pounds"):
			return (int(tokens[2]) * 0.75) / 67
		if (tokens[4] == "Yen"):
			return (int(tokens[2]) * 113.41) / 67
	#converion of USD to other currencies
	if (tokens[1] == "Dollar"):
		if (tokens[4] == "INR"):
			return (int(tokens[2]) * 67)
		if (tokens[4] == "Pounds"):
			return (int(tokens[2]) * 0.75)
		if (tokens[4] == "Yen"):
			return (int(tokens[2]) * 113.41)
	#converion of pounds to other currencies
	if (tokens[1] == "Pounds"):
		if (tokens[4] == "INR"):
			return (int(tokens[2]) * 67) / 0.75
		if (tokens[4] == "Dollar"):
			return (int(tokens[2]) / 0.75)
		if (tokens[4] == "Yen"):
			return (int(tokens[2]) * 113.41) / 0.75
	#converion of Yen to other currencies
	if (tokens[1] == "Yen"):
		if (tokens[4] == "INR"):
			return (int(tokens[2]) * 67) / 113.41
		if (tokens[4] == "Dollar"):
			return (int(tokens[2]) / 113.41)
		if (tokens[4] == "Pounds"):
			return (int(tokens[2]) * 0.75) / 113.41

def main():

	host = '127.0.0.1'
	port = 5000
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host,port))
	print ("server started")
	while True:
		data, addr = s.recvfrom(1024)
		print("message from " + str(addr))
		print("from connect user " + str(data))
		message = conversion(data.decode())
		print("sending " + str(message))
		s.sendto(str(message).encode(), addr)
	s.close()

if __name__ == '__main__':
	main()