## Final project: ready for the fireworks ?

The project you will work on must have a social impact and be of high added value for the community at large. That's how we are at OpenClassrooms: we share !

Carry out a digital project in the form that seems most appropriate to you (make a web application; code a website or a mobile application...) to meet a need around you. It can be a booking site for the theater association of your city, an application to locate and reference found objects during a festival, etc.

For this final project, I decided to create a social network web application where each user can add one or more cooking recipes to share with his subscribers.

### Features
- Create user account
- Edit user account profile photo
- Add cooking recipes
- Edit cooking recipes
- Delete cooking recipes
- Subscribe or Unsubscribe to users
- Select favorite cooking recipes
- Select cooking recipes by categories

### Technologies
* [Python](https://www.python.org/downloads/): Version 3.8
* [Django](https://docs.djangoproject.com/fr/4.0/): Version 4.0

### Installation
1. Clone the repository
```
git clone https://github.com/Ghazi92e/P13-OC-Recipe-blog-backend.git
```
2. Create a virtual env
```
python -m venv env
```
3. Activate the virtual env
```
source env/bin/activate
```
4. Install packages from requirements.txt
```
pip install -r requirements.txt
```
5. Create a database with Postgresql(pgAdmin)

6. Create a .env file in folder blog_lebanese_recipes(with file settings.py)
```
touch .env
```
7. Set up .env file
```
SECRET_KEY=''
DATABASE_NAME=''
DATABASE_USER=''
DATABASE_PASS=''
```

8. Run application
```
python manage.py runserver
```