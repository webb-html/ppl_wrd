from flask import Flask

import os
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    return '''
    hello world! -tessto
    '''

if __name__ == '__main__':
    print('starting app {{ 127.0.0.1:5000 }}')
    serve(app, port=os.environ.get("PORT", 5000), host='0.0.0.0')