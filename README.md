osss-web
========

In your operating system you must have Python and virtualenvwrapper installed. If you have Ubuntu you can:

$ sudo apt-get install python python-dev virtualenvwrapper

After that you create a virtualenv and you can install the necessary packages for the project(without sudo!):

$ mkvirtualenv osss-web
$ pip install flask flask-sqlalchemy

If you open a new shell session, don't forget to activate the virtualenv:

$ workon osss-web

To start the server, run the python script:

$ python magazin.py
