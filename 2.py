from selenium import webdriver
from selenium.webdriver.chrome.service import Service  #新加mac调试
from selenium.webdriver.common.by import By
import rsa
import os
from urllib import parse
print(123)


def d1(k):
    return k

import requests

import requests

url_login = 'https://passport.teamsyun.com/papi/passport/login/applogin'

url = "https://weapp.teamsyun.com/api/basicserver/menu/checkInitModule"
cookie1 = "LOGIN_TYPE=pc_account; langType=zh_CN; e_cancleAutoLogin=1; JSESSIONID=57624FD6AECA4503CCE1B2B4909010D1; ETEAMSID=ec5f3983bd7ba254ef6c2a12499b12e2; ETEAMSID=ec5f3983bd7ba254ef6c2a12499b12e2"
headers = {"cookie": "ETEAMSID=082f94659943de7aef4c444bb1b49cd3"}
d2 = requests.session()
d1 = d2.get(url=url, headers=headers)
print(d1.text)
d3 = d2.get(url="https://weapp.teamsyun.com/api/baseserver/queryEmpMenusContext")
print(d3.text)
class A:
    def __init__(self):
        self.a = 1
     
    def cc(self):
        return 1
