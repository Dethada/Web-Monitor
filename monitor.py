#!/usr/bin/env python3
import requests, time
from pathlib import Path
from datetime import datetime
from sendgrid_mail import send_notification
from settings import *

def mail_admins(subj, msg):
    for address in ADMINS:
        send_notification(MAIL_FROM, address, subj, msg)

# Initialization
page_file = '{}.html'.format(URL.split('//')[1])
page = Path(page_file)
if not page.is_file():
    with open(page_file, 'w') as f:
        f.write(requests.get(URL).text)

print('Monitoring {} ...'.format(URL))

try:
    while True:
        try:
            response = requests.get(URL)
        except Exception as e:
            mail_admins('{} might be down!'.format(URL), 'Web monitor expirenced an exception at {}\n{}'.format(datetime.now(), str(e)))
            print('{} might be down! {}\n{}'.format(URL, datetime.now(), str(e)))
            break

        if response.status_code != 200:
            code = response.status_code
            mail_admins('{} return status {}!'.format(URL, code), '{} returned {} at {}'.format(URL, code, datetime.now()))
            print('{} returned status {} at {}'.format(URL, code, datetime.now()))
            break

        with open(page_file, 'r+') as f:
            new = response.text
            old = f.read()
            if new != old:
                # send notification and continue monitoring
                f.seek(0)
                f.write(new)
                f.truncate()
                with open('{}_{}.html'.format(URL.split('//')[1], datetime.now()), 'w') as f2:
                    f2.write(old)
                mail_admins('{} Updated'.format(URL), '{} was updated at {}'.format(URL, datetime.now()))
                print('{} updated {} '.format(URL, datetime.now()))
        
        time.sleep(FREQUENCY)
except KeyboardInterrupt:
    print('\nExiting...')
