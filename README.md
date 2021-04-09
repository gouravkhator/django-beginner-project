# Django Demo Products App

This webapp was taught in [FreeCodeCamp Youtube video](https://www.youtube.com/watch?v=F5mRW0jo-U4). This webapp does not have all features, its just a small demonstration.

## Setup and Usage

Clone the repository. Then create config directory in your root directory and create a secret_key.txt file and add your secret key there like :

thisismysecretkey

Then type the following in your terminal in the root directory of the app:

### Creating Virtual Env and Installing Dependencies

```bash
pip install pipenv
pipenv shell
pipenv install
```

### Creating pre-run setup:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### Run the webapp on the development server:

```bash
python manage.py runserver
```
