FROM python:latest
MAINTAINER "fionnkell@gmail.com"

COPY . /nominate

# install all python requirements
RUN pip3 install -r /nominate/requirements.txt
WORKDIR /nominate/webapp

EXPOSE 5000
ENV FLASK_APP /nominate/app.py
CMD ["flask", "run"]
