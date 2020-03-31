from lxml import etree
import datetime
import requests

class truthwiki:

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
        content = self.html.xpath("//div[@class = 'topHeading']//p//a/@href")
        for ele in content:
            if ele not in all_links:
                all_links.append(ele)
        return all_links

    def get_date(self):
        # get the date
        now_date = datetime.datetime.now()
        date = self.html.xpath("//div[@class = 'topHeading']//span/text()")[0]
        if "years"  in date or "year" in date:
            year = int(date.split(" ")[1])
            return datetime.datetime(now_date.year - year , now_date.month, now_date.day).strftime('%Y%m%d')
        elif "months" in date or "month" in date:
            month = int(date.split(" ")[1])
            return datetime.datetime(now_date.year, now_date.month - month, now_date.day).strftime('%Y%m%d')
        else:
            return now_date.strftime('%Y%m%d')
