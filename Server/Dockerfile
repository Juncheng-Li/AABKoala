FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code
RUN pip3 install -r requirements.txt
ADD docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
ADD wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh
