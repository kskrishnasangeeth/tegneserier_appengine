import wsgiref.handlers
from google.appengine.ext import webapp
from models.picture import Picture


class PictureHandler(webapp.RequestHandler):
	def get(self):
		key = self.request.path.split('/')[-1]
		picture = Picture.get(key)
		self.response.headers['Content-Type'] = picture.content_type.__str__()
		self.response.out.write(picture.picture)

def main():
	app = webapp.WSGIApplication([
	(r'.*', PictureHandler)], debug=True)
	wsgiref.handlers.CGIHandler().run(app)

if __name__ == "__main__":
	main()