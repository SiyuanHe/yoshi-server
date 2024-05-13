# pull official base image
FROM python:3.9-slim

RUN apt-get -y update
RUN apt-get -y install git
RUN apt-get update && apt-get install -y \
    build-essential libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# install dependencies
RUN pip install --upgrade pip
RUN pip install mecab-python3 cutlet unidic-lite  
COPY ./requirements.txt .

#copy yoshi-tts to docker
RUN pip install -r requirements.txt

# copy project
COPY . .
