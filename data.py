from get_details import get_details
from get_comments import get_links

class Data:

    def __init__(self, link):
        self.name, self.image, self.price, self.rating = get_details(link)
        if (len(self.name) >= 40):
            self.name = self.name[0:38]+'...'
        self.link = link

def getAllData(key):
    return list(map(Data, get_links(key)))