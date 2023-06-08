![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for Codeanywhere. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Codeanywhere and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **March 3rd, 2023**

## Codeanywhere Reminders

To run a frontend (HTML, CSS, Javascript only) application in Codeanywhere, in the terminal, type:

`python3 -m http.server`

A button should appear to click: _Open Preview_ or _Open Browser_.

To run a frontend (HTML, CSS, Javascript only) application in Codeanywhere with no-cache, you can use this alias for `python3 -m http.server`.

`http_server`

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A button should appear to click: _Open Preview_ or _Open Browser_.

In Codeanywhere you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In Codeanywhere, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

---

Happy coding!
------------- D E L E T E ------------

Commands:

`heroku_config`


# Install program in gitpod and codeanywhere

pip3 install django - done<br>
django-admin startproject granbodagard . -  done<br>
pip3 install django-allauth - done<br>
pip3 install Pillow - done <br>
pip3 install dj_database_url psycopg2 <br>
pip3 install dj3-cloudinary-storage <br>
pip3 install django-crispy-forms <br>
pip3 install django-summernote <br>
pip3 install django-allauth <br>
pip install crispy-bootstrap5 <br>


pip3 freeze > requirements.txt <br>

python3 manage.py createsuperuser


## Terminal code to remeber


python3 manage.py makemigrations --dry-run <br>
python3 manage.py showmigrations <br>
python3 manage.py makemigrations <br>
python3 manage.py migrate <br>
python3 manage.py runserver <br>
pip install fontawesomefree <br>

# For env.py

import os <br>

os.environ["DATABASE_URL"] = "Paste in ElephantSQL database URL" <br>
os.environ["SECRET_KEY"] = "Make up your own randomSecretKey" <br>
os.environ["CLOUDINARY_URL"] = "cloudinary://************************"


-------------------------- NOTES -----------------------------
A Django model defines the fields and data behaviour's of the structured database.Therefore I would say that changing the field names alone of an existing walkthrough project model is not custom.What is custom is changing the field     types, options and relationships of an existing walkthrough project model. Also custom is creating a new model for the students project requirements where the field names, types options and relationships are appropriate for the user story. I hope that is clearer.

https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+ECOMM_PAGPPF+2021_Q2/courseware/c38cb7ad50e9443dbd94f4cef3fed1ae/0b467723b3f54a5db85c975fdf67116d/

    
    


    size = None
    if 'course_size' in request.POST:
        size = request.POST['course_size']


    if size:
        if item_id in list(shoppingbag.keys()):
            if size in shoppingbag[item_id]['items_by_size'].keys():
                shoppingbag[item_id]['items_by_size'][size] += quantity
            else:
                shoppingbag[item_id]['items_by_size'][size] = quantity
        else:
            shoppingbag[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(shoppingbag.keys()):
            shoppingbag[item_id] += quantity
        else:
            shoppingbag[item_id] = quantity
            messages.success(request, f'Added {course.name}')

