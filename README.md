# Instagram clone
A clone of the website for the popular photo app Instagram.

# App Screenshots:

## Home View
<img src="https://github.com/scrupycoco/InstagramClone/blob/master/media/screenshot1.png">

## Other View 
<img src="https://github.com/scrupycoco/InstagramClone/blob/master/media/screenshot2.png">

## Single view
<img src="https://github.com/scrupycoco/InstagramClone/blob/master/media/screenshot3.png">


# User stories
* Sign in to the application to start using.
* Upload my pictures to the application.
* See my profile with all my pictures.
* Follow other users and see their pictures on my timeline.
* Like a picture and leave a comment on it.

# Technologies used: 
* Html,
* python.

# Installation and Setup

Clone the repository below

```
git clone https://github.com/{username}/{repo_name}.git
```

### Create and activate a virtual environment

    virtualenv venv --python=python3.6

    source venv/bin/activate

### Install required Dependencies

    pip install -r requirements.txt

### Copy environment variable

    cp env.sample .env

### Load/refresh .environment variables

    source .env

## Running the application

```
python manage.py server
```


## Endpoints Available
 - update your available endpoints

| Method | Endpoint                        | Description                           | Roles         |
| ------ | ------------------------------- | ------------------------------------- | ------------  |
| POST   |        /auth/signup             | sign up a user                        | users         |
| POST   |        /auth/login              | log in  a user                        | users         |



# Author(s) information: 
> Namugera Bbaale Philip

# Contact information.
> To collaborate, reach out to namugera.philip@gmail.com

# License and Copyright information.
> The MIT License (MIT) Copyright © 2020 Namugera Bbaale Philip.
