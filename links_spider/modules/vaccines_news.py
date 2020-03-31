from lxml import etree
import datetime
import requests

class vaccines_news:

    def __init__(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        self.url = url
        self.homepage = "https://vaccines.news/"
        parser_html = etree.HTMLParser()
        self.html = etree.fromstring(response.content, parser_html)


    def get_all_links(self):
        # get the links
        all_links = []
        if self.url == self.homepage:
            content = self.html.xpath("//div[@class= 'Container']//a/@href")
            for ele in content:
                if ele not in all_links:
                    all_links.append("https://vaccines.news/"+ele)

        else:
            content = self.html.xpath("//div[@class='PostArticle']//p//a/@href")
            for ele in content:
                if ele not in all_links:
                    all_links.append(ele)
        return all_links

    def get_date(self):
        # get the date
        date = self.html.xpath("//div[@class='Sticky1']//span[@class = 'Date']/text()")[0]
        start_date = datetime.datetime.strptime(date, "%m/%d/%Y")
        final_date = start_date.strftime("%Y%m%d")
        return final_date