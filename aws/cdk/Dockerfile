FROM node

ARG DEBIAN_FRONTEND=noninteractive
RUN apt update -y && apt install -yq --no-install-recommends apt-utils
RUN apt install -y htop nano && apt update -y
RUN apt install -y curl autoconf automake libtool pkg-config
