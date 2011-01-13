from crawlers.base import BaseComicCrawler
import time

class Lunch(BaseComicCrawler):
  def __init__(self):
    super(Lunch, self).__init__('Lunch', 'dagbladet.no', 50, 'Norske')
    self.timezone = -2
    self.url = "http://www.dagbladet.no/tegneserie/luncharkiv/serve.php?%d" % (time.mktime(self.date.date().timetuple()))