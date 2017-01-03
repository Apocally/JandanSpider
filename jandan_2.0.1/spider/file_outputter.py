import sqlite3

class FileOutput(object):
    def __init__(self):
        self.final_dict = {}

    def collect_data(self, new_data):
        self.final_dict.update(new_data)

    def output(self):
        #values = [author, oo_num, xx_num,comment_sanitize,img_link]
        try:
            with open("all_jandan_records.html",'w',encoding='utf-8') as fl:
                fl.write('<html>')
                fl.write('''<head><meta charset="utf-8"></head>''')  #这句很重要
                fl.write('<body>')
                for each_record in self.final_dict:
                    fl.write('<p>')
                    for i in self.final_dict[each_record][3]:
                        fl.write(i)
                    fl.write('</p>')

                    fl.write('<p>')
                    for i in self.final_dict[each_record][4]:
                        fl.write(i)
                    fl.write('</p>')

                    fl.write('<p>'+ 'Author: ' + self.final_dict[each_record][0] + 'oo: ' + self.final_dict[each_record][1] + 'xx: ' + self.final_dict[each_record][2] + '</p>')
                    fl.write('<hr />')
                fl.write('</body>')
                fl.write('</html>')
        except IOError as err:
            print('File Error: ' + str(err))

    def output_to_sqlite(self):
        conn = sqlite3.connect('jandan_records.db')
        c = conn.cursor()  #创建一个cursor
        c.execute('CREATE TABLE IF NOT EXISTS jandan(id REAL, author TEXT, oo REAL, xx REAL, comment TEXT, urls TEXT)')
        for each_record in self.final_dict:
            _id = each_record
            _author = self.final_dict[each_record][0]
            _oo = self.final_dict[each_record][1]
            _xx = self.final_dict[each_record][2]
            _comment = self.final_dict[each_record][3]
            _urls = ';'.join(self.final_dict[each_record][4])
            c.execute('INSERT INTO jandan (id, author, oo, xx, comment, urls) VALUES(?,?,?,?,?,?)',
                      (_id,_author,_oo,_xx,_comment,_urls))
        conn.commit()
        c.close()
        conn.close()
        self.final_dict = {}  #清空字典
