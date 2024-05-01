class File(object):
    def __init__(self, file_name, file_model):
        self.file_name = file_name
        self.file_model = file_model

    def __enter__(self):
        print("这是上文")
        self.file = open(self.file_name, self.file_model)
        return self.file

    def __exit__(self):
        print("这是下文")
        self.file.close()

# 使用with方法调用上下文管理器
with File('xxx', 'r') as f:
    file_data = f.read()
    print(file_data)