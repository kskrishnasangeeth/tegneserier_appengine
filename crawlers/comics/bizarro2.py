from crawlers.base import BaseComicCrawler

class Bizarro2(BaseComicCrawler):
	def __init__(self):
		super(Bizarro2, self).__init__('ag9taW5ldGVnbmVzZXJpZXJyCwsSBUNvbWljGAIM')
		self.url = "http://cserver.it-content.com/retriever.php?id=87&date=%s" % (self.date.strftime("%Y%m%d"))
		