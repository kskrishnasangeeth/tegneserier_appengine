from crawlers.base import BaseComicCrawler
import time

class SkavlansArk(BaseComicCrawler):
  def __init__(self):
    super(SkavlansArk, self).__init__('Skavlans Ark', 'dagbladet.no', 83, 'Norske')
    self.timezone = -2
    self.url = "http://www.dagbladet.no/tegneserie/skavlanarkiv/serve.php?%d" % (time.mktime(self.date.date().timetuple()))