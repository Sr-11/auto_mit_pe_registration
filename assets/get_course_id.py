# This file aims to resolve the Duo 2FA verification.
import browser_cookie3
import requests_pkcs12
from bs4 import BeautifulSoup
import pandas as pd

cookies = browser_cookie3.chrome(domain_name='.mit.edu')
url = "https://eduapps.mit.edu/mitpe/student/registration/sectionList?filter=full&termId="
response = requests_pkcs12.get(url, verify=True, cookies=cookies, timeout=3)
response.cookies
content = response.text
soup = BeautifulSoup(content, 'lxml')
table = soup.find('table')

# table.__dict__
# rows = table.find_all('tr')  # 查找表格行
# for row in rows:
#     cells = row.find_all('td')  # 查找表格单元格
#     id_cell = cells[0] # 手工找到的
#     a = id_cell.find('a')
#     a.text
#     a.name
#     a.attrs.get('href')
a_list = table.find_all('a')
for a in a_list:
    if a.text in ['PE.0414-2 ']:
        print(a.attrs.get('href'))
    
