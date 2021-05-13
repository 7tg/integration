integration
===========

Case study for Monotech

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style

Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Celery
^^^^^^

This app comes with Celery.

To run a celery worker:

.. code-block:: bash

    cd integration
    celery -A config.celery_app worker -l info

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.

Deployment
----------

The following details how to deploy this application.

Docker
^^^^^^

You will need to build the stack first. To do that, run:
.. code-block:: bash
    docker-compose -f local.yml build
Once this is ready, you can run it with:
.. code-block:: bash
    docker-compose -f local.yml up
To run the stack and detach the containers, run:
.. code-block:: bash
    docker-compose -f local.yml up -d
To run a migration, open up a second terminal and run:
.. code-block:: bash
    docker-compose -f local.yml run --rm django python manage.py migrate
To create a superuser, run:
.. code-block:: bash
    docker-compose -f local.yml run --rm django python manage.py createsuperuser
If you need a shell, run:
.. code-block:: bash
    docker-compose -f local.yml run --rm django python manage.py shell
To check the logs out, run:
.. code-block:: bash
    docker-compose -f local.yml logs

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html
