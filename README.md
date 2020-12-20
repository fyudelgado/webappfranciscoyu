WebApp to get all the GitHub Users stored on a local sqllite database
=====================================================================


# WebApp GitHub Users

WebApp to get all the GitHub Users stored on a local sqllite database. Using Flask, SQLAlchemy, Jinja2.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
- Python 3.7
- Pip
- Virtual Enviroment
- Libraries:
    alembic==1.4.3
    aniso8601==8.1.0
    certifi==2020.12.5
    chardet==4.0.0
    click==7.1.2
    Flask==1.1.2
    flask-marshmallow==0.14.0
    Flask-Migrate==2.5.3
    Flask-RESTful==0.3.8
    Flask-SQLAlchemy==2.4.4
    idna==2.10
    itsdangerous==1.1.0
    Jinja2==2.11.2
    Mako==1.1.3
    MarkupSafe==1.1.1
    marshmallow==3.10.0
    marshmallow-sqlalchemy==0.24.1
    python-dateutil==2.8.1
    python-editor==1.0.4
    pytz==2020.4
    requests==2.25.1
    six==1.15.0
    SQLAlchemy==1.3.22
    urllib3==1.26.2
    Werkzeug==1.0.1

```

### Installing

You need to have a python virtual environment for the project that uses python version 3.7

```
C:\Users\franciscoyu\PycharmProjects\webapp>python -m venv venv
```

Enable the virtual enviroment already created

```
C:\Users\franciscoyu\PycharmProjects\webapp>venv\Scripts\activate
```

Deploy the application on the directory where you created the venv enviroment, and install the requirements that the application need using the next command

```
(venv) C:\Users\franciscoyu\PycharmProjects\webapp>pip install -r requirements.txt
```

To populate the SQLite database with the data from GitHub, you need to execute the follow line. Remember if you are already run this commmand, and want to run it again, you need to delete manually the file users.db

This will cause that all the objects on the database will be drop. Be carefull when you will run this command.

[total] is the number of records that you want to download from the GitHub RestAPI that contains the users available.

```
(venv) C:\Users\franciscoyu\PycharmProjects\webapp>python main.py [total]
```

Once you seed the database with the data. Run the webapplication using the next command

```
(venv) C:\Users\franciscoyu\PycharmProjects\webapp>python run.py
```

You can see that the server is running and waiting for requests when you see the next information on the console

```
(venv) C:\Users\franciscoyu\PycharmProjects\webapp>python run.py
 * Serving Flask app "run" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 888-132-526
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## Running the tests

To run the unittests you could use the following command. There are two Unit Tests created, one for creation of the object User and the other to seed information from GitHub.

```
(venv) C:\Users\franciscoyu\PycharmProjects\webapp>python -m unittest
```
If you want instead of run the unittest, you could check the results on a web browser, following the next steps.

You could check and test the web application opening a browser like Google Chrome or Firefox and enter the next URL

```
http://127.0.0.1:5000/users
```

### Filters

You could test the filters using the next parameters on the URL

By default page_size has the value 25 and ordering is asc, but you could change the defaults values for page_size and ordering that only could have 2 values ['asc', 'desc']

```
http://127.0.0.1:5000/users/1?page_size=50&ordering=desc
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Python](https://www.python.org/) - Python 3.7
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Flask Framework
* [SQLAlchemy](https://www.sqlalchemy.org/) - ORM Database

## Authors

* **Francisco Yu** - *Initial work* - [fyudelgado](https://github.com/fyudelgado)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
