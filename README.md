# Application to get Twitter second line followers, in other words followers, of their followers.

## How to run application 
	
### Install requirements:
In folder with rerquirements.txt run  

	pip install -r requirements.txt

The best option is [creating new virtual environment](http://virtualenvwrapper.readthedocs.io/en/latest/install.html)

NOTE: You may need python3 (Tested on python 3.4.3). Before installing requirements do for example:

	virtualenv -p /usr/bin/python3.4 <path/to/new/virtualenv/>


### Run tests

	python manage.py test

### Make migrations

	python manage.py migrate

### Run localhost

	python manage.py runserver


## Requirements:
	python 3.4.3
	Django==1.10.2
	future==0.15.2
	oauthlib==2.0.0
	python-twitter==3.1
	requests==2.11.1
	requests-oauthlib==0.7.0
