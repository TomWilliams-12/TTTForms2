FROM python:3.9.7
ENV pythonunbuffered=1
WORKDIR /app

RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev gcc  -y
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .


