from flask import Flask
from flask import render_template, request, session
import config
import sendgrid
from sendgrid.helpers.mail import *
from validate_email import validate_email

app = Flask(__name__)
app.secret_key = config.secret_key

app.jinja_env.add_extension("pyjade.ext.jinja.PyJadeExtension")

@app.route("/")
def index():
    if session.get("nominee_name", None):
        return render_template("nominated.jade", name=session["nominee_name"])

    return render_template("home.jade")

@app.route("/submit", methods=["POST"])
def nominate():
    if session.get("nominee_name", None):
        return render_template("nominated.jade", name=session["nominee_name"])

    form = request.form

    sender_name = form.get("name", None)
    sender_email = form.get("email", None)
    nominee_name = form.get("nominee_name", None)
    nominee_email = form.get("nominee_email", None)
    reason = form.get("reason", None)

    errors = [] # store any input validation errors

    if sender_name == None or len(sender_name) == 0:
        errors.append("You forgot to enter your name.")

    if sender_email == None or len(sender_email) == 0:
        errors.append("You forgot to enter your email.")
    elif not validate_email(sender_email):
        errors.append("The email you entered in your personal details isn't valid.")

    if nominee_name == None or len(nominee_name) == 0:
        errors.append("You forgot to tell us who you're nominating.")

    if nominee_email == None or len(nominee_email) == 0:
        errors.append("You forgot to tell us the email of your nominee.")
    elif not validate_email(nominee_email):
        errors.append("The email address you provided for the nominee isn't valid.")

    if reason == None or len(reason) == 0:
        errors.append("You forgot to tell us why your nominee should receive HLM.")
    elif len(reason) > 2000:
        errors.append("Please limit your reasons for nominating to a maximum of 2000 characters.")

    if len(errors) > 0:
        return render_template("nominated.jade", errors=errors)

    sg = sendgrid.SendGridAPIClient(apikey=config.email_config["api_key"])
    from_email = Email(config.email_config["from_address"])
    to_email = Email(config.email_config["to_address"])
    subject = "[HLM] Nomination for %s" % nominee_name

    content = Content("text/plain", """
    [SENDER DETAILS]
    Name: %s
    Email: %s

    [NOMINEE DETAILS]
    Name: %s
    Email: %s

    [REASON]
    \"%s\"
    """ % (sender_name.strip(), sender_email.strip(), nominee_name.strip(), nominee_email.strip(), reason.strip()))

    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())

    status_code = str(response.status_code)

    if not status_code.startswith("20"):
        error = "There was a problem sending your nomination. Please try again,"\
                "or email your nomination to %s." % config.email_config["to_address"]
        return render_template("nominated.jade", errors=[error])

    session["nominee_name"] = nominee_name.strip()
    return render_template("nominated.jade", name=nominee_name.strip())
