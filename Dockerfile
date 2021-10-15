FROM docker.io/andreacensi/act4e:spring2021

WORKDIR /ACT4E

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

COPY src src
COPY setup.py .

RUN python3 -m pip install -e .

