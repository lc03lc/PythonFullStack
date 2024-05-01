from tkinter import Toplevel, Text, Button, END, UNITS
from tkinter.scrolledtext import ScrolledText
import time


class WindowChat(Toplevel):
    def __init__(self):
        super().__init__()
        # 设置窗口大小
        self.geometry('%dx%d' % (795, 505))

        # 设置窗口大小不变
        self.resizable(False, False)

        # 添加组件
        self.add_widget()

    def add_widget(self):
        chat_textarea = ScrolledText(self)
        chat_textarea['width'] = 110
        chat_textarea['height'] = 30
        chat_textarea.grid(row=0, column=0, columnspan=2)

        chat_textarea.tag_config('green', foreground='#008B00')
        chat_textarea.tag_config('system', foreground='red')
        self.children['chat_textarea'] = chat_textarea

        chat_input_area = Text(self, name='chat_input_area')
        chat_input_area['width'] = 100
        chat_input_area['height'] = 7
        chat_input_area.grid(row=1, column=0, pady=10)

        send_button = Button(self, name='send_button')
        send_button['text'] = '发送'
        send_button['width'] = 5
        send_button['height'] = 2
        send_button.grid(row=1, column=1)

    def set_title(self, title):
        self.title('欢迎{}进入聊天室'.format(title))

    def on_send_button_click(self, command):
        self.children['send_button']['command'] = command

    def send_msg(self):
        msg = self.children['chat_input_area'].get(0.0, END)
        self.children['chat_input_area'].delete(0.0, END)
        return msg

    def append_message(self, sender, message):
        send_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        send_info = '{}: {}'.format(sender, send_time)
        if sender == '我':
            self.children['chat_textarea'].insert(END, send_info, 'system')
        else:
            self.children['chat_textarea'].insert(END, send_info, 'green')
        self.children['chat_textarea'].insert(END, '\n' + message + '\n')
        self.children['chat_textarea'].yview_scroll(3, UNITS)

    def on_window_close(self, command):
        self.protocol('WM_DELETE_WINDOW', command)