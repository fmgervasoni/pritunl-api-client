import os
import wget
import logging
from pritunl_scripts.auth import request
from pritunl_scripts.get_organization import get_organization
from pritunl_scripts.get_user import get_user

BASE_URL = os.environ['PRITUNL_BASE_URL']


def get_key(organization, username):
    user = get_user(organization, username)
    filename = '/tmp/{}_{}.zip'.format(organization, username)
    response = request(
    'GET', '/key/{}/{}'.format(get_organization(organization), user['id']))
    resp = response.json()
    urlKey = BASE_URL + resp['key_zip_url']
    wget.download(urlKey, filename, False)
    try:
        os.path.isfile(filename)
        logging.info('Keys generated successfully')
    except Exception as e:
        logging.warning(e)
