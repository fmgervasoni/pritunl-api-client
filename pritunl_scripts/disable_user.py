import logging
from pritunl_scripts.auth import request
from pritunl_scripts.get_organization import get_organization
from pritunl_scripts.get_user import get_user


def disable_user(organization, username):
    user = get_user(organization, username)
    create = request('PUT','/user/{}/{}'.format(get_organization(organization), user['id']),
    template = {
        'name': user['name'],
        'email': user['email'],
        'disabled': True,
    })
    if create.status_code == 200:
        logging.info('User: {} Disabled'.format(user))
    else:
        return create.status_code
