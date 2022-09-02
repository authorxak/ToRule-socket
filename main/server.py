import socket, webbrowser, os

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((f'{socket.gethostbyname_ex(socket.gethostname())[2][0]}',4040))
print(f'SERVER STARTED...\nIP: {socket.gethostbyname_ex(socket.gethostname())[2][0]}')
server.listen()
is_work=True

def start_server():
    global is_work
    while is_work:
        usr, addr = server.accept()
        print(f'<<<--------------------------->>>\nUSER CONNECTED!\nIP: {addr[0]}\nPORT: {addr[1]}\n<<<--------------------------->>>')
        while is_work:
            data=usr.recv(2048).decode("utf-8").lower()
            print(data)
            if data=="close":
                usr.send("SERVER DISCONNECT....".encode('utf-8'))
                is_work=False
                server.close()

            elif data == "youtube":
                webbrowser.open('https://www.youtube.com/')

            elif data == "github":
                webbrowser.open('https://github.com/')

            elif data == "soul":
                webbrowser.open("https://youtu.be/JfBQFcrNn0o")

            elif data == "python":
                os.startfile(r"C:\Program Files\JetBrains\PyCharm Community Edition 2022.1.3\bin\pycharm64.exe")


if __name__=="__main__":
    start_server()
    print('SERVER DISCONNECT....')