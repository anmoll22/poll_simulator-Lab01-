from Tools.scripts.make_ctype import values
from flask import *

app = Flask(__name__)

candidateDB = {}
err = None
voterDB = {}
countDB = {}


@app.route('/')
def index():
    return redirect(url_for('home'))


@app.route('/Home')
def home():
    return render_template("Home.html")


@app.route('/AddCandidate', methods=['GET', 'POST'])
def addCandidate():
    global err
    err = None
    global countDB
    if request.method == 'POST':
        if 'id' in request.form and 'Name' in request.form:
            id = request.form['id']
            Name = request.form['Name']
            if id in candidateDB.keys():
                err = 'Already Registered'
                return redirect(url_for('home'))
            else:
                candidateDB[id] = Name
                countDB[Name] = 0
                err = 'Registration Successful'
                return redirect(url_for('home'))
    return render_template("AddCandidate.html", err=err)


@app.route('/Vote', methods=['GET', 'POST'])
def vote():
    global err
    err = None
    global voterDB
    global countDB
    if request.method == 'POST':
        if 'voterID' in request.form and 'candidate' in request.form:
            voterID = request.form['voterID']
            Candidate = request.form['Candidate']
            if voterID in voterDB.key():
                err = "Already voted"
            else:
                voterDB[voterID] = Candidate
                countDB[Candidate] += 1
                err = "Voted Successfully"
                return redirect(url_for('home'))
    global candidateDB
    return render_template("Vote.html", candidateDB=candidateDB, err=err)


@app.route('/Result')
def result():
    global err
    err = None
    global countDB
    max1 = max(countDB.values())
    val1 = values.index(max1)
    max2 = 0
    for v in countDB.values():
        if max2 < v < max:
            max2 = v
    val2 = values.index(max2)
    return render_template("Result.html", max1=max1, max2=max2, val1=val1, val2=val2)


@app.route('/Summary')
def summary():
    global err
    err = None
    return render_template("Summary.html", countDB=countDB)


if __name__ != "__main__":
    pass
else:
    app.run()
