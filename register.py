import browser_cookie3
import requests
import pandas as pd
import webbrowser
import os
from bs4 import BeautifulSoup
pd.options.mode.chained_assignment = None  # default='warn'
COOKIES = browser_cookie3.chrome(domain_name='eduapps.mit.edu')

def get_course_id(target_course):
    url="https://eduapps.mit.edu/mitpe/student/registration/sectionList?filter=full"
    response = requests.get(url, verify=True, cookies=COOKIES, timeout=10)
    content = response.text
    soup = BeautifulSoup(content, 'lxml')
    table = soup.find('table')
    a_list = table.find_all('a')
    for a in a_list:
        if a.text == target_course or a.text == target_course[:-1] or a.text[:-1] == target_course:
            return a.attrs.get('href')

def open_html(content):
    browser = webbrowser.get('chrome')
    with open("temp.html", "w") as f:
        f.write(content)
    file_path = os.path.abspath("temp.html")
    browser.open('file://' + file_path)

def submit_registration(target_course, mit_id):
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Origin': 'https://eduapps.mit.edu',
        'Upgrade-Insecure-Requests': '1',
    }

    # 定义POST请求的数据
    data = {
        'sectionId': get_course_id(target_course),  # 请替换为实际的sectionId
        'mitId': str(mit_id),  # 请替换为实际的mitId
        'wf': '/registration/quick'
    }

    # 发送POST请求
    url = 'https://eduapps.mit.edu/mitpe/student/registration/create'
    response = requests.post(url, headers=headers, data=data, cookies=COOKIES, verify=True)
    # 打印
    open_html(response.text)

if __name__ == '__main__':
    submit_registration('PE.0658-1', '558684029')