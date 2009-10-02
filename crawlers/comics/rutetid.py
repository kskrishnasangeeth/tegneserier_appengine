from crawlers.base import BaseComicCrawler

class Rutetid(BaseComicCrawler):
	def __init__(self):
		super(Rutetid, self).__init__('ag9taW5ldGVnbmVzZXJpZXJyCwsSBUNvbWljGAcM')
		self.url = "http://nutria.msn.no/external/strand/rute_%s.jpg" % (self.date.strftime("%Y%m%d"))