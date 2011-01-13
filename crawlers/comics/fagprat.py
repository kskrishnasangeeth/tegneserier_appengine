from crawlers.base import BaseComicCrawler
import time

class Fagprat(BaseComicCrawler):
  def __init__(self):
    super(Fagprat, self).__init__('Fagprat', 'dagbladet.no', 30, 'Norske')
    self.timezone = -2
    self.url = "http://www.dagbladet.no/tegneserie/fagpratarkiv/serve.php?%d" % (time.mktime(self.date.date().timetuple()))