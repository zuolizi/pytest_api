from utils.handle_excel import Handle_Excel
from utils.handle_conf import Handle_Conf
from utils.handle_requests import Send_Request
from utils.handle_path import *


class Handel_CMS:

    def login_cms(self, case=None):
        # data.xlsx路径
        conf_p = os.path.join(conf_path, 'config.ini')

        hc = Handle_Conf(conf_p)
        host_url = hc.get_value('env', 'url')
        headers = eval(hc.get_value('env', 'headers'))

        if case:
            datas = case
        else:
            data_p = os.path.join(data_path, 'data.xlsx')
            # 读取第一行数据
            he = Handle_Excel(data_p, 'login')
            datas = he.first_line()
        url = host_url + datas.get('url')
        method = datas.get('method')
        data = eval(datas.get('data'))
        return Send_Request.send(method=method, url=url, data=data, headers=headers)


if __name__ == '__main__':
    cms = Handel_CMS()
    cms.login_cms()
