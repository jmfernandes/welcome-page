import os
import json
from flask import Flask, render_template, url_for
from werkzeug.routing import Map, Rule, NotFound, RequestRedirect, BaseConverter

app = Flask(__name__)

app.secret_key = 'cheese'







import web


urls = (
        '/', 'Index',
        '/login', 'Login',
        '/logout', 'Logout',
        )

web.config.debug = False
app = web.application(urls, locals())
session = web.session.Session(app, web.session.DiskStore('sessions'))

class Index:
    def GET(self):
        if session.get('logged_in', False):
            return '<h1>You are logged in</h1><a href="/logout">Logout</a>'
        return '<h1>You are not logged in.</h1><a href="/login">Login now</a>'

class Login:
    def GET(self):
        session.logged_in = True
        raise web.seeother('/')

class Logout:
    def GET(self):
        session.logged_in = False
        raise web.seeother('/')

















def login():
    session['username'] = "someuser"
    session['urls'] = []

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

#@app.after_request
#def store_visted_urls():
#    session['urls'].append(request.url)
#    if(len[session['urls']]) > 5:
#           session['urls'].pop(0)
#    session.modified = True

@app.route('/')
def index():
    return  render_template('welcome.html')

@app.route('/about', endpoint='about')
def index():
    data = []
    #if 'urls' in session:
    #    data = session['urls']
    return  render_template('about.html',data=data)

@app.route('/contact', endpoint='contact')
def index():
    return  render_template('contact.html')

@app.route('/examples', endpoint='examples')
def index():
    return  render_template('example.html')

@app.route("/all-links")
def all_links():
    links = []
    for rule in app.url_map.iter_rules():
        url = url_for(rule.endpoint)
        links.append((url, rule.endpoint))
    return render_template("all_links.html", links=links)

#app.debug = True
#app.run()
#exit()
           
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

