from utils.handle_conf import Handle_Conf
from utils.handle_path import *
from utils.handle_requests import Send_Request as sr
from utils.handle_cms import Handel_CMS
from utils.handle_excel import Handle_Excel
import pytest
import os

hc = Handle_Conf(os.path.join(conf_path, 'config.ini'))
uname = hc.get_value('login_data', 'uname')
pwd = hc.get_value('login_data', 'pwd')


class Test_login():
    # 获取config.ini 和 data.xlsx路径
    data_path = os.path.join(data_path, 'data.xlsx')
    # 获取data.xlsx文件的数据
    he = Handle_Excel(data_path, 'login')
    datas = he.read_data()

    @pytest.fixture()
    def before_after(self, request):
        print(request.param)
        return request.param

    @pytest.mark.parametrize('case', datas)
    @pytest.mark.run(order=1)
    def test_login(self, case):
        cms = Handel_CMS()
        resp = cms.login_cms(case)
        json_resp = resp.json()
        resp_code = json_resp['code']
        row_num = case['case_id'] + 1
        excepted_code = eval(case['excepted'])['code']
        try:
            assert resp_code == excepted_code, '登录失败'
        except Exception:
            print(Exception, resp_code, excepted_code)
            self.he.write_data(row=row_num, column=8, value='失败')
        else:
            self.he.write_data(row=row_num, column=8, value='成功')


if __name__ == '__main__':
    pytest.main()
