<img src="https://github.com/UCCNetsoc/wiki/raw/master/assets/logo-service-hlms.svg" width="360" />

# HLM Nomination Form

A simple Flask app to help out with Netsoc's HLM nominations.

## Installation

1. Move `config.example.py` to `config.py`, and modify them to contain your Sendgrid API details.
2. `docker build -t netsoc/nominate-form .`
3. `docker run -d --restart --p 4499:5000 netsoc/nominate-form`
