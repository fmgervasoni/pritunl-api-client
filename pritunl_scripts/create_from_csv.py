import os
import csv
import logging
from pritunl_scripts.auth import request
from pritunl_scripts.get_organization import get_organization
from pritunl_scripts.get_keys import get_key
from pritunl_scripts.send_keys import mail_sender

"""

The csv must have the following structure
e.g:

Username,Email,Organization
fgervasoni,fgervasoni@mail.com,Tech

"""


def create_from_csv(csvpath):
    csv_list = []
    # Read csv and create a list with users
    with open(csvpath) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            csv_list.append(row)

    for i in csv_list:
        create = request('POST', '/user/{}'.format(get_organization(i['Organization'])),
        template = {
            'name': i['Username'],
            'email': i['Email'],
            'disabled': False,
        })
        if create.status_code == 200:
            logging.info('User {} created on pritunl server'.format(i['Username']))
            get_key(i['Organization'], i['Username'])
            mail_sender(i['Organization'], i['Username'], i['Email'])
        else:
            return create.status_code
