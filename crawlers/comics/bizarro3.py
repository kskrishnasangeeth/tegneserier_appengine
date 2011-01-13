from crawlers.base import BaseComicCrawler

class Bizarro3(BaseComicCrawler):
	def __init__(self):
		super(Bizarro3, self).__init__('Bizarro', 'est.rbma.com', 85, 'Utenlandske')
		self.headers = { "Referer": 'http://www.kingfeatures.com/features/comics/bizarro/about.htm' }
		self.url = "http://est.rbma.com/content/Bizarro?date=%s" % (self.date.strftime("%Y%m%d"))
