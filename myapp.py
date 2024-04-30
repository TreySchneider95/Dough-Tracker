from flask import Flask
from flask import request
from flask import render_template, redirect, url_for
from dd import get_dd, write_dd
from party import read_parties, write_party, remove_party
import json

app = Flask(__name__)
app.run(debug=False)
app.static_folder = "static"

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

@app.route("/finish_party/<name>", methods=["GET"])
def finish_party(name):
    print(name)
    remove_party(name)
    return redirect(url_for('home'))
    
