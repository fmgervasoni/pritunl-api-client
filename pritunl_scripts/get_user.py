import logging
from pritunl_scripts.auth import request
from pritunl_scripts.get_organization import get_organization


def get_user(organization, user_name):
    try:
        response = request('GET', '/user/{}'.format(get_organization(organization)))
        assert(response.status_code == 200)
        data = response.json()

        for user in data:
            if user['name'] == user_name:
                return user

    except Exception as e:
      logging.warning(e)
