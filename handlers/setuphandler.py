import wsgiref.handlers
from datetime import date
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.api import urlfetch
from models.comic import Comic
from models.picture import Picture

class SetupHandler(webapp.RequestHandler):
	def get(self):
		norske = ['Bizarro - ba.no', 'Bizarro - it-content.com', 'Nemi - bt.no', 'Nemi - db.no', 'Nemi - adressa.no', 'Rutetid - msn.no', 'Six Chix - it-content.com']
		utenlandske = ['Bizarro - kingfeatures.com', 'Joy of Tech - geekculture.com', 'Tom Toles - washingtonpost.com', 'Wulffmorgenthaler - wulffmorgenthaler.com', 'xkcd - xkcd.com']

		counter = 1
		
		for tegneserie in norske:
			self.response.out.write("%s - %s <br />\n" % (tegneserie, create_comic(tegneserie, 'norske', counter).key()))
			counter += 1
		
		for tegneserie in utenlandske:
			self.response.out.write("%s - %s <br />\n" % (tegneserie, create_comic(tegneserie, 'utenlandske', counter).key()))
			counter += 1
		
		self.response.out.write("Inserted comics!")

def create_comic(name, group, sort_order):
	comic = Comic(name = name, group=group, sort_order = sort_order)
	comic.put()
	return comic

def main():
	app = webapp.WSGIApplication([
	(r'.*', SetupHandler)], debug=True)
	wsgiref.handlers.CGIHandler().run(app)

if __name__ == "__main__":
	main()