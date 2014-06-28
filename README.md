osss-web
========

To be translated in English later

În sistem trebuie să ai Python și virtualenvwrapper. Dacă ai ubuntu poți face așa:

$ sudo apt-get install python python-dev virtualenvwrapper

După care faci un virtualenv și instalezi pachetele necesare pentru proiect (fără sudo!):

$ mkvirtualenv osss-web
$ pip install flask flask-sqlalchemy

Dacă deschizi un shell nou, nu uita să activezi virtualenv-ul:

$ workon osss-web

Ca să pornești serverul, rulezi scriptul python:

$ python magazin.py
