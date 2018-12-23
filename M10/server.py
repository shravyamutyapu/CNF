import socket
import threading

def clients_handle(client,username):
    client1 = True
    keys = clients.keys()
    help = "1)**broadcast -Broadcasting your message.2) **username -Personal Chat.3)**quit in msg"
    while client1:
        try:
            msg = client.recv(1024).decode('ascii')
            if('**broadcast' in msg):
                msg = msg.replace('**broadcast','')
                for k,v in clients.items():
                    v.send(msg.encode('ascii'))
            elif('**help' in msg):
                client.send(help.encode('ascii'))
            elif('**quit' in msg):
                clients.pop(username)
                message = str(username) + 'Logged Out'
                client.send(message.encode('ascii'))
                client1 = False
            else:
                for name in keys:
                    if('**'+name in msg):
                        msg = msg.replace('**'+name,'')
                        clients.get(name).send(msg.encode())
                        found = True
                    elif(not found):
                        message1 = 'You entered an invalid person'
                        client.send(message1.encode('ascii'))
        except:
            clients.pop(username)
            print(str(username) + "logged out")
            client1 = False

if __name__ == '__main__':
    s =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server = True
    host1 = socket.gethostname()
    port = 5000
    clients = {}
    host = socket.gethostbyname(host1)
    s.bind((host,port))
    print("Server start")
    print("IP address of the server::%s"%host)
    s.listen(10)
    while server:
        client, addr = s.accept()
        username = client.recv(1024).decode('ascii')
        print("connected to the server" + str(username))
        client.send("Welcome to chat press **help for help".encode('ascii'))
        if(client not in clients):
            clients[username] = client
            threading.Thread(target = clients_handle, args = (client,username,)).start()