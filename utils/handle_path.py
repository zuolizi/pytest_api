# 此模块保存项目中各个包的绝对路径

import os

# 项目路径
base_path = os.path.dirname(os.path.dirname(__file__))
# config模块路径
conf_path = os.path.join(base_path,'config')
# data模块路径
data_path = os.path.join(base_path,'data')
# lib模块路径
lib_path = os.path.join(base_path,'lib')
# report模块路径
report_path = os.path.join(base_path,'report')
# run模块路径
run_path = os.path.join(base_path,'run')
# testcase模块路径
testcase_path = os.path.join(base_path,'testcase')
# utils模块路径
utils_path = os.path.join(base_path,'utils')


# print(base_path)
# print(conf_path)
# print(data_path)
# print(lib_path)
# print(report_path)
# print(run_path)
# print(testcase_path)
# print(utils_path)