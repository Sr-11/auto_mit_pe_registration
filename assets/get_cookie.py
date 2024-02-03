# This file aims to resolve the Duo 2FA verification.

import browser_cookie3
# cookies = browser_cookie3.chrome(domain_name='.mit.edu')
cookies = browser_cookie3.chrome(domain_name='eduapps.mit.edu')
for cookie in cookies:
    if cookie.name == 'JSESSIONID':
        print(cookie.value)