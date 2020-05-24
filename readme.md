# Pritunl API Client

Manage Users and Organizations

## Requirements

- Python 3.6 or higher
- Pip
- Virtualenv (optional)


## Installation

If you decide to run it in a virtual environment, perform the following steps within a virtual environment

```bash
pip install -r requirements.txt
```

### Enviroment variables
| Variable               | Description                                                                                                 | Required | Default                            | Example                                 |
|------------------------|-------------------------------------------------------------------------------------------------------------|:--------:|------------------------------------|-----------------------------------------|
| PRITUNL_BASE_URL | The URL from our Pritunl Server |    Yes   | None               | https://mycompany.pritunl.com |
| PRITUNL_API_TOKEN         | Token provided by your Pritunl Server                                                                     |    Yes   | None                               | 7h1Si54T0k3N7h1Si54T0k3N                |
| PRITUNL_API_SECRET              | Key provided by your Pritunl Server                                                                             |    Yes   | None                               | 5M7pK3y5M7pK3y                          |

## Usage


Run the program

To run the program you have four options:

* `python3 main.py --get-oid <org_name>`
* `python3 main.py --get-user <org_name> <user_name>`
* `python3 main.py --create-user <org_name> <user_name> <user_email>`
* `python3 main.py --delete-user <org_name> <user_name>`
* `python3 main.py --disable-user <org_name> <user_name>`
* `python3 main.py --create-users-from-csv <csv_path>`

* The first option get the Organization ID. `e.g: 5e28b320357a484d65bd690d`
* The second option Get the User properties in `<dict>` format.
* The third option will create the pritunl account.
* The fourth option will delete the pritunl account.
* The fifth option will disable the pritunl account.
* The sixth option create a bulk of users from csv file.

### Debug mode

Print additional information to debug errors.

You can run the script in this mode by adding `--debug` at the end of the command
