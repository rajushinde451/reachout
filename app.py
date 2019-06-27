from flask import Flask, redirect, url_for, request, jsonify
from dbManager.selectQuery import getresutls
from dbManager.insertQuery import insertRecord
import json

app = Flask(__name__)


@app.route('/teaminsert', methods=['POST'])
def insertteamRec():
    if request.method == 'POST':
        name = request.form['teamname']
        dl = request.form['dl']
        desc = request.form['description']
        return insertRecord("insert into sys.teams (name,DL,Description) values('{}','{}','{}')".format(name, dl, desc))


@app.route('/taginsert', methods=['POST'])
def inserttag():
    if request.method == 'POST':
        name = request.form['tagName']
        return insertRecord("insert into sys.tags (TagName) values('{}')".format(name))

@app.route('/tagteaminsert', methods=['POST'])
def inserttagteam():
    if request.method == 'POST':
        teamid = request.form['teamid']
        tagid = request.form['tagid']
        return insertRecord("insert into sys.teamtags values({},{})".format(tagid,teamid))


@app.route('/')
def index():
    rows = getresutls('select * from Employee')
    #for row in rows:
    return jsonify(
        id=rows[0][0],
        name = rows[0][1],
        sid = rows[0][2],
        type = rows[0][3]
    )


@app.route('/search/<name>')
def search(name):
    rows = getresutls("select * from Employee where name='%s'" % name)
    return json.dumps(rows)


@app.route('/insert', methods=['POST'])
def insertRec():
    if request.method == 'POST':
        sid = request.form['sid']
        name = request.form['nm']
        typeofemp = request.form['type']
        return insertRecord("insert into sys.Employee (name, sid, type) values('{}','{}','{}')".format(name, sid, salary))


@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog Number %d' % postID


@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'Revision Number %f' % revNo


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm'] + " POST"
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm') + " GET"
        return redirect(url_for('success', name=user))


app.run(debug=True)
