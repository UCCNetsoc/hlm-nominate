FROM python:3.8
LABEL maintainer="netsoc@uccsocieties.ie"

WORKDIR /nominate

EXPOSE 5000

ENV FLASK_APP /nominate/app.py

COPY requirements.txt requirements.txt

# install all python requirements
RUN pip3 install -r /nominate/requirements.txt

COPY . .

CMD ["flask", "run", "--host", "0.0.0.0"]
