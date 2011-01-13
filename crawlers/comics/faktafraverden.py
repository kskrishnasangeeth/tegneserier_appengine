from crawlers.base import BaseComicCrawler
import time

class FaktaFraVerden(BaseComicCrawler):
  def __init__(self):
    super(FaktaFraVerden, self).__init__('Fakta fra Verden', 'dagbladet.no', 35, 'Norske')
    self.timezone = -2
    self.url = "http://www.dagbladet.no/tegneserie/faktafraverdenarkiv/serve.php?%d" % (time.mktime(self.date.date().timetuple()))