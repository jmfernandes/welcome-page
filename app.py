import os
from flask import Flask

print '<HTML><HEAD>'
print '<TITLE>Hello World</TITLE></HEAD>'
print '<BODY><H1>Hello World</H1>'
print '<P>Program with'
print '<A HREF="http://www.python.org/"'
print '>Python</A> today</BODY></HTML>'

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)