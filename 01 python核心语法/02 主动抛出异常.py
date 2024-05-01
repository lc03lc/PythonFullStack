def input_password():
    password = input('请输入密码: ')
    # 1. 判断密码是否符合长度要求
    if len(password) >= 8:
        return password
    # 2. 如果不满足要求，创建异常对象
    print('主动抛出异常...')
    ex = Exception('密码长度不够')
    # 3. 抛出异常
    raise ex


if __name__ == '__main__':
    try:
        psd = input_password()
        print(psd)
    except Exception as e:
        print(e)
