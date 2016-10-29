FROM ubuntu:14.04

MAINTAINER Mohd Sheeraz

RUN apt-get update -y && apt-get install -y nginx \
    python-dev \
    supervisor \
    python-pip \
    libffi-dev \
    libssl-dev \
    libpq-dev \
    libmysqlclient-dev \
    && \
    pip install -U pip && \
    rm /bin/sh && \
    ln -s /bin/bash /bin/sh

ENV WORKDIR /opt/workspace/dexterhive/

COPY requirements.txt $WORKDIR

WORKDIR $WORKDIR

RUN pip install -r requirements.txt && pip install j2cli gunicorn boto3

COPY ./ $WORKDIR

EXPOSE 80

RUN chmod +x deploy/init.sh
