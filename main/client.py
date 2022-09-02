import socket
import threading

ip=str(input("IP: "))
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((ip,4040))
print("\nENTER YOUR MESSAGE\n")
is_work=True

def start_client():
	    while is_work:
	    	client.send(input().encode("utf-8"))
	    	
def listen_message():
	global is_work
	data= client.recv(1024).decode("utf-8")
	print(f"SERVER: {data}")
	is_work=False
		
if __name__== "__main__":
	threading.Thread(target=start_client).start()
	threading.Thread(target=listen_message).start()