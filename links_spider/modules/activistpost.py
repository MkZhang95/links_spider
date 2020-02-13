from lxml import etree
import datetime
import requests

class activistpost:

    def __init__(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        parser_html = etree.HTMLParser()
        self.html = etree.fromstring(response.content, parser_html)


    def get_all_links(self):
        # get the links
        all_links = []
        content = self.html.xpath("//div[@class = 'entry-content clearfix']//p//a/@href")
        for ele in content:
            if ele not in all_links and 'sign-up' not in ele and "activistpost" not in ele:
                all_links.append(ele)
            elif 'sign-up' in ele:
                break
        return all_links

    def get_date(self):
        # get the date
        date = self.html.xpath("//span[@class='entry-meta-date updated']/text()")[0]
        start_date = datetime.datetime.strptime(date, "%B %d, %Y")
        final_date = start_date.strftime("%Y%m%d")
        return final_date