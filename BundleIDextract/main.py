from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def check_app_ids():
    if request.method == 'POST':
        # Get Apple IDs from form
        apple_ids = request.form.get('apple_ids').split(',')
        # Call your main() function to check IDs
        results = main(apple_ids)
        # Render template with results
        return render_template('results.html', results=results)
    else:
        # Render empty form
        return render_template('form.html')

apple_ids = [357828853,
            389157776,
            909998122,
            521633042,
            545551605,
            1176001245,
            1044413150] # remove when un-needed

def main(apple_ids):
    
    if len(apple_ids) == 0:
        return 'No input provided'
    else:
        output = []
        for id in apple_ids:
            with requests.Session() as s:
                url = f'https://itunes.apple.com/lookup?id={id}&country=us'
                r = s.get(url)
                data = r.json()
                if data['resultCount'] == 0:
                    output.append(f'No results found for Apple App ID {id}')
                else:
                    bundle = data['results'][0]['bundleId']
                    output.append(f'AppStoreID: {id}, BundleID: {bundle}')
        return output
