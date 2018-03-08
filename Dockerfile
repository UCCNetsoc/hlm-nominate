FROM python:latest
MAINTAINER "fionnkell@gmail.com"

COPY . /nominate

# install all python requirements
RUN pip3 install -r /nominate/requirements.txt
WORKDIR /nominate/webapp

EXPOSE 5000
ENTRYPOINT ["python3", "app.py"]
