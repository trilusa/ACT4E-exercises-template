ARG DOCKER_REGISTRY
FROM ${DOCKER_REGISTRY}/act4e/act4e-tests:alphubel

WORKDIR /ACT4E

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

COPY src src
COPY setup.py .

RUN python3 -m pip install -e .

