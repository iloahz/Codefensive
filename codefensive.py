import os
import cgi
import webapp2
from google.appengine.ext.webapp import template

class index(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__),"index.html")
        self.response.out.write(template.render(path,{}))

class cov(webapp2.RequestHandler):
    def post(self):
        self.response.out.write('OK')

app = webapp2.WSGIApplication([('/',index),
                               ('/cov',cov)],
                              debug=True)
