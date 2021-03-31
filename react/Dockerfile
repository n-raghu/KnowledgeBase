FROM node

ARG DEBIAN_FRONTEND=noninteractive
RUN apt update -y && apt install -yq --no-install-recommends apt-utils
RUN apt update -y && apt install -y htop nano curl
RUN apt install -y curl autoconf automake libtool pkg-config
RUN mkdir /app
WORKDIR /app
RUN npx create-react-app kcc -y
COPY tools/ /app/kcc/