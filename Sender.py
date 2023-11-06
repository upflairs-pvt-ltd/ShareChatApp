import os, sys, socket
from ShareChat.logger import logging
from ShareChat.exception import ShareChatException

# establishing connection with UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 

target_ip="127.0.0.1"
target_port=1005
final_target=(target_ip,target_port)
title_message="""
What do you want to share ?
0    ---->  MESSAGE
1    ---->  TEXT-FILE
2    ---->  IMAGE"""
print(title_message)
task_choice = input('Plz enter your choice :- ')
if task_choice == '0':
    try:
        logging.info(f"we are sending message to :- {final_target}")
        break_condition = True
        while break_condition:
            msg=input("Plz enter your message : ")
            if msg :
                msg = '0'+msg
                encrepted_message=msg.encode('ascii')
                s.sendto(encrepted_message,final_target)
            else:
                break_condition = False
    except Exception as e:
        raise ShareChatException(e,sys)
elif task_choice == '1':
    # text-file
    pass
else:
    #images
    pass
