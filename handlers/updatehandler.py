import wsgiref.handlers
from google.appengine.ext 							import webapp, db
from datetime														import date
from models.picture											import Picture

from crawlers.comics.bizarro1  					import Bizarro1
from crawlers.comics.bizarro2  					import Bizarro2
from crawlers.comics.bizarro3  					import Bizarro3
from crawlers.comics.donald    					import Donald
from crawlers.comics.joyoftech 					import JoyOfTech
from crawlers.comics.nemi1  	 	 				import Nemi1
from crawlers.comics.nemi2  						import Nemi2
from crawlers.comics.nemi3  						import Nemi3
from crawlers.comics.rutetid					  import Rutetid
from crawlers.comics.sixchix						import SixChix
from crawlers.comics.tomtoles						import TomToles
from crawlers.comics.wulffmorgenthaler  import WulffmorgentHaler
from crawlers.comics.xkcd  							import Xkcd

class UpdateHandler(webapp.RequestHandler):
	def get(self):
		comics_classes = [Bizarro1, Bizarro2, Bizarro3, Donald, JoyOfTech, Nemi1, Nemi2, Nemi3, Rutetid, SixChix, TomToles, WulffmorgentHaler, Xkcd]
		
		for comic_class in comics_classes:
			try:
				comic = comic_class()
				response = comic.fetch()
				content_type = response.headers["content-type"]
				picture = response.content

				if not content_type.startswith("image/"):
					continue
				
				already_exists = db.GqlQuery('SELECT * FROM Picture WHERE date = :1 AND url = :2', date.today(), comic.url).count() > 0
				
				if already_exists:
					continue
				
				
				db_object = Picture(
				name=comic.name,
				host=comic.host,
				group=comic.group,
				url=comic.url,
				picture=picture,
				content_type=content_type,
				date=date.today(),
				sort_order=comic.sort_order)
				
				db_object.put()
			except TypeError, te:
				continue
			except Exception, e:
				raise e

def main():
	app = webapp.WSGIApplication([
	(r'.*', UpdateHandler)])
	wsgiref.handlers.CGIHandler().run(app)

if __name__ == "__main__":
	main()