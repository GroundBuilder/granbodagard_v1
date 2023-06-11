# To Be Ahead Blog - Introduction

Portfolio Project 5 for Code Institute Full-stack development program.
This project is a Full Stack website built using the Django framework. Granbodagård is a farm where visitors can come and buy courses that they are holding.
There is detailed about every course what you will expect from it. When its going to happen.

[Live Project Here](https://to-be-ahead-blog.herokuapp.com/)

![MockUp](docs/readme_images/mockup-tobeaheadblog.png)<br>

README Table Content

- [To Be Ahead - Introduction](#to-be-ahead-blog---introduction)
- [User Experience - UX](#user-experience---ux)

- [Design](#design)

- [Features](#features)

- [Messages and Interaction With Users](#messages-and-interaction-with-users)

- [Admin Panel/Superuser](#admin-panelsuperuser)
- [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
    - [Django Packages](#django-packages)
  - [Frameworks - Libraries - Programs Used](#frameworks---libraries---programs-used)
  - [Testing](#testing)
- [Creating the Django app](#creating-the-django-app)
- [Deployment of This Project](#deployment-of-this-project)
- [Final Deployment](#final-deployment)
- [Forking This Project](#forking-this-project)
- [Cloning This Project](#cloning-this-project)
- [Credits](#credits)
  - [Content](#content)
  - [Information Sources / Resources](#information-sources--resources)
- [Special Thanks](#special-thanks)



## User Experience - UX

![UX - Project](docs/readme_images/ux-design1.png)<br>

![UX - Issues](docs/readme_images/ux-design2.png)<br>

## Design

![Colours Palete](docs/readme_images/colors_tobeahead.png)<br>


## Features


## Messages and Interaction With Users


## Admin Panel/Superuser


## Technologies Used

### Languages Used

* [HTML 5](https://en.wikipedia.org/wiki/HTML/)
* [CSS 3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://www.javascript.com/)
* [Django](https://www.python.org/)
* [Python](https://www.djangoproject.com/)

#### Django Packages

* [Gunicorn](https://gunicorn.org/)<br>
   As the server for Heroku
* [Cloudinary](https://cloudinary.com/)<br>
   Was used to host the static files and media
* [Dj_database_url](https://pypi.org/project/dj-database-url/)<br>
   To parse the database URL from the environment variables in Heroku
* [Psycopg2](https://pypi.org/project/psycopg2/)<br>
   As an adaptor for Python and PostgreSQL databases
* [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)<br>
   For authentication, registration, account
   management


### Frameworks - Libraries - Programs Used

* [Git](https://git-scm.com/)<br>
   Git was used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub
* [Bootstrap](https://getbootstrap.com/)<br>
   Was used to style the website, add responsiveness and interactivity
* [GitHub](https://github.com/)<br>
   GitHub is used to store the project's code after being pushed from Git
* [Heroku](https://id.heroku.com)<br>
   Heroku was used to deploy the live project
* [ElephantSQL](https://customer.elephantsql.com/login/)<br>
   Database used through heroku.
* [Gitpod](https:///)<br>
   VSCode was used to create and edit the website
* [Fontawesome](https://fontawesome.com/)<br>
   To add icons to the website
* [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)<br>
   To check App responsiveness and debugging
* [Google Fonts](https://fonts.google.com/) **Not used now.**<br>
   To add the 2 fonts that were used throughout the project
* [Balsamiq](https://balsamiq.com/)<br>
   To build the wireframes overlay for the project
* [PIXLR](https://pixlr.com)<br>
   To convert the images to webp format


### Testing



## Creating the Django app

1. Go to the Code Institute Gitpod Full Template [Template](https://github.com/Code-Institute-Org/gitpod-full-template)
2. Click on Use This Template
3. Once the template is available in your repository click on Gitpod
4. When the image for the template and the Gitpod are ready open a new terminal to start a new Django App
5. Install Django and gunicorn: `pip3 install django gunicorn`
6. Install supporting database libraries dj_database_url and psycopg2 library: `pip3 install dj_database_url psycopg2`
7. Create file for requirements: in the terminal window type `pip freeze --local > requirements.txt`
8. Create project: in the terminal window type django-admin startproject your_project_name
9. Create app: in the terminal window type python3 manage.py startapp your_app_name
10. Add app to the list of installed apps in settings.py file: you_app_name
11. Migrate changes: in the terminal window type python3 manage.py migrate
12. Run the server to test if the app is installed, in the terminal window type python3 manage.py runserver
13. If the app has been installed correctly the window will display The install worked successfully! Congratulations!

## Deployment of This Project

* This site was deployed by completing the following steps:

1. Log in to [Heroku](https://id.heroku.com) or create an account
2. On the main page click the button labelled New in the top right corner and from the drop-down menu select Create New
App
3. You must enter a unique app name
4. Next select your region
5. Click on the Create App button
6. Click in resources and select Heroku Postgres database
7. Click Reveal Config Vars and add a new record with SECRET_KEY
8. Click Reveal Config Vars and add a new record with the `CLOUDINARY_URL`
9. Click Reveal Config Vars and add a new record with the `DISABLE_COLLECTSTATIC = 1`
10. The next page is the project’s Deploy Tab. Click on the Settings Tab and scroll down to Config Vars
11. Next, scroll down to the Buildpack section click Add Buildpack select python and click Save Changes
12. Scroll to the top of the page and choose the Deploy tab
13. Select Github as the deployment method
14. Confirm you want to connect to GitHub
15. Search for the repository name and click the connect button
16. Scroll to the bottom of the deploy page and select the preferred deployment type
17. Click either Enable Automatic Deploys for automatic deployment when you push updates to Github

## Final Deployment 

1. Create a runtime.txt `python-3.8.13`
2. Create a Procfile `web: gunicorn your_project_name.wsgi`
3. When development is complete change the debug setting to: `DEBUG = False` in settings.py
4. In this project the summernote editor was used so for this to work in Heroku add: `X_FRAME_OPTIONS = SAMEORIGIN `to
   settings.py.
5. In Heroku settings, delete the config vars for `DISABLE_COLLECTSTATIC = 1`

## Forking This Project

* Fork this project by following the steps:

1. Open [GitHub](https://github.com/groundbuilder/)
2. Find the 'Fork' button at the top right of the page
3. Once you click the button the fork will be in your repository

## Cloning This Project

* Clone this project by following the steps:

1. Open [GitHub](https://github.com/groundbuilder/)
2. You will be provided with three options to choose from, HTTPS, SSH or GitHub CLI, click the clipboard icon in order
to copy the URL
3. Once you click the button the fork will be in your repository
4. Open a new terminal
5. Change the current working directory to the location that you want the cloned directory
6. Type 'git clone' and paste the URL copied in step 3
7. Press 'Enter' and the project is cloned

## Credits

### Content

* Ideas for content came from www.granbodagård.se 


### Information Sources / Resources

* [W3Schools - Python](https://www.w3schools.com/python/)
* [Stack Overflow](https://stackoverflow.com/)
* [Django](https://docs.djangoproject.com/en/4.2/)
* [Dev](https://www.devhandbook.com/django/user-profile/)

## Special Thanks

* Special thanks to my mentor Gareth.