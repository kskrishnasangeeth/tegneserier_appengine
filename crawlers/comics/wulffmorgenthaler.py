from crawlers.base import BaseComicCrawler
from google.appengine.api import urlfetch
from BeautifulSoup import BeautifulSoup

class WulffmorgentHaler(BaseComicCrawler):
	def __init__(self):
		super(WulffmorgentHaler, self).__init__('WulffmorgentHaler', 'wulffmorgenthaler.com', 130, 'Utenlandske')
		self.url = "http://www.wulffmorgenthaler.com/%s" % (self._imagelink())
	
	def _imagelink(self):
		content = urlfetch.fetch('http://www.wulffmorgenthaler.com/').content
		soup = BeautifulSoup(content)		
		return soup.find('img', {'id': 'ctl00_content_Strip1_imgStrip'})['src']