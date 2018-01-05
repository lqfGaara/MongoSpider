import random
# 导入配置文件
from scrapy.conf import settings
import base64


class MyUserAgent(object):
    def process_request(self, request, spider):
        useragent = random.choice(settings["USER_AGENTS"])
        # print(useragent)
        request.headers.setdefault("User-Agent", useragent)


class MyProxyAgent(object):
    def process_request(self, request, spider):
        proxy = random.choice(settings["PROXYS"])
        # print(proxy)
        # Set the loca、tion of the proxy
        request.meta['proxy'] = proxy['ip']
        if len(proxy['passwd']) != 0:
            # 很多网上的答案使用base64.encodestring来编码proxy_user_pass，有一种情况，当username太长的时候，会出现错误，所以推荐使用b64encode编码方式
            encodedPasswd = base64.b64encode(proxy['passwd'])
            # 有些代理是有账户和密码的，这时候就需要验证
            request.headers['Proxy_Authorization'] = 'Basic ' + encodedPasswd
