from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


class KeywordsForm(Form):
    keywords = StringField('Enter keywords of interest.',
                           validators=[Required()])
    submit = SubmitField('Search')
