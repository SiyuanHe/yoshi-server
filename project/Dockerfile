# pull official base image
FROM python:3.9

RUN apt-get -y update
RUN apt-get -y install git

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .

#copy yoshi-tts to docker
RUN pip install -r requirements.txt

# copy project
COPY . .
