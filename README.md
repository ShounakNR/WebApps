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
1)In a virutal environment, you should install django and create a django project. <br />
2) you will need to install the following dependencies before you can run the service: django, tensorflow, scikit-learn, pandas, mysql-connector-python,
mysqlclient, datetime, rest_framework, apscheduler, yahoo_fin.<br />
3) You need to make a mysql server to which the project is connected and the connections have to be made like the way described in the report.<br />
