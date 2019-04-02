# twitter-like

App similar to twitter. Main functionalities:
* Users handling - adding, modification, deleting account
* Posts - Max 140 chars
* Comments - max 60 chars
* Messages - private messages between users

## Technology Stack
* Python
* Django
* PostgreSQL
* Bootstrap4
* jQuery

## Installation
1. Clone repository
2. Create virtualenv
3. Activate virtualenv `source <venv_name>/bin/activate`
4. Install python dependencies `pip install -r requirements.txt`
5. Setup psql database called `twitter_db`
6. Change password and user to your credentials in settings.py
7. Migrate - `python manage.py migrate`

Enjoy!
