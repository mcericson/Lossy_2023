#source: https://stackoverflow.com/questions/18743962/python-send-udp-packet
import socket

count = 0 


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
local_hostname = socket.gethostname()
local_fqdn = socket.getfqdn()
udp_ip = socket.gethostbyname(local_hostname)   
print (udp_ip)
udp_port = 23456



def setup():
    size(100,100)
    
    
def draw():
    global sock, count, udp_ip, udp_port

    count += 1
    

    msg = (str(count)).encode("utf-8")
    sock.sendto(msg, (udp_ip, udp_port))
    print (msg)




