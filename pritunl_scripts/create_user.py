import logging
from pritunl_scripts.auth import request
from pritunl_scripts.get_organization import get_organization
from pritunl_scripts.get_user import get_user
from pritunl_scripts.get_keys import get_key
from pritunl_scripts.send_keys import mail_sender


def create_user(organization, username, user_email):
    create = request('POST', '/user/{}'.format(get_organization(organization)), 
    template = {
        'name': username,
        'email': user_email,
        'disabled': False,
    })
    if create.status_code == 200:
        logging.info('User: {} created'.format(username))
    else:
        logging.warning(create.status_code)
    try:
        get_key(organization, username)
        mail_sender(organization, username, user_email)
        return logging.info('User created Successfully')
    except Exception as e:
        return logging.warning(e)
