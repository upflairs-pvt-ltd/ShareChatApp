from ShareChat.exception import ShareChatException
from ShareChat.logger import logging
from ShareChat.component.chat_message import ChatMessage
from ShareChat import utils
import os,sys,socket,time

#creating Instance of the classes
Chat_msg_obj = ChatMessage()

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
my_ip="0.0.0.0"
my_port=1005
my_address=(my_ip,my_port)
s.bind(my_address)

while True :
    recieved_data = s.recvfrom(100)
    message , ip_address , port = Chat_msg_obj.filter_message_address(RecieveDat=recieved_data)
    Data_label = utils.Data_identifier(Recieve_data_message=message)
    if Data_label == "message":
        try:
            logging.info('Dealing with message...')
            print(f"{message[1:]}  >> from --> {ip_address}")
            time.sleep(2)
        except Exception as e:
            raise ShareChatException(e,sys)

    elif Data_label == 'text-file':
        try:
            logging.info('Dealing with Text file')
        except Exception as e:
            raise ShareChatException(e,sys)

    else:
        try:
            logging.info('Dealing with image..')
        except Exception as e:
            raise ShareChatException(e,sys)
    
