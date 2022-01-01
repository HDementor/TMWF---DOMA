from flask import Flask, send_from_directory, render_template
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
from backend.HelloApiHandler import HelloApiHandler


app = Flask(__name__, static_url_path='', static_folder='frontend/build')
CORS(app) #comment this on deployment
api = Api(app)


@app.route('/flask_app')
def index_flask():
    my_name = "Hamza A"
    #return render_template('index.html', msg = my_name)
    return render_template('index_flask.html', msg=my_name)
    #return send_from_directory(app.static_folder, 'index.html')


@app.route("/", defaults={'path':''})
@app.route('/react_app', defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index_react.html')

api.add_resource(HelloApiHandler, '/flask/hello')


if __name__ == '__main__':
    app.run()