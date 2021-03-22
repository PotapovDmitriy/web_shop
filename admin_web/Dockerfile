FROM python:3-buster
COPY . /apps
WORKDIR /apps
RUN pip install -r requirements.txt
RUN pip install pymysql
RUN pip install flask_sqlalchemy

RUN apt-get update
RUN apt-get -y install build-essential libssl-dev libffi-dev python-dev
RUN pip install cryptography


CMD ["python", "main.py"]