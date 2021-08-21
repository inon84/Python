from datetime import datetime as dt
from datetime import timezone, timedelta, tzinfo
import requests
from flask import Flask, render_template, abort, redirect, url_for, request

app = Flask(__name__)

'''
Each PR should have the following properties:
- PR number.
- Title.
- Description.
- Author (full name).
- Status (Draft/Open/Closed).
- Labels.
- Creation Date.
'''

req_method = 'GET'

@app.route('/pr/', methods=['GET'])
def search():
    req_method = 'GET'
    return render_template('index.html',
                            req_params=request.args,
                            req_method=req_method)

@app.route('/pr/', methods=['POST'])
def pr():
    req_method = 'POST'
    pr = {
        'id': request.form['id'],
        # 'title': request.form['title'],
        # "description": request.form['desc'],
        # "author_name": request.form['author_name'],
        # "status": request.form['status'],
        # "labels": request.form['labels'],
        # "date_created": request.form['date_created']
    }
    print(pr)
    
    return render_template('index.html',
                            pr=pr,
                            req_method=req_method)

if __name__ == '__main__':
    # app.run()
    app.run(debug=True)
