FROM python:3.12-slim

WORKDIR /quotes/

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./quotes .

CMD ["python","manage.py","runserver","0.0.0.0:8000"]
