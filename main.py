from flask import Flask, render_template, request
from flask_mail import Mail, Message
import configparser

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('config.ini')

app.config['MAIL_SERVER'] = config["mail"]["MAIL_SERVER"]
app.config['MAIL_PORT'] = config["mail"]["MAIL_PORT"]
app.config['MAIL_USE_TLS'] = config.getboolean("mail", "MAIL_USE_TLS")
app.config['MAIL_USERNAME'] = config["mail"]["MAIL_USERNAME"]
app.config['MAIL_PASSWORD'] = config["mail"]["MAIL_PASSWORD"]


mail = Mail(app)

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/submit_form', methods=['POST',])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    msg = Message('New Contact Form Message', sender=config["mail"]["MAIL_USERNAME"], recipients=[config["settings"]["TARGET_CANTACT_MAIL"]])
    msg.body = f'Name: {name}\nEmail: {email}\nMessage: {message}'
    mail.send(msg)

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, port=8000)

