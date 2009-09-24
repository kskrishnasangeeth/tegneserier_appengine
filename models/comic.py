from google.appengine.ext import db

class Comic(db.Model):
	name = db.StringProperty(required=True)
	group = db.StringProperty(required=True)
	sort_order = db.IntegerProperty(required=True)