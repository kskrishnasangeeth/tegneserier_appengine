from google.appengine.ext import db
from comic import Comic

class Picture(db.Model):
	comic = db.ReferenceProperty(Comic)
	url = db.LinkProperty(required=True)
	picture = db.BlobProperty(required=True)
	content_type = db.StringProperty(required=True)
	date = db.DateProperty(required=True)