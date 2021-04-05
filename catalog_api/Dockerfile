FROM python:3-buster
COPY requirements.txt /catalog_api/requirements.txt
WORKDIR /catalog_api
RUN pip install -r requirements.txt


COPY . /catalog_api
CMD ["python", "main.py"]