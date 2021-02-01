FROM python:3.9.1

ARG DEBIAN_FRONTEND=noninteractive
RUN apt update -y && apt install -yq --no-install-recommends apt-utils
RUN apt update -y && apt install -y htop && apt install -y nano
RUN apt install -y curl autoconf automake libtool pkg-config

COPY requirements.txt /tmp
WORKDIR /tmp
RUN pip install --upgrade pip
RUN pip install -r requirements.txt