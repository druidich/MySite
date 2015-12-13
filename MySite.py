from flask import Flask, request, make_response, redirect, abort, render_template
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)


@app.route('/')
def hello_world():
    return render_template("user.html",
                           name='miha')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500
if __name__ == '__main__':
    app.run()
