# Automated Audit Benchmarking System - By Team Koala
Bacause of the increament of the audit data, a regular Excel file is not capable of handling the increasingly complex data structure and audit process conducted by the ARPANSA. As a result, a database is urgently required. This project normalised the Excel data into a Mysql database schema and implemented a backend that automates the "IMRT" and "3DRT" analysis process. 

In addition, an local program is developed as a substitution of front-end to allow user to run the automated process with various options.

## Recommended System Requirement

* **CPU**: 3.2GHz x 2 cores
* **RAM**: 16GB
* **Hard drive**: 40GB
* **Operating** **system**: Linux(centOS)

## Technology
* Database: Mysql 8.0
* Backend: Django Rest Framework 3.11.1
* Deployment: Docker 19.03.13
* Python dependencies:
  * Django 3.1.1
  * mysqlclient 1.4.0
  * matplotlib 3.3.1
  * pandas 1.1.1
  * drf-yasg 1.17.1

## Getting Started
### Deploy our service
Before you start, make sure `git`, `docker` and `docker-compose` are installed on the server.(If you need help with this, instructions can be found in our [deployment guide](https://github.com/geoffreychen831/AABKoala/blob/doc/deploy/deployment%20guide/AA-Koala%20Deployment%20Guide.md))

**1. Pull code from our github repo**

   ```shell 
   git clone https://github.com/geoffreychen831/AABKoala.git
   ```

(Alternatively, you can upload the code in server directory onto the server)

**2. Deploy**

   ```shell
   cd Server
   sudo docker-compose up -d
   ```
### Use local program
Once deployment completes, you can use local program to run our predefined audit process.
Here takes inserting result as an example.
1. Open `uploadData.xlsx` and fill in the data you want to insert into database

2. Open the `Demo.py` and call `insertResult()`
```python
from LocalProgram.resultRequest import *
resultRequest.insertNewResult()
```
3. If it returns a json in the console, meaning it has succesfully inserted the result
4. You can check the inserted result by calling `listResults()`
```python
from LocalProgram.resultRequest import *
resultRequest.listResults()
```
5. Go to download folder, open the downloaded Excel, all the data in database are now downloaded in this file.

For full instruction, please refer to our [Local Program Document](https://github.com/geoffreychen831/AABKoala/blob/doc/local/local%20program%20guide/local%20program%20guide.md)

## Documents
* [Database](https://github.com/geoffreychen831/AABKoala/blob/doc/database/database%20guide/AA-Koala_Database_Guide.md)
* [Backend](https://github.com/geoffreychen831/AABKoala/blob/doc/backend/backend%20guide/Server.md)
* [Local Program](https://github.com/geoffreychen831/AABKoala/blob/doc/local/local%20program%20guide/local%20program%20guide.md)
* [Deployment guide](https://github.com/geoffreychen831/AABKoala/blob/doc/deploy/deployment%20guide/AA-Koala%20Deployment%20Guide.md)
* [User Stories](https://github.com/geoffreychen831/AABKoala/blob/master/Doc/Userstories.pdf)
* [Test Cases Doc](https://github.com/geoffreychen831/AABKoala/blob/master/Test/FunctionalTestCase.pdf)

## Test
* [Local Program Test Cases](https://github.com/geoffreychen831/AABKoala/tree/master/LocalProgram/tests)
* [Backend Test Cases](https://github.com/geoffreychen831/AABKoala/tree/master/Server/apps/graphs/tests)

## Changelog
* [Changelog](https://github.com/geoffreychen831/AABKoala/blob/doc/changelog/CHANGLOG.md)

## List of files
```
├── Doc
├── LocalProgram
│   ├── Demo.py
│   ├── config.py
│   ├── graphRequest.py
│   ├── resultRequest.py
│   ├── tests
│   └── upload
└── Server
    ├── AAB
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── apps
    │   └── graphs
    │       ├── Services
    │       │   └── graphService.py
    │       ├── admin.py
    │       ├── apps.py
    │       ├── migrations
    │       ├── models.py
    │       ├── serializers.py
    │       ├── tests
    │       │   ├── test_urls.py
    │       │   └── test_views.py
    │       ├── urls.py
    │       └── views.py
    ├── utils
        ├── images
        ├── plGraphs  
        ├── plot.py
        └── sample.py
```

## Motivational Model
* Functional Goal
![Functional Goal](https://github.com/geoffreychen831/AABKoala/blob/doc/images/images/Functional_Model.png)
* Non-functional Goal
![Non-functional_Model](https://github.com/geoffreychen831/AABKoala/blob/doc/images/images/Non-functional_Model.png)

## Personas
![personas](https://github.com/geoffreychen831/AABKoala/blob/doc/images/images/personas.png)
