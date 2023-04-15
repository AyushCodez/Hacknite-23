from get_details import get_details

class Data:

    def __init__(self, link):
        self.name, self.image, self.price, self.rating = get_details(link)
        if (len(self.name) >= 40):
            self.name = self.name[0:38]+'...'
        self.link = link

def getAllData():
    l = []
    l.append(Data(
        'https://www.amazon.in/Razer-DeathAdder-RZ01-02540100-R3M1-Essential-Optical/dp/B07F2GC4S9/ref=sr_1_5?crid=163HYHBRPY6ZU&keywords=gaming%2Bmouse&qid=1681536172&sprefix=gaming%2Bmouse%2Caps%2C264&sr=8-5&th=1'
    ))
    l.append(Data(
        'https://www.amazon.in/Levis-Mens-Jeans-18298-1253_Solid-Black_34/dp/B09Z781TTL/ref=sr_1_5?keywords=levis%2Bjeans%2Bfor%2Bmen&qid=1681536283&sprefix=levis%2Caps%2C209&sr=8-5&th=1&psc=1'
    ))
    l.append(Data(
        'https://www.amazon.in/Kill-Mockingbird-Harper-Lee/dp/0099549484/ref=sr_1_3?keywords=to+kill+a+mockingbird&qid=1681536418&s=books&sprefix=to+kill+%2Cstripbooks%2C284&sr=1-3'
    ))
    return l