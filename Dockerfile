FROM python:3.7-bullseye

WORKDIR /home
RUN pip install --upgrade pip && pip install uvicorn

ADD requirements.txt .
RUN pip install -r requirements.txt

