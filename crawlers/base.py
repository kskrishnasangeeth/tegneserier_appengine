from datetime import date, timedelta

class BaseComicCrawler(object):
	timezone = 0
	headers = {}
	def __init__(self, key):
		self.key = key
	
	@property
	def date(self):
		return date.today() + timedelta(hours = self.timezone)