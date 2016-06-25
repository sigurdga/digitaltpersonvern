Digitalt personvern
===================

Development
-----------

```sh
git clone https://github.com/sigurdga/digitaltpersonvern
cd digitaltpersonvern
virtualenv -p python2 venv
source venv/bin/activate
pip install -r requirements.txt
cd digitaltpersonvern
python manage.py migrate
python manage.py runserver
```


