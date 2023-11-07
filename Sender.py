import os, sys, socket
from ShareChat.logger import logging
from ShareChat.exception import ShareChatException
from ShareChat.component.Text_file_Process import TextFileProcess

textfile_processObj = TextFileProcess()

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
print()

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
    try:
        Data_file_path = input('Plz paste your file path ... ')
        encrypted_file_data_with_label = textfile_processObj.Data_sampling(file_path= Data_file_path)
        s.sendto(encrypted_file_data_with_label,final_target)
        logging.info(f"Text-file Data has been successfully sent to :- {final_target}")

    except Exception as e:
        raise ShareChatException(e,sys)
        
else:
    #images
    pass
