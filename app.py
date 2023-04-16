from flask import Flask, render_template, request, redirect, session
from get_comments import Data, get_keywords, get_links
from key_sentiment import get_sent

app = Flask(__name__)
app.secret_key = 'd902mEFm/-1290?-=12iod932m'
d = {}

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        q = request.form['search']
        return redirect(f'/search/{q}')
    return render_template('index.html')

@app.route('/search/<q>', methods=['GET', 'POST'])
def search(q = None):
    session.pop('words', None)
    if request.method == 'POST':
        q = request.form['search']
        return redirect(f'/search/{q}')
    datalist = get_links(q)
    for i in range(len(datalist)):
        session['link'+str(i)] = datalist[i].link
        d[datalist[i].link] = datalist[i]
    return render_template('search.html', dl=datalist, q=q)

@app.route('/product/<index>/', methods=['GET', 'POST'])
@app.route('/product/<index>/<keyword>/', methods=['GET', 'POST'])
def product(index: int, keyword=None):
    if request.method == 'POST':
        q = request.form['keyword']
        return redirect(f'/product/{index}/{q}')
    link = session['link'+str(index)]
    data = d[link]
    name = data.name
    image = data.image
    price = data.price
    rating = data.rating
    try:
        words = session['words']
    except:
        words = get_keywords(link)
        session['words'] = words
    if (not keyword and words):
        val = get_sent(link, [words[0]])
        keyword = words[0]
    else:
        val = get_sent(link, [keyword])
    print('----------------------------'+index+'----------------------------')
    print('----------------------------'+keyword+'----------------------------')
    return render_template('product.html', name=name, link=link, image=image, price=price, rating=rating, keyword=keyword, wordlist=words, val=val, get_sent=get_sent)

# onclick="{{ url_for('app.result') }}"

if __name__ == "__main__":
    app.run()