from flask import Flask, render_template, jsonify
from flask_cors import CORS

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__, static_folder="./dist/static", template_folder=">/dist")
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all():
    return render_template("index.html")


@app.route('/api/random')
def random_number():
    print("YOU GOT HERE")
    response = {
        'data': "HELLO!"
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run()