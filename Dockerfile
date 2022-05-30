FROM python:3.8
RUN apt-get update
RUN apt-get install -y libaio1 wget
RUN wget -P /tmp https://api-rest-yomori.s3.amazonaws.com/instantclient-basic-linux.x64-21.6.0.0.0dbru.zip
RUN unzip /tmp/instantclient-basic-linux.x64-21.6.0.0.0dbru.zip -d /usr/lib
ENV PYTHONUNBUFFERED=1
ENV LD_LIBRARY_PATH=/usr/lib/instantclient_21_6