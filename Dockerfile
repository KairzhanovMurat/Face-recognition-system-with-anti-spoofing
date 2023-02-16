FROM python:3.10.3-slim-bullseye



WORKDIR /app


COPY . /app

RUN apt-get -y update
RUN apt-get install -y --fix-missing \
    build-essential \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libatlas-base-dev \
    libavcodec-dev \
    libavformat-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python3-dev \
    python3-numpy \
    software-properties-common \
    zip \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*


RUN  git clone https://github.com/davisking/dlib.git && cd dlib &&\
     mkdir build && cd build && cmake ..&& cmake --build . && cd ../.. &&\
     pip install -r requirements.txt &&  \
     rm requirements.txt && \

EXPOSE 8000



