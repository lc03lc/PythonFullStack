from tkinter import Label, Entry, Frame, Button, LEFT, END
from tkinter import Tk


class WindowLogin(Tk):
    """登录窗口"""

    def __init__(self):
        """初始化登录窗口"""
        super().__init__()
        # 设置窗口属性
        self.widow_init()
        # 填充控件
        self.add_widgets()

    def widow_init(self):
        # 设置窗口标题
        self.title('登录')
        # 设置窗口大小和位置
        window_width = 255
        window_height = 95

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        pos_x = screen_width / 2 - window_width / 2
        pos_y = screen_height / 2 - window_height / 2

        self.geometry('%dx%d+%d+%d' % (window_width, window_height, pos_x, pos_y))
        # 设置窗口不能拉伸
        self.resizable(False, False)

    def add_widgets(self):
        # 用户名
        username_label = Label(self)
        username_label['text'] = '用户名: '
        username_label.grid(row=0, column=0, padx=10, pady=5)

        username_entry = Entry(self, name='username_entry')
        username_entry.grid(row=0, column=1)
        username_entry['width'] = 25

        # 密码
        password_label = Label(self)
        password_label['text'] = '密码: '
        password_label.grid(row=1, column=0)

        password_entry = Entry(self, name='password_entry')
        password_entry.grid(row=1, column=1)
        password_entry['width'] = 25
        password_entry['show'] = '*'

        # 按钮区
        button_frame = Frame(self, name='button_frame')
        # 重置按钮
        reset_button = Button(button_frame, name='reset_button')
        reset_button['text'] = '重置'
        reset_button.pack(side=LEFT, padx=20)
        # 登录按钮
        login_button = Button(button_frame, name='login_button')
        login_button['text'] = '登录'
        login_button.pack(side=LEFT)
        button_frame.grid(row=2, columnspan=2, pady=5)

    def get_username(self):
        username = self.children['username_entry'].get()
        return username

    def get_password(self):
        password = self.children['password_entry'].get()
        return password

    def clear_entry(self):
        self.children['username_entry'].delete(0, END)
        self.children['password_entry'].delete(0, END)

    def on_reset_button_click(self, command):
        """登录按钮的响应注册"""
        reset_button = self.children['button_frame'].children['reset_button']
        reset_button['command'] = command

    def on_login_button_click(self, command):
        """登录按钮的响应"""
        login_button = self.children['button_frame'].children['login_button']
        login_button['command'] = command

    def on_window_closed(self, command):
        # 设置关闭窗口
        self.protocol('WM_DELETE_WINDOW', command)


if __name__ == '__main__':
    window = WindowLogin()
    window.mainloop()
