from crawlers.base import BaseComicCrawler

class Nemi1(BaseComicCrawler):
	def __init__(self):
		super(Nemi1, self).__init__('Nemi', 'images.bt.no', 40, 'Norske')
		self.url = "http://images.bt.no/gfx/cartoons/nemi/%s.gif" % (self.date.strftime("%d%m%y"))