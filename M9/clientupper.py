"""socket has to be imported"""
import socket

def Main():
    host = '192.168.1.11'
    port = 5001
    #client flag
    client = True
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    """connect accepts only one argument
    so host and port are given as tuple """
    s.connect((host, port))

    print("Connected")
    message = input("Enter your guess: Q for abort")
    while message != 'Q':

        s.send(message.encode())
        data = s.recv(1024).decode()
        #print recieved data
        print("Received" + str(data))
        value = data.split()
        if (value[0] == 'Correct' or value[0] == 'q'):
            s.send('Q'.encode())
            break
        message = input("-> ")
        #socket closing
    s.close()
if __name__ == '__main__':
    Main()