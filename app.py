from flask import Flask, render_template, redirect, url_for, request, send_from_directory

app = Flask(__name__, static_url_path='', static_folder='frontend/build')


@app.route('/')
def index():
    my_name = "Hamza A"
    #return render_template('index.html', msg = my_name)
    return render_template('index.html', msg=my_name)
    #return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    app.run()