FROM python:latest

COPY requirements.txt usr/src/app/requirements.txt
WORKDIR usr/src/app
RUN pip install -r requirements.txt

CMD ["python", "consumer.py"]

COPY . .