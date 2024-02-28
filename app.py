from flask import Flask, request, jsonify, redirect
from flask_cors import CORS
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)
CORS(app)


@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Get form data
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Send email to hackoverflow@cumail.in
    send_email(name, email, message)

    # Send automated personalized text
    send_personalized_text(email)

    # Return JSON response
    return redirect("https://hackoverflow-society-website.vercel.app/contact", code=302)


def send_email(name, email, message):
    # Set up SMTP server
    smtp_server = 'smtp.gmail.com'  # Gmail SMTP server
    smtp_port = 587  # SMTP port for Gmail
    sender_email = 'inderkiran20233@gmail.com'  # Your email
    app_password = 'krhu cexv lyue dmnz'  # Your generated app password

    # Create message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = 'hackoverflow@cumail.in'
    msg['Subject'] = "New contact form submission from Hackoverflow website."

    body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
    msg.attach(MIMEText(body, 'plain'))

    # Send email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, app_password)
        server.send_message(msg)


def send_personalized_text(email):
    # Set up SMTP server
    smtp_server = 'smtp.gmail.com'  # Gmail SMTP server
    smtp_port = 587  # SMTP port for Gmail
    sender_email = 'inderkiran20233@gmail.com'  # Your email
    app_password = 'krhu cexv lyue dmnz'  # Your generated app password

    # Create message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = 'Message Confirmation'

    body = "Your message has been sent. We'll get back to you soon!"
    msg.attach(MIMEText(body, 'plain'))

    # Send email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, app_password)
        server.send_message(msg)

