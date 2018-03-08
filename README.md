# HLM Nomination Form

A simple Flask app to help out with Netsoc's HLM nominations.

## Installation

1. Move `config.example.py` to `config.py`, and modify them to contain your Sendgrid API details.
2. `docker build -t netsoc/nominate-form .`
3. `docker run -v $HOME/config.py:/nominate/config.py -d --rm --expose 5000:5000 netsoc/nominate-form`
