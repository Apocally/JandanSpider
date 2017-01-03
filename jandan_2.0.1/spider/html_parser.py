from bs4 import BeautifulSoup


class HtmlParser(object):
    def parse(self, html_cont):
        try:
            pic = {}
            soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
            #<a class="previous-comment-page" href="http://i.jandan.net/pic/page-8527#comments" title="Older Comments">»</a>
            next_page = soup.find('a',class_="previous-comment-page")
            next_url = next_page['href']
            #<ol class="commentlist" >   # 每一页图的node
            pic_list = soup.find('ol', class_="commentlist").find_all('li')
            for each_node in pic_list:
                try:  #中途失败了一次 导致跳出，故再加一个try
                    values = []
                    pic_num = str(each_node.find('span', class_='righttext').find('a').get_text()) #获得每一组图的id

                    author = each_node.find('b').get_text() #获得每一组图的作者

                    # [<span id="cos_support-3073580">39</span>] ,[<span id="cos_unsupport-3073580">6</span>] 支持与反对的代码
                    oo_id = 'cos_support-' + pic_num
                    xx_id = 'cos_unsupport-' + pic_num
                    oo_num = each_node.find('span',id=oo_id).get_text()
                    xx_num = each_node.find('span',id=xx_id).get_text()  #获得每一张图的oo与xx数量

                    #<a href="http://ww2.sinaimg.cn/large/a801236bjw1f1d5ut8a8uj20gu0nzdh3.jpg" target="_blank" class="view_img_link">[查看原图]</a>
                    img_set = each_node.find_all('a',class_="view_img_link") #获得每一张图的链接
                    img_links = []
                    img_link = []
                    for each_img_tag in img_set:
                        img_links.append(str(each_img_tag['href']))
                    for each_link in img_links:
                        img_link.append(str(each_link))

                    comment = each_node.p.get_text()
                    comment_sanitize = comment.replace('[查看原图]','').strip()


                    #使用一个字典保存
                    keys = str(pic_num)
                    values = [author, oo_num, xx_num,comment_sanitize,img_link]
                    pic[keys] = values
                except:
                    pass

            print(pic)
            return next_url, pic

        except:
            return None
