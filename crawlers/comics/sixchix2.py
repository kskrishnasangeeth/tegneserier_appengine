# http://www.kingfeatures.com/features/comics/sixchix/aboutMaina.php
from crawlers.base import BaseComicCrawler

class SixChix2(BaseComicCrawler):
	def __init__(self):
		super(SixChix2, self).__init__('Six Chix', 'est.rbma.com', 92, 'Utenlandske')
		self.headers = { "Referer": 'http://www.kingfeatures.com/features/comics/sixchix/aboutMaina.php' }
		self.url = "http://est.rbma.com/content/6Chix?date=%s" % (self.date.strftime("%Y%m%d"))