from utils.handle_conf import Handle_Conf
from utils.handle_path import *
from utils.handle_requests import Send_Request
from utils.handle_cms import Handel_CMS
from utils.handle_excel import Handle_Excel
import pytest
import os


class Test_adduser():
    # 获取用户信息
    he = Handle_Excel(os.path.join(data_path, 'data.xlsx'), 'add_user')
    datas = he.read_data()
    @pytest.mark.parametrize('case', datas)
    def test_adduser(self, case):
        Handel_CMS().login_cms()
        # 获取域名拼接接口
        hc = Handle_Conf(os.path.join(conf_path, 'config.ini'))
        method = case['method']
        url = hc.get_value('env', 'url') + case['url']
        datas = eval(case['data'])
        headers = eval(hc.get_value('env', 'headers'))
        resp = Send_Request.send(method=method,url=url,data=datas,headers=headers)
        print(resp.text)

if __name__ == '__main__':
    pytest.main(['-vs',r'E:\DCS_wrokspace\PycharmProjects\P\pytest_api\testcase\test_adduser.py'])
