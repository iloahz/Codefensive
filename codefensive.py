import os
import sys
import cgi
import webapp2
from google.appengine.ext.webapp import template
import transform

class index(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__),"index.html")
        self.response.out.write(template.render(path,{}))

class cov(webapp2.RequestHandler):
    def post(self):
        s = self.request.get('sourcecode')
        s = transform.trans(s)
        path = os.path.join(os.path.dirname(__file__),"cov.html")
        self.response.out.write(template.render(path,{'sourcecode':s}))

app = webapp2.WSGIApplication([('/',index),
                               ('/cov',cov)],
                              debug=True)
