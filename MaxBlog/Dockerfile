FROM mediasapiens/python3

RUN mkdir /web
WORKDIR /web
COPY requirements.txt /requirements.txt
RUN apt-get update && apt-get -y install libz-dev libjpeg-dev libfreetype6-dev python-dev python-imaging python3-imaging
RUN pip install -r /requirements.txt && rm /requirements.txt