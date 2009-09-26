from crawlers.base import BaseComicCrawler

class Bizarro3(BaseComicCrawler):
	def __init__(self):
		super(Bizarro3, self).__init__('ag9taW5ldGVnbmVzZXJpZXJyCwsSBUNvbWljGAIM')
		self.headers = { "Referer": 'http://www.kingfeatures.com/features/comics/bizarro/about.htm' }
		self.url = "http://est.rbma.com/content/Bizarro?date=%s" % (self.date.strftime("%Y%m%d"))
