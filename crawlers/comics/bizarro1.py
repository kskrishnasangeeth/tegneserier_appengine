from crawlers.base import BaseComicCrawler
from google.appengine.api import urlfetch
from BeautifulSoup import BeautifulSoup

class Bizarro1(BaseComicCrawler):
	def __init__(self):
		super(Bizarro1, self).__init__('ag9taW5ldGVnbmVzZXJpZXJyCwsSBUNvbWljGAEM')
		self.url = "http://felles.ba.no/bastripen/%s" % (self._imagelink())
	
	def _imagelink(self):
		content = urlfetch.fetch('http://felles.ba.no/bastripen/?p=18').content
		soup = BeautifulSoup(content)		
		return soup.find('div', {'id': 'stripe'}).findNext('img')['src']