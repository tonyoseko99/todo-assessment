# use an official Python runtime as a parent image, a lightweight, minor version of Python 3.8.10

FROM python:3.8.10-slim-buster

# set the working directory in the container to /app

WORKDIR /app

# copy the current directory contents into the container at /app

COPY . /app

# install any needed packages specified in requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

#  make port 8000 available to the world outside this container

EXPOSE 8000

# define the environment variable

ENV DJANGO_SETTINGS_MODULE=TODO_Project.settings

# run the command to start Django app

CMD ["python", "manage.py", "runserver", "0,0,0,0:8000"]