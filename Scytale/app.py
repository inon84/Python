from datetime import datetime as dt
# import pytz
from pymongo import MongoClient
from flask import Flask, render_template, jsonify, abort, redirect, url_for, request, make_response

app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb://localhost:27017/prs_db"
# mongo_client = MongoClient(app)
# db = mongo_client.db

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

class PullRequest():
        def __init__(self, id, title, description, author_name, status, labels, date_created):
            self.id = id
            self.title = title
            self.description = description
            self.author_name = author_name
            self.status = status
            self.labels = labels
            self.date_created = date_created
            # self.create_timestamp()
        
        def create_timestamp():
            return str(dt.now().replace(microsecond=0).timestamp()).split('.')[0]

# Mock DB
# Lorem ipsum, dolor sit amet consectetur adipisicing elit. Est deserunt dolore explicabo id dolor! In doloribus nostrum ipsum pariatur tempora provident, expedita quibusdam, corporis veniam culpa adipisci! Distinctio, praesentium inventore!
pr1 = PullRequest(id=500, title='Just a PR title', description='Just a description, descriptions can be long, test longer ones here as well. "OK" that\'s enough. pretty long indeed', author_name='Inon Moshkowitz', status='Draft', labels=['#test-labels', '#production'], date_created='1629933323')
pr2 = PullRequest(id=501, title='Just another title a bit longer than the one before', description="Dolor sit amet. Descriptions can be longer that that even, test more lines with long descriptions, should i shorten the preview of description in order to not present longer one's?", author_name='Random User', status='Open', labels=['#pariatur', '#culpa', '#praesentium'], date_created='1629933374')
pr3 = PullRequest(id=502, title='Doloribus nostrum', description='Dolore explicabo', author_name='Lorem Ipsom', status='Draft', labels=['#test-labels', '#testing'], date_created='1629932324')
pr4 = PullRequest(id=503, title='Tempora provident', description='Consectetur adipisicing elit', author_name='Culpa Adipisci', status='Open', labels=['#test-labels', '#todo'], date_created='1629932321')
pr5 = PullRequest(id=504, title='Is that enough titles', description='More descriptions', author_name='Expedita Quibusdam', status='Draft', labels=['#test-labels', '#edit'], date_created='1629922324')
pr6 = PullRequest(id=505, title='No, here is another', description='Descriptionnnnnnn', author_name='Who wrote this?', status='Closed', labels=['#inventore', '#another-label'], date_created='1629922325')
pr7 = PullRequest(id=506, title='Yet another title', description='Descriptioner', author_name='Inon Moshkowitz', status='Draft', labels=['#pariatur', '#important'], date_created='1629922326')
pr8 = PullRequest(id=507, title='More titles', description='עברית שפה קשה', author_name='Expedita Quibusdam', status='Open', labels=['#tempora', '#provident'], date_created='1629922327')
pr9 = PullRequest(id=508, title='Another title', description='אני עברית מינוס', author_name='Culpa Adipisci', status='Closed', labels=['#corporis', '#expedita'], date_created='1629922328')
pr10 = PullRequest(id=509, title='Corporis Veniam', description='One Two Three Four', author_name='Random User', status='Draft', labels=['#corporis', '#expedita'], date_created='1629922329')
prs_data = [pr1, pr2, pr3, pr4, pr5, pr6, pr7, pr8, pr9, pr10]

@app.route('/')
def index():
    return render_template('index.html', 
                            prs_data=prs_data)

@app.route('/prs', methods=['GET', 'POST'])
def prs():
    if request.method == 'GET':
        # return make_response(jsonify(prs_data), 200)
        # return make_response(None, 200)
        pass

    elif request.method == 'POST':
        pass

if __name__ == '__main__':
    # app.run()
    app.run(debug=True)
