from config import *


class RequestProtocol(object):
    """响应拼接"""

    @staticmethod
    def request_login(username, password):
        return DELIMITER.join([REQUEST_LOGIN, username, password])

    @staticmethod
    def request_chat(username, messages):
        return DELIMITER.join([REQUEST_CHAT, username, messages])
