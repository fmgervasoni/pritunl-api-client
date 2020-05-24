import logging
from pritunl_scripts.auth import request


def get_organization(org_name):
    try:
        response = request('GET','/organization')
        assert(response.status_code == 200)
        data = response.json()

        for organization in data:
            if organization['name'] == org_name:
                return organization['id']
                
    except Exception as e:
      logging.warning(e)
