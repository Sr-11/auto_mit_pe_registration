import browser_cookie3
import requests_pkcs12 
import pandas as pd
import time 
import pytz  
import curses
import itertools
pd.options.mode.chained_assignment = None  # default='warn'
est_timezone = pytz.timezone('US/Eastern')

cookies = browser_cookie3.chrome(domain_name='.mit.edu')
headers = {}
# url = "https://eduapps.mit.edu/mitpe/student/registration/sectionList?filter=open&termId=" # only view open classes
url = "https://eduapps.mit.edu/mitpe/student/registration/sectionList?filter=all&termId="

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

target_keywords = ['Pistol ', 'Rifle ', 'Air Pistol ', 'Air Rifle ']
for i in itertools.count():
    start_time = time.time()

    response = requests_pkcs12.get(url, verify=True, cookies=cookies, timeout=3, headers=headers)

    mid_time = time.time()

    content = response.text
    tables = pd.read_html(content)
    df = tables[0]
    filtered_rows = df[df['Title'].apply(lambda x: any(x.startswith(s) for s in target_keywords))]
    filtered_rows.loc[:, 'Title'] = filtered_rows['Title'].apply(lambda x: next((s for s in target_keywords if x.startswith(s)), x))
    filtered_rows = filtered_rows.drop(columns=['Activity', 'Locations'])

    end_time = time.time()

    request_duration = end_time - start_time
    parsing_duration = end_time - mid_time
    est_time = time.strftime('%H:%M:%S', time.localtime(time.time()))
    output = f'\n################################################\n\
                \rRequest Duration: {request_duration:.2f}s\n\
                \rParsing Duration: {parsing_duration:.2f}s\n\
                \rEST Time: {est_time}\n\
                \r{filtered_rows}\n\
                \r################################################\n'

    stdscr.clear()
    stdscr.addstr(0, 0, output)
    stdscr.refresh()

    # time.sleep(1)
