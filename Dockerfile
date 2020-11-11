FROM python:3.8

WORKDIR /work

RUN apt-get update && apt-get install -y \
    sudo \
    git \
    libopencv-dev \
    opencv-data \
    git

RUN pip install --upgrade pip

COPY requirements.txt /work
RUN pip install -r requirements.txt

CMD [ "/bin/bash" ]
