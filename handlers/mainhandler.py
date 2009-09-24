import wsgiref.handlers
from datetime import date
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from models.comic import Comic
from models.picture import Picture

class MainHandler(webapp.RequestHandler):
	def get(self):
		pictures = db.GqlQuery('SELECT * FROM Picture WHERE date = :1', date.today())
		values = {
			'pictures': pictures
		}
		self.response.out.write(
			template.render('../templates/main.html', values))

def main():
	app = webapp.WSGIApplication([
	(r'.*', MainHandler)], debug=True)
	wsgiref.handlers.CGIHandler().run(app)

if __name__ == "__main__":
	main()