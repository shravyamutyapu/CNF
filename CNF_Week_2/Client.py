import socket

def main():
    host = "127.0.0.1"
    port = 3128
    s = socket.socket()
    s.connect((host, port))
    while True:
        data = s.recv(1024).decode()
        data = str(data)
        print(data)
        if "-" in data:
            tokens = str(data).split("-")
            if tokens[1] in ["SUCCESS", "NOTFOUND", "Syntax"]:
                break
        inp = input().encode()
        s.send(inp)
    s.close()

if __name__ == '__main__':
    main()