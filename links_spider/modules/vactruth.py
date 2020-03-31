from lxml import etree
import datetime
import requests

class vactruth:

    def __init__(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        self.url = url
        self.homepage = "https://vactruth.com/"
        parser_html = etree.HTMLParser()
        self.html = etree.fromstring(response.content, parser_html)


    def get_all_links(self):
        # get the links
        all_links = []
        if self.url == self.homepage:
            content = self.html.xpath("//div[@class ='hcb-si']//a/@href")
        else:
            content = self.html.xpath("//div[@class='awr']//p//a/@href") + self.html.xpath("//div[@class='awr']//li//a/@href")
        for ele in content:
            if ele not in all_links:
                all_links.append(ele)
        return all_links

    def get_date(self):
        # get the date
        date = self.html.xpath("//div[@class='awr']//span/text()")[1].split('/')[1]
        start_date = datetime.datetime.strptime(date, " %B %d, %Y ")
        final_date = start_date.strftime("%Y%m%d")
        return final_date