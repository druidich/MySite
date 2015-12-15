from flask import Flask, request, make_response, redirect, abort, render_template, session, url_for, flash
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from datetime import datetime
from config import secretKey
from TestForm import TestForm

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = secretKey


# @app.route('/')
# def hello_world():
#     return render_template("TestTime.html",
#                            current_time=datetime.utcnow(),
#                            name='miha')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = TestForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed you name')
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('test.html', form=form, name=session.get('name'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
