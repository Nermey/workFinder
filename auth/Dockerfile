FROM python:3.12

WORKDIR /app

COPY requirements.txt .
COPY .env .

RUN export $(cat .env | xargs)

RUN pip install -r requirements.txt

COPY auth .

CMD auth.py