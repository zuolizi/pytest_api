import requests


class Send_Request():

    _session = None

    @classmethod
    def get_session(cls):
       if not cls._session:
           cls._session = requests.session()
       return cls._session

    @classmethod
    def send(cls, method, url, data=None, json=None, params=None, headers=None):
        cls.get_session()
        method = method.lower()
        if method == 'get':
            resp = cls._session.get(url=url, params=params, headers=headers)
        elif method == 'post':
            resp = cls._session.post(url=url, data=data, headers=headers)
        elif method == 'post_json':
            resp = cls._session.post(url=url, json=data, headers=headers)

        return resp

    def session_send(self, method, url, data=None, json=None, params=None, headers=None):
        method = method.lower()
        if method == 'get':
            resp = requests.get(url=url, params=params, headers=headers)
        elif method == 'post':
            resp = requests.post(url=url, data=data, headers=headers)
        elif method == 'post_json':
            resp = requests.post(url=url, json=data, headers=headers)

        return resp


if __name__ == '__main__':
    sr = Send_Request()
    url = 'http://cms.duoceshi.cn/cms/manage/loginJump.do'
    method = 'post'
    datas = {
        'userAccount': 'admin',
        'loginPwd': '123456'
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    resp = sr.send(method=method, url=url, data=datas, headers=headers)
    print(resp.json())
