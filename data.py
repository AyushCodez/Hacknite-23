from get_details import get_details
from get_comments import get_links

class Data:

    def __init__(self, link, name, image, price, rating):
        self.link, self.name, self.image, self.price, self.rating = link, name, image, price, rating
        if (len(self.name) >= 40):
            self.name = self.name[0:38]+'...'

def getAllData(key):
    print('Getting data lol')
    return list(map(Data, get_links(key)))