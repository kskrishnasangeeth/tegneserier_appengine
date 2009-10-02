from crawlers.base import BaseComicCrawler

class TomToles(BaseComicCrawler):
	def __init__(self):
		super(TomToles, self).__init__('ag9taW5ldGVnbmVzZXJpZXJyCwsSBUNvbWljGAsM')
		self.url = "http://www.washingtonpost.com/wp-srv/opinion/ssi/images/Toles/c_%s_520.gif" % (self.date.strftime("%m%d%Y"))