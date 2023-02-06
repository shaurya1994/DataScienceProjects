import requests
from flask import request as req
from flask import Blueprint, render_template


# Stores the standard routes for the website and also for rendering custom templates
views = Blueprint('views', __name__)


# ROUTES
# 'GET', 'POST' are the methods allowed on the URL
@views.route('/', methods=['GET', 'POST'])
def index():
    if req.method == 'POST': # Remove script from index.html
        API_URL = 'https://api-inference.huggingface.co/models/facebook/bart-large-cnn'
        headers = {'Authorization': 'Bearer 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'}

        # Connects to <form> in .html
        summerize_str = req.form['str_data'] 

        max_length = int(req.form['maxL'])
        min_length = max_length // 4  # // To remove decimal value

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query({
            'inputs': summerize_str,
            'parameters': {'min_length': min_length, 'max_length': max_length}
        })[0]
        return render_template('index.html', result=output['summary_text'])
        # variable/param name important to send in .html ^
    else:
        return render_template('index.html')