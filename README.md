# Automated Audit Benchmarking System - By Team Koala
Bacause of the increament of the audit data, a normal Excel table is not capable of handling the and increasingly complex audit process and data analysis conducted by the ARPANSA. As a result, a database is urgently required. This project normalises the Excel data into a Mysql database schema and implemented a backend to automate the "IMRT" and "3DRT" analysis process.

Additionally, an local program is developed as a substitution of front-end to allow user to run the automated process.

## List of files
```
├── LocalProgram
│   ├── Demo.py
│   ├── config.py
│   ├── download
│   ├── graphRequest.py
│   ├── resultRequest.py
│   ├── unitTest.py
│   ├── upload
│      	├── AllData.xlsx
│      	└── uploadingData.xlsx
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

## Documents
* [Database](https://github.com/geoffreychen831/AABKoala/blob/doc/database/database%20guide/AA-Koala_Database_Guide.md)
* [Backend](https://github.com/geoffreychen831/AABKoala/blob/doc/backend/backend%20guide/Server.md)
* Local Program
* [Deployment guide](https://github.com/geoffreychen831/AABKoala/blob/doc/deploy/deployment%20guide/AA-Koala%20Deployment%20Guide.md)

## Changelog
* [Changelog](https://github.com/geoffreychen831/AABKoala/blob/doc/changelog/CHANGLOG.md)

## Recommented System Requirement

* **CPU**: 3.2GHz x 2 cores
* **RAM**: 16GB
* **Hard drive**: 40GB
* **Operating** **system**: Linux(e.g. ubuntu or centOS)

## Deploy our service
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

