from config import *


class ResponseProtocol(object):
    """响应拼接"""

    @staticmethod
    def response_login(result, nickname, username):
        """
        拼接登录响应，数据格式为“编号|结果|呢称|用户名”
        :param result: 登录结果，0或1
        :param nickname: 昵称，如果失败，该字符串为空
        :param username: 用户名，如果失败，该字符串为空
        :return: 登录结果响应格式字符串
        """
        return DELIMITER.join([RESPONSE_LOGIN, result, nickname, username])

    @staticmethod
    def response_chat(nickname, messages):
        return DELIMITER.join([RESPONSE_CHAT, nickname, messages])
