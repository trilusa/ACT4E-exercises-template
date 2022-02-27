# ARG DOCKER_REGISTRY=docker.io
# FROM ${DOCKER_REGISTRY}/act4e/act4e-tests:alphubel

FROM python:3.10
RUN python3 -m pip install -U pip -v
WORKDIR /ACT4E

RUN uname -a
COPY .devcontainer/requirements.txt .
RUN python3 -m pip install -r requirements.txt

COPY src src
COPY setup.py .

RUN python3 -m pip install -e .

