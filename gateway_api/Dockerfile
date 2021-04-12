FROM python:3-buster
COPY requirements.txt /apps/requirements.txt
WORKDIR /apps
RUN pip install -r requirements.txt

COPY . /apps
CMD ["python", "main.py"]