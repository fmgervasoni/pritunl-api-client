import logging
from pritunl_scripts.auth import request
from pritunl_scripts.get_organization import get_organization
from pritunl_scripts.get_user import get_user


def delete_user(organization, username):
    user = get_user(organization, username)
    response = request(
    'DELETE', '/user/{}/{}'.format(get_organization(organization), user['id']))
    if response.status_code == 200:
        logging.info('User: {} Deleted'.format(user))
    else:
        return response.status_code
