import requests
from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def display_sellers():
    if request.method == 'POST':
        # Retrieve JSON URL from the form submission
        json_url = request.form.get('json_url')

        # Check for a valid URL
        if not json_url.startswith(('http://', 'https://')):
            return "Invalid URL. Please enter a valid HTTP or HTTPS URL."

        # Correct the URL if it doesn't end with "sellers.json"
        if not json_url.endswith('sellers.json'):
            json_url += '/sellers.json'

        try:
            # Make a GET request to the corrected JSON file URL
            response = requests.get(json_url)
            response.raise_for_status()  # Raise an exception for bad responses

            # Load JSON data
            data = response.json()
            sellers_data = data.get('sellers', [])

            # Generate HTML table with a title
            table_html = f'<h2>JSON URL: {json_url}</h2>'
            table_html += '<table border="1"><tr><th>Seller ID</th><th>Name</th><th>Domain</th><th>Seller Type</th></tr>'
            for seller in sellers_data:
                table_html += f'<tr><td>{seller["seller_id"]}</td><td>{seller["name"]}</td><td>{seller["domain"]}</td><td>{seller["seller_type"]}</td></tr>'
            table_html += '</table>'

            return render_template_string(table_html)

        except requests.exceptions.RequestException as e:
            # Handle request exceptions (e.g., connection error)
            return f"Error accessing sellers.json: {e}"

        except ValueError as e:
            # Handle JSON decoding errors
            return f"Error decoding sellers.json: {e}"

    return '''
    <form method="post">
        <label for="json_url">Enter JSON URL:</label>
        <input type="text" id="json_url" name="json_url" required>
        <input type="submit" value="Submit">
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
