import wsgiref.handlers
from google.appengine.ext import webapp
from google.appengine.api import urlfetch
from crawlers.comics.bizarro3 import Bizarro3

class TestHandler(webapp.RequestHandler):
	def get(self):
		bizarro = Bizarro3()
		self.response.headers["Content-type"] = "image/gif"
		self.response.out.write(urlfetch.fetch(bizarro.url, headers = bizarro.headers).content)

def main():
	app = webapp.WSGIApplication([
	(r'.*', TestHandler)], debug=True)
	wsgiref.handlers.CGIHandler().run(app)

if __name__ == "__main__":
	main()