import os
import sys
import cgi
import webapp2
from google.appengine.ext.webapp import template
import transform

title = 'Codefensive 0.1 Beta'

class index(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__),"index.html")
        var = {'title':title}
        self.response.out.write(template.render(path,var))

class cov(webapp2.RequestHandler):
    def post(self):
        s = transform.trans(self.request.get('sourcecode'))
        path = os.path.join(os.path.dirname(__file__),"cov.html")
        var = {'title':title,
               'sourcecode':s}
        self.response.out.write(template.render(path,var))

app = webapp2.WSGIApplication([('/',index),
                               ('/cov',cov)],
                              debug=True)
