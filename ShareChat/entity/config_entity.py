from ShareChat.exception import ShareChatException
from ShareChat.logger import logging
import os , sys

class SharingConfig:
    def __init__(self):
        try:
            self.artifact_dir = os.getcwd()
        except Exception as e:
            raise ShareChatException(e,sys)


class MessageConfig:
    def __init(self,SharingConfig=SharingConfig):
        self.message_dir = os.paht.join(SharingConfig.artifact_dir,"chat_message")