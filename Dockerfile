FROM andreacensi/act4e:spring2021

WORKDIR /ACT4E

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src src
COPY setup.py .


#RUN git clone --branch spring2021 https://github.com/idsc-frazzoli/ACT4E-exercises.git
#RUN cd ACT4E-exercises && python setup.py develop


RUN python setup.py develop

