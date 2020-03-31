import requests

class WayBackApi:
    def __init__(self, link, date):
        self.link = link
        self.date = date

    def way_back_find(self):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
            }
            r = requests.get(self.link, headers=headers,timeout = 10)
            if r.status_code == 404:
                api = 'https://archive.org/wayback/available?url=%s&timestamp=%s' % (self.link, self.date)
                archive = requests.get(api)
                snapshots = archive.json()['archived_snapshots']
                if snapshots:
                    return snapshots['closest']['url']
                else:
                    return 'dead'
            else:
                return self.link
        except requests.exceptions.RequestException as e:
            api = 'https://archive.org/wayback/available?url=%s&timestamp=%s' % (self.link, self.date)
            archive = requests.get(api)
            snapshots = archive.json()['archived_snapshots']
            if snapshots:
                return snapshots['closest']['url']
            else:
                return 'dead'
