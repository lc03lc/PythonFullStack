from threading import Thread

from client_socket import ClientSocket
from config import *
from request_protocol import RequestProtocol
from window_login import WindowLogin
from tkinter.messagebox import showinfo
from window_chat import WindowChat


class Client(object):
    def __init__(self):
        # 初始化客户端
        self.username = None
        self.window = WindowLogin()
        self.window.on_reset_button_click(self.window.clear_entry)
        self.window.on_login_button_click(self.send_login_data)
        self.conn = ClientSocket()
        self.response_handle_function = {}
        self.response_handle_function[RESPONSE_LOGIN] = self.response_login_handle
        self.response_handle_function[RESPONSE_CHAT] = self.response_chat_handle

        self.chat_window = WindowChat()
        # self.chat_window.withdraw()
        self.chat_window.on_send_button_click(self.send_chat_data)

    def startup(self):
        self.conn.connect()
        Thread(target=self.response_handle).start()
        self.window.mainloop()

    def send_login_data(self):
        username = self.window.get_username()
        password = self.window.get_password()

        request_text = RequestProtocol.request_login(username, password)
        self.conn.send_data(request_text)

    def send_chat_data(self):
        message = self.chat_window.send_msg()
        request_text = RequestProtocol.request_chat(self.username, message)
        self.conn.send_data(request_text)

        self.chat_window.append_message('我', message)

    def response_handle(self):
        while True:
            # 获取消息
            recv_data = self.conn.recv_data()
            # 解析消息
            response_data = self.parse_response_data(recv_data)
            handle_function = self.response_handle_function[response_data['response_id']]
            if handle_function:
                handle_function(response_data)

    @staticmethod
    def parse_response_data(recv_data):
        response_data_list = recv_data.split(DELIMITER)
        response_data = {}
        response_data['response_id'] = response_data_list[0]

        if response_data['response_id'] == RESPONSE_LOGIN:
            response_data['result'] = response_data_list[1]
            response_data['nickname'] = response_data_list[2]
            response_data['username'] = response_data_list[3]

        elif response_data['response_id'] == RESPONSE_CHAT:
            response_data['nickname'] = response_data_list[1]
            response_data['message'] = response_data_list[2]

        return response_data

    def response_login_handle(self, response_data):
        result = response_data['result']
        if result == '0':
            showinfo('提示', '登录失败!')
            return

        nickname = response_data['nickname']
        self.username = response_data['username']
        showinfo('提示', '欢迎{}回来!'.format(nickname))
        self.window.withdraw()
        self.chat_window.deiconify()
        self.chat_window.set_title(nickname)
        self.chat_window.deiconify()

    def response_chat_handle(self, response_data):
        sender = response_data['nickname']
        message = response_data['message']
        self.chat_window.append_message(sender, message)


Client().startup()
