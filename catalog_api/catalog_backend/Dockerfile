FROM python:3-buster
COPY requirements.txt /catalog_backend/requirements.txt
WORKDIR /catalog_backend
RUN pip install -r requirements.txt


COPY . /catalog_backend
CMD ["python", "main.py"]