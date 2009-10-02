from datetime import date, timedelta, datetime, time as dtime
import time

class BaseComicCrawler(object):
	headers = {}
	def __init__(self, key):
		self.key = key
		self.timezone = 1
	
	@property
	def date(self):
		return datetime.combine(date.today(), dtime()) + timedelta(hours = self.timezone)