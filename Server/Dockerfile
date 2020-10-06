FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code
RUN pip3 install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]