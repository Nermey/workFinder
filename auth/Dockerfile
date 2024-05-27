FROM python:3.12

WORKDIR /auth_service

COPY requirements.txt ./requirements.txt

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV AUTH_SERVICE_PORT=$AUTH_SERVICE_PORT
ENV AUTH_HOST=$AUTH_HOST

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY . /auth_service

CMD uvicorn auth:app --host $AUTH_HOST --port $AUTH_SERVICE_PORT