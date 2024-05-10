from flask import Flask
from flask import request
import os
from flask_mail import Mail, Message
from flask import render_template, redirect, url_for
from dd import get_dd, write_dd
from party import read_parties, write_party, remove_party
import json
from dotenv import load_dotenv

load_dotenv()

mail_username = os.environ.get('MAIL_USERNAME')
mail_password = os.environ.get('MAIL_PASSWORD')

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = mail_username
app.config['MAIL_PASSWORD'] = mail_password
app.static_folder = "static"

mail = Mail(app)

mail_username = os.environ.get('MAIL_USERNAME')
print(mail_username)
mail_password = os.environ.get('MAIL_PASSWORD')

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            dd = json.loads(request.data.decode('utf-8'))
            write_dd(dd['dd'])
            return "sucess"
        except Exception as e:
            print(e)
    else:
        try:
            dd = get_dd()
            try:
                party_names = [x['party_name'] for x in read_parties()]
            except Exception as e:
                party_names = []
            return render_template("home.html", dd = dd, party_names = party_names)
        except Exception as e:
            print(e)

@app.route('/add_party', methods=['POST'])
def add_party():
    party = json.loads(request.data.decode('utf-8'))
    write_party(party)
    return 'success'

@app.route('/party/<name>', methods=['GET'])
def get_party(name):
    parties = read_parties()
    the_party = [x for x in parties if x['party_name'] == name][0]
    return render_template('party.html', party = the_party)

@app.route("/finish_party/<name>", methods=["GET", "POST"])
def finish_party(name):
    if request.method == "GET":
        pass
    else:
        info = json.loads(request.data.decode('utf-8'))
        print(info)
        subject = f"{name} party info"
        body = f"{name}\n\n"
        for x in info['doughList']:
            body += f"\t{x["name"]}:\n\n\tEstimated Scoops: {x["estimated"]}\n\tQty Left: {x['qtyLeft']}\n\tTotal Scoops: {x["total"]}\n\n"
        body += f"\n\nTotal Scoops: {info['total_served']}"
        msg = Message(subject=subject, sender=mail_username, recipients=[mail_username])
        msg.body = body
        mail.send(msg)
    remove_party(name)
    return redirect(url_for('home'))
    
if __name__=="__main__":
    port=4444