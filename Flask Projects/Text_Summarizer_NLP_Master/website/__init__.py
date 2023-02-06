from flask import Flask


def initialize_app():
    # Creating main app object    
    app = Flask(__name__)

    # Import and initialize views(blueprints) here
    from .views import views # Importing here because of circular dependency issue

    app.register_blueprint(views, url_prefix='/')  
    # app.register_blueprint(home, url_prefix='/flask-todo/') Example: Sets prefix as flask-todo but does not set automatically

    return app


    # if __name__ == '__main__':
    #     app.debug = True
    #     app.run()


    # @app.route('/', methods=['GET', 'POST'])
    # def index():
    #     return render_template('index.html')

    # @app.route('/summarize', methods=['GET', 'POST'])
    # def summarize():
    #     if req.method == 'POST':
    #         API_URL = 'https://api-inference.huggingface.co/models/facebook/bart-large-cnn'
    #         headers = {'Authorization': 'Bearer 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'}

    #         # Connects to <form> in .html
    #         summerize_str = req.form['str_data'] 

    #         max_length = int(req.form['maxL'])
    #         min_length = max_length // 4

    #         def query(payload):
    #             response = requests.post(API_URL, headers=headers, json=payload)
    #             print(max_length)
    #             return response.json()
                
    #         output = query({
    #             'inputs': summerize_str,
    #             'parameters': {'min_length': min_length, 'max_length': max_length}
    #         })[0]
    #         return render_template('index.html', result=output['summary_text'])
    #         # variable/param name important to send in .html ^
    #     else:
    #         return render_template('index.html')
