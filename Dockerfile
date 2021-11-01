FROM nikolaik/python-nodejs:python3.9-nodejs16
RUN apt update && apt upgrade -y
RUN apt install python3-pip ffmpeg -y
COPY . /app
WORKDIR /app
RUN pip3 install -U pip
RUN pip3 install -U -r requirements.txt
CMD python3 main.py
