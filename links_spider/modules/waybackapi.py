import requests

class WayBackApi:
    def __init__(self, link, date):
        self.link = link
        self.date = date

    def way_back_find(self):
        try:
            r = requests.get(self.link)
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