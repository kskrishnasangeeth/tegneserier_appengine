from crawlers.base import BaseComicCrawler
import time

class Nemi2(BaseComicCrawler):
	def __init__(self):
		super(Nemi2, self).__init__('Nemi', 'dagbladet.no', 50, 'Norske')
		self.timezone = -2
		self.url = "http://www.dagbladet.no/tegneserie/nemiarkiv/serve.php?%d" % (time.mktime(self.date.date().timetuple()))