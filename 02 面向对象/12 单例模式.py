# 创建一个音乐播放器
class MusicPlayer:
    # 类属性
    instance = None
    init_flag = False

    # 重写new方法
    def __new__(cls, *args, **kwargs):
        # 1. 判断当前类属性是否为None
        if not cls.instance:
            # 2. 调用父类方法，为类对象创建一个内存空间
            cls.instance = super().__new__(cls)
        # 3. 返回类属性保存的引用
        # 重写new方法后，必须要调用父类中的new方法
        return cls.instance

    def __init__(self):
        # 判断init方法是否为第一次执行
        if not MusicPlayer.init_flag:
            print('播放器初始化中...')
            MusicPlayer.init_flag = True


if __name__ == '__main__':
    player1 = MusicPlayer()
    player2 = MusicPlayer()
    print(player1, player2, sep='\n')
