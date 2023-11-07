from ShareChat.exception import ShareChatException
from ShareChat.logger import logging
from ShareChat.component.chat_message import ChatMessage
from ShareChat.entity.config_entity import SharingConfig
from ShareChat.entity.config_entity import MessageConfig
from ShareChat import utils
import os,sys,socket,time

#creating Instance of the classes
Chat_msg_obj = ChatMessage()
path_obj = SharingConfig()
message_config_obj = MessageConfig()
artifact_dir_path = path_obj.artifact_dir

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

            #file handling to save the Data of messaging
            message_artifact_path_with_ip = os.path.join(artifact_dir_path,ip_address,'chat_message')
            print(message_artifact_path_with_ip)
            os.makedirs(message_artifact_path_with_ip, exist_ok=True)

            print()
            message_file_path = os.path.join(message_artifact_path_with_ip , message_config_obj.message_file_name)
            print(message_file_path)
            logging.info(f"writing message in Database !")
            with open(message_file_path,'a+') as message_file:
                message_file.write('\n'+message[1:])

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
    
