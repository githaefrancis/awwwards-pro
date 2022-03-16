# Awwwards Pro

## Description

A django web application that allows users to rate other people's software projects.Users can also upload their personal projects and have the audience rate them.


# BDD
- User views all projects posted.

- User registers for an account.

-User logs into the account.

-User updates profile.

-User uploads a project.

-User rates selected project based on design, usability and content.

-User views the average of the rating criteria per project.


# API endpoints

The application provides two RESTFUL API endpoints:

1. **api/profile**

-Returns all user profiles json format
2. **api/projects**

-Returns all projects posted in json format


# Tools and Technologies

- Python-Programming language
- Django - Web app framework.
- Django Rest Framework -For API creation
- Postgresql -For the database
- Bootstrap5 -For styling and responsiveness.

-JQuery - Interactivity and AJAX

## Setting up the project locally

1. Clone the repository
```bash
git clone git@github.com:githaefrancis/awwwards-pro.git
```

2. Navigate to the project folder
```
cd AWWWARDS-PRO
```
3. Create and activate the virtual environment

```bash
python3 -m venv virtual

source virtual/bin/ activate
```

4. Install dependencies from the requirements.txt

```bash
pip install -r requirements.txt
```
5. Create database


6. Create .env file

```bash
export DB_NAME=<name_of_db>

export DB_USER='db_user'

export DB_PASSWORD='db_password'
export SECRET_KEY='secret_key'


export DEBUG='False'

export DB_HOST='127.0.0.1'

export MODE='dev'

export ALLOWED_HOSTS='.localhost','.heroku.com','.127.0.0.1'

export DISABLE_COLLECTSTATIC=1

cloudinary_api_key=<cloudinary secret key>
cloudinary_secret=<cloudinary secret>
cloud_name=<cloudinary cloud name>
```

7. Load .env

```bash 
source .env
```

8. Migrate models

```
python3 manage.py migrate
```
9. Run tests

```
python3 manage.py test
```

10. Run the app

```
python3 manage.py runserver

```


## Livelink

[Awwwards Pro](https://awwwards-pro.herokuapp.com/)

## Contact

Email: mureithigithae@gmail.com

## License

This project is under the MIT License [click here for more information](LICENSE)

&copy; 2022 Francis Githae

