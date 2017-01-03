import urllib.request
import random

class HtmlDownloader(object):
    def __init__(self):
        self.ver = '5.1.1'
        self.phone_type = 'Galaxy Nexus'
    def download(self, next_url):
        try:
            my_header = {'User-Agent': 'Mozilla/5.0 (Linux; Android %s; %s Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19'
                         % (self.ver,self.phone_type)}
            request = urllib.request.Request(next_url, headers=my_header)
            data = urllib.request.urlopen(request)
            return data.read().decode('utf-8')
        except:
            return None

    def ramdom_ver(self):
        ver1 = str(random.randrange(2, 6))
        ver2 = str(random.randrange(0, 10))
        ver3 = str(random.randrange(0, 10))
        self.ver = ver1 + '.' + ver2 + '.' + ver3
        ran = random.randrange(0,10)
        types = ['Galaxy S4','Galaxy S5','Galaxy S6','Galaxy S7','MI 4LTE','HM NOTE 1LTE','Sony Xperia Z','Sony Xperia Z1','Sony Xperia Z2','Sony Xperia Z3']
        self.phone_type = types[ran]


