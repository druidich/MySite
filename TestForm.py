from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


class TestForm(Form):
    name = StringField('What is you name?', validators=[Required()])
    submit = SubmitField('Submit')
