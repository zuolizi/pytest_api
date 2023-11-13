# 操作config包下的ini类型的配置文件

from configparser import ConfigParser
from utils.handle_path import *


class Handle_Conf(ConfigParser):

    def __init__(self, filename):
        super(Handle_Conf, self).__init__()  # 继承父类的初始化方法
        self.filename = filename
        self.read(self.filename)

    def get_value(self, section, option):
        return self.get(section, option)


if __name__ == '__main__':
    filename = os.path.join(conf_path, 'config.ini')
    hc = Handle_Conf(filename)
    env_url = hc.get('env','url')
    print(env_url)
