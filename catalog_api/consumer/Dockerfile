FROM python:latest

COPY requirements.txt usr/src/app/requirements.txt
WORKDIR usr/src/app
RUN pip install -r requirements.txt

#RUN python -m pip install pika
#RUN python -m pip install requests

CMD ["python", "consumer.py"]

COPY . .