FROM python:3-buster
COPY requirements.txt /catalog/requirements.txt
WORKDIR /catalog
RUN pip install -r requirements.txt


COPY . /catalog
CMD ["python", "main.py"]