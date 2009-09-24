import wsgiref.handlers
from datetime import date
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.api import urlfetch
from models.comic import Comic
from models.picture import Picture

class CreateHandler(webapp.RequestHandler):
	def get(self):
		comic1 = Comic(name = 'Bizarro', group = 'Norske', sort_order = 1)
		comic1.put()
		result = urlfetch.fetch('http://felles.ba.no/bastripen/striper/20090923_C3347MC9132.jpg')
		content_type = result.headers['content-type']
		picture1 = Picture(url = 'http://felles.ba.no/bastripen/striper/20090923_C3347MC9132.jpg', date = date.today(), comic = comic1.key(), picture = result.content, content_type = content_type)
		picture1.put()
		self.response.out.write("Inserted comics!")

def main():
	app = webapp.WSGIApplication([
	(r'.*', CreateHandler)], debug=True)
	wsgiref.handlers.CGIHandler().run(app)

if __name__ == "__main__":
	main()