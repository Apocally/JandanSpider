from spider import html_downloader
from spider import html_parser
from spider import file_outputter
from spider import url_manager
import time
import pickle



class SpiderMain:
    def __init__(self):
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputter = file_outputter.FileOutput()

    def craw(self, next_url):
        count = 0
        while next_url is not None:
            try:
                print('Crawing:' + next_url)
                html_cont = self.downloader.download(next_url)
                next_url, new_data = self.parser.parse(html_cont)
                self.outputter.collect_data(new_data)
                time.sleep(1)
                count += 1
            except:
                print('Craw Failed')
                count += 1
            if count == 20:
                try:
                    with open('craw_record.pickle','wb') as fl:
                        pickle.dump(next_url,fl)
                    print("Current URL  Saved successfully!")
                    self.downloader.ramdom_ver()
                    print("Version Changed Automatically")
                    self.outputter.output()
                    self.outputter.output_to_sqlite()
                    print("Data Saved!")
                    count = 0
                except IOError as err:
                    print("Save Failed..." + str(err))



if __name__ == "__main__":
    source_url = ''
    try:
        with open('craw_record.pickle','rb') as fl:
            source_url = pickle.load(fl)
    except IOError as err2:
        print("Save File Error!" + str(err2))
    if source_url == '':
        start_url = 'http://i.jandan.net/pic'
    else:
        start_url = source_url
    spider = SpiderMain()
    spider.craw(start_url)
