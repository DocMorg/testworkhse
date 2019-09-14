FROM python:3.7.4-windowsservercore-1803
LABEL MAINTAINER Vladislav Ustimov 'viustimov@edu.hse.ru'
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt -v
CMD RUN project.py