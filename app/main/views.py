from datetime import datetime
from flask import render_template, session, redirect, url_for, flash
from . import main
from .forms import KeywordsForm
from .. import db
from ..models import Article
import requests
from lxml import etree


ENTREZ_ADDRESS = ('http://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
                  'esearch.fcgi?db=pubmed&term=PLoS%20*[journal]')
ENTREZ_OPTIONS = ['&usehistory=y']

@main.route('/', methods=['GET', 'POST'])
def index():
    form = KeywordsForm()
    if form.validate_on_submit():
        session['keywords'] = form.keywords.data.split()
        session['query'] = ENTREZ_ADDRESS + '+AND+'.join(session['keywords'])
        session['query'] += ''.join(ENTREZ_OPTIONS)

        # query PubMed for PMID's that match keywords
        r = requests.get(session.get('query', ''))
        if r.status_code == 200:
            xml = etree.fromstring(r.text)
            try:
                pmids = xml.xpath('//IdList//Id')
                pmids = [pmid.text for pmid in pmids]
                session['pmids'] = pmids
            except:
                pass

        return redirect(url_for('.index'))

    flash('I am in the process of redoing TLDRMed and have not yet ported '
          'all features over to my new codebase.\n'
          'Watch this space for updates.')

    return render_template('index.html',
                           form=form,
                           current_time=datetime.utcnow(),
                           keywords=session.get('keywords'),
                           pmids=session.get('pmids'))
