Docusign Connect


Docusign Connect is a Django app to instantly connect django project with docusign e-signing platform by APIs.
This Package comes with build in admin panel to sign and maintain files & 
docusign api values can be added by admin panel.

Quick start

1. Add "crispy_forms","app" & "docusign" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'crispy_forms',
        'app',
        'docusign',
        ...
    ]
2. Add line : AUTH_USER_MODEL='app.CustomUser'  to setting.py
3. Add line : X_FRAME_OPTIONS = 'ALLOWALL' to setting.py
4. Include the app URLconf in your project urls.py like this::

    path('', include('app.urls')),

5. Run ``python manage.py makemigrations`` to create the migrations.
6. Run ``python manage.py migrate`` to create the app models.
7. Run ``python manage.py createsuperuser`` to create admin username & password to login.
8. Start the development server and visit http://127.0.0.1:8000/manage/
   to manage files & settings.

9. Visit http://127.0.0.1:8000/form/ to sign document.

* PyPI page: https://pypi.org/project/deligence-django-docusign-connect/
* Bugtracker: https://github.com/deligence-vinit/deligence-django-docusign-connect/issues
* Code repository: https://github.com/deligence-vinit/deligence-django-docusign-connect
