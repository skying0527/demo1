
import requests

host = "http://127.0.0.1:8000/"

'''
登录获取token         
:param user: 用户名
:param psw: 密码
:return: token
'''

def token(user="admin", pwd="12345678"):

    login_url = host+"api/v1/login/"
    headers = {
        "Content-Type": "application/json"
    }
    body = {
        "username": user,
        "password": pwd
    }
    r = requests.post(url=login_url, headers=headers, json=body)
    try:
        return_token = r.json()["token"]
    except:
        print("大兄弟，返回的不是标准json格式，或者没取到token, 别问我为什么报错, 因为返回内容：\n %s" % r.text)
        return_token = ''
    return return_token

if __name__ == "__main__":

    print("获取到token值：%s" % token())


