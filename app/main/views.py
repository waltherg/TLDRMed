from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .forms import KeywordsForm
from .. import db
from ..models import Article

@main.route('/', methods=['GET', 'POST'])
def index():
    form = KeywordsForm()
    if form.validate_on_submit():
        session['keywords'] = form.keywords.data.split(' ')
        return redirect(url_for('.index'))
    return render_template('index.html',
                           form=form,
                           current_time=datetime.utcnow(),
                           keywords=session.get('keywords'))
