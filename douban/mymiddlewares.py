import random
from scrapy.conf import settings


class MyUserAgent(object):
   def process_request(self,request,spider):
      useragent=random.choice(settings["USER_AGENTS"])
      # print(useragent)
      request.headers.setdefault("User-Agent",useragent)
