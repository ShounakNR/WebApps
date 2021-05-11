# WebApps
------------------------------
## File structure
```
\---SuperStonks (name of your virtual environment)
    |   manage.py
    |   
    +---stockapp
    |   |   admin.py
    |   |   apps.py
    |   |   indicators.py
    |   |   long_term.py
    |   |   models.py
    |   |   queries.py
    |   |   short_term.py
    |   |   tests.py
    |   |   urls.py
    |   |   views.py
    |   |   __init__.py
    |   |   
    |   +---static
    |   |       api.css
    |   |       main.css
    |   |          
    |   +---templates
    |   |       aapl.html
    |   |       about.html
    |   |       amzn.html
    |   |       analysis.html
    |   |       contact.html
    |   |       fb.html
    |   |       googl.html
    |   |       historical_data.html
    |   |       home.html
    |   |       landing_page.html
    |   |       learning_page.html
    |   |       longterm.html
    |   |       myhome.html
    |   |       nflx.html
    |   |       predict.html
    |   |       predict_form.html
    |   |       query.html
    |   |       trip.html
    |   |       tsla.html
    |   |       twtr.html
    |   |       vac.html
    |   |       yelp.html
    +---updater
    |   |   update.py            
    |           
    \---SuperStonks
        |   asgi.py
        |   serializers.py
        |   settings.py
        |   urls.py
        |   wsgi.py
        |   __init__.py
```
-------------------------------
## Implementation:
1)In a virutal environment, you should install django and create a django project. (python mamage.py startproject) <br />
2) you will need to install the following dependencies before you can run the service: django, tensorflow, scikit-learn, pandas, mysql-connector-python,
mysqlclient, datetime, rest_framework, apscheduler, yahoo_fin.<br />
#### 3) You need to make a mysql server to which the project is connected and the connections have to be made like the way described in the report.<br />
4) Create an app in the project called stockapp (using python manage.py startapp stockapp). Copy paste all these files in the exact same file structure in your virtual environment. please make sure the manage.py, setting.py are the same as in the project<br />
5) run the server using python manage.py runserver
6) you can populate the mysql using the data from the .csv files in here. If you need to create the Tables in the database you can use the SQL queries written below.
CREATE TABLE stocks (
sid INT PRIMARY KEY,
ticker VARCHAR(10)
);

CREATE TABLE historical (
sid INT,
dat DATE,
open_value FLOAT,
low FLOAT,
high FLOAT,
close_value FLOAT,
volume INT,
PRIMARY KEY (sid, dat),
FOREIGN KEY (sid) REFERENCES Stocks (sid)
);

CREATE TABLE realtime (
sid INT,
dat DATE,
tim TIME,
open_value FLOAT,
low FLOAT,
high FLOAT,
close_value FLOAT,
volume INT,
PRIMARY KEY (sid, dat, tim),
FOREIGN KEY (sid) REFERENCES Stocks (sid)
);
