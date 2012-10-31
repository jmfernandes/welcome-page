import os
import json
from flask import Flask
from flask import render_template
from werkzeug.routing import Map, Rule, NotFound, RequestRedirect, BaseConverter

class ListConverter(BaseConverter):
    def to_python(self, value):
        return value.split(',')
    def to_url(self, values):
        return ','.join(BaseConverter.to_url(value)
                        for value in values)

app = Flask(__name__)
app.url_map.converters['list'] = ListConverter


@app.route('/')
def index():
    return  render_template('welcome.html')

@app.route('/about', endpoint='about')
def index():
    return  render_template('about.html')

@app.route('/contact', endpoint='contact')
def index():
    return  render_template('contact.html')

@app.route('/all-links')
def all_links():
    links = []
    for rule in app.url_map.iter_rules():
        url = url_for(rule.endpoint)
        links.append((url, rule.endpoint))
    render_template('all_links.html', links=links)
    return 'hello'


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

