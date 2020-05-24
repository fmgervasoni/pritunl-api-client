"""Pritunl API Client

Usage:
    main.py (-h | --help)
    main.py --get-oid <org_name> [--debug]
    main.py --get-user <org_name> <user_name> [--debug]
    main.py --create-user <org_name> <user_name> <user_email> [--debug]
    main.py --delete-user <org_name> <user_name> [--debug]
    main.py --disable-user <org_name> <user_name> [--debug]
    main.py --create-users-from-csv <csv_path> [--debug]

Options:
    -h --help                   Show this screen
    --get-oid                   Get Organization ID
    --get-user                  Get User properties
    --create-user               Create new user
    --delete-user               Delete user from server
    --disable-user              Disable user from server
    --create-users-from-csv     Create a bulk users from csv file
    --debug                     Set loglevel to DEBUG


"""

import sys
import time
import logging
from docopt import docopt

from pritunl_scripts.auth import request
from pritunl_scripts.get_user import get_user
from pritunl_scripts.create_user import create_user
from pritunl_scripts.get_organization import get_organization
from pritunl_scripts.create_from_csv import create_from_csv
from pritunl_scripts.delete_user import delete_user
from pritunl_scripts.disable_user import disable_user

if __name__ == '__main__':
    arguments = docopt(__doc__)

    if arguments['--debug']:
        LOGLEVEL = 'DEBUG'
    else:
        LOGLEVEL = 'INFO'

    logging.basicConfig(
        level=LOGLEVEL,
        format='%(asctime)s [%(levelname)s] %(message)s',
        handlers=[logging.StreamHandler()]
        )

    if arguments['--get-oid']:
        organization = arguments["<org_name>"]
        response = get_organization(organization)
        logging.debug(response)

    if arguments['--get-user']:
        organization = arguments["<org_name>"]
        user = arguments["<user_name>"]
        response = get_user(organization, user)
        logging.debug(response)

    if arguments['--create-user']:         
        organization = arguments["<org_name>"]
        user = arguments["<user_name>"]
        user_email = arguments["<user_email>"]
        response = create_user(organization, user, user_email)
        logging.debug(response)

    if arguments['--delete-user']:
        organization = arguments["<org_name>"]
        user = arguments["<user_name>"]
        response = delete_user(organization, user)
        logging.debug(response)

    if arguments['--disable-user']:
        organization = arguments["<org_name>"]
        user = arguments["<user_name>"]
        response = disable_user(organization, user)
        logging.debug(response)

    if arguments['--create-users-from-csv']:
        csvpath = arguments["<csv_path>"]
        response = create_from_csv(csvpath)
        logging.debug(response)
