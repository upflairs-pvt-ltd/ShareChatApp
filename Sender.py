import  socket 

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 

target_ip="127.0.0.1"
target_port=1005
final_target=(target_ip,target_port)

while True:
    msg=input("Plz enter your message : ")
    new_msg=msg.encode('ascii')
    s.sendto(new_msg,final_target)