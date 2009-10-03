from crawlers.base import BaseComicCrawler

class Rutetid(BaseComicCrawler):
	def __init__(self):
		super(Rutetid, self).__init__('Rutetid', 'nutria.msn.no', 70, 'Norske')
		self.url = "http://nutria.msn.no/external/strand/rute_%s.jpg" % (self.date.strftime("%Y%m%d"))