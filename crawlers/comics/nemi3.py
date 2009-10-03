from crawlers.base import BaseComicCrawler

class Nemi3(BaseComicCrawler):
	def __init__(self):
		super(Nemi3, self).__init__('Nemi', 'adressa.no', 60, 'Norske')
		self.url = "http://www.adressa.no/template/ver2-0/img/tegneserier/Nemi/nemi_%s.gif" % (self.date.strftime("%d%m%y"))