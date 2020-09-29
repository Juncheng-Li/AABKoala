#FROM python:3.6
#ENV PYTHONUNBUFFERED 1
#RUN mkdir /code
#WORKDIR /code
#COPY . /code
#RUN pip3 install -r requirements.txt

FROM ubuntu:18.04
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code
RUN apt-get update -y
RUN apt-get install -y python3.6-dev
RUN apt-get install -y libmysqlclient-dev
RUN apt-get install -y python3.6
RUN apt-get remove python3-pip
RUN apt-get install -y python3-pip
RUN pip3 install -r requirements.txt
