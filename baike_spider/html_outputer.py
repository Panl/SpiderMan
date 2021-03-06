class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, res_data):
        if res_data is None:
            return
        self.datas.append(res_data)

    def output_html(self):
        file_out = open('output.html', 'w')
        file_out.write("<html>")
        file_out.write("<body>")
        file_out.write("<table>")
        for data in self.datas:
            file_out.write("<tr>")
            file_out.write("<td>%s</td>" % data['url'].encode('utf-8'))
            file_out.write("<td>%s</td>" % data['title'].encode('utf-8'))
            file_out.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            file_out.write("</tr>")
        file_out.write("</table>")
        file_out.write("</body>")
        file_out.write("</html>")
        file_out.close()