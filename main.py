#!/usr/bin/env python

import wsgiref.handlers
from datetime import date
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import urlfetch

class Comic(db.Model):
	name = db.StringProperty(required=True)
	url = db.StringProperty(required=True)
	picture = db.BlobProperty(required=False)
	date = db.DateTimeProperty(auto_now_add=True)

class MyHandler(webapp.RequestHandler):
	def get(self):
		comics = db.GqlQuery('SELECT * FROM Comic WHERE date >= :1', date.today())
		values = {
			'comics': comics
		}
		self.response.out.write(
			template.render('templates/main.html', values))

class PictureHandler(webapp.RequestHandler):
	def get(self):
		key = self.request.path.split('/')[-1]
		self.response.headers['Content-Type'] = "image/png"
		self.response.out.write(Comic.get(key).picture)
		

class CreateHandler(webapp.RequestHandler):
	def get(self):
		comic1 = Comic(url = 'http://felles.ba.no/bastripen/striper/20090923_C3347MC9132.jpg', name='Bizarro')
		# comic2 = Comic(url = 'http://cserver.it-content.com/retriever.php?id=87&date=20090923', name='Bizarro')
		# 		comic3 = Comic(url = 'http://www.donald.no/upload/Forside/dagensstripexml/images/2009/big/stripestor_23_09_2009.gif', name='Donald')
		# 		comic4 = Comic(url = 'http://images.bt.no/gfx/cartoons/nemi/230909.gif', name='Nemi')
		# 		comic5 = Comic(url = 'http://www.dagbladet.no/tegneserie/nemiarkiv/serve.php?1253660400', name='Nemi')
		# 		comic6 = Comic(url = 'http://www.adressa.no/template/ver2-0/img/tegneserier/Nemi/nemi_230909.gif', name='Nemi')
		# 		comic7 = Comic(url = 'http://nutria.msn.no/external/strand/rute_20090923.jpg', name='Rutetid')
		# 		comic8 = Comic(url = 'http://cserver.it-content.com/retriever.php?id=31&date=20090923', name='Six Chix')
		# 		comic9 = Comic(url = 'http://kommisjonen.org/tegneserier/bizarro.php', name='Bizarro')
		# 		comic10 = Comic(url = 'http://danzigercartoons.com/wp-content/uploads/2009/09/dancart4109.jpg', name='Danziger')
		# 		comic11 = Comic(url = 'http://danzigercartoons.com/wp-content/uploads/2009/09/dancart4107.jpg', name='Danziger')
		# 		comic12 = Comic(url = 'http://www.geekculture.com/joyoftech/joyimages/1296.jpg', name='Joy of Tech')
		# 		comic13 = Comic(url = 'http://www.washingtonpost.com/wp-srv/opinion/ssi/images/Toles/c_09232009_520.gif', name='Tom Toles')
		# 		comic14 = Comic(url = 'http://www.wulffmorgenthaler.com/striphandler.ashx?stripid=99065c95-55da-4641-ac08-6db43ac071e9', name='Wulffmorgenthaler')
		# 		comic15 = Comic(url = 'http://imgs.xkcd.com/comics/tornado_hunter.png', name='xkcd')
		comic1.picture = urlfetch.fetch(comic1.url).content
		comic1.put()
		# comic2.put()
		# 		comic3.put()
		# 		comic4.put()
		# 		comic5.put()
		# 		comic6.put()
		# 		comic7.put()
		# 		comic8.put()
		# 		comic9.put()
		# 		comic10.put()
		# 		comic11.put()
		# 		comic12.put()
		# 		comic13.put()
		# 		comic14.put()
		# 		comic15.put()
		self.response.out.write("Inserted comics!")
		

def main():
	app = webapp.WSGIApplication([
	(r'/comics/.*', PictureHandler),
	(r'/create', CreateHandler),
	(r'.*', MyHandler)], debug=True)
	wsgiref.handlers.CGIHandler().run(app)

if __name__ == "__main__":
	main()