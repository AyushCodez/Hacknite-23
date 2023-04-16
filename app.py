from flask import Flask, render_template, request, redirect, session
from get_comments import Data, get_keywords, get_links

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
    if request.method == 'POST':
        q = request.form['search']
        return redirect(f'/search/{q}')
    datalist = get_links(q)
    for i in range(len(datalist)):
        session['link'+str(i)] = datalist[i].link
        d[datalist[i].link] = datalist[i]
        # session['name'+str(i)] = datalist[i].name
        # session['image'+str(i)] = datalist[i].image
        # session['price'+str(i)] = datalist[i].price
        # session['rating'+str(i)] = datalist[i].rating
    return render_template('search.html', dl=datalist, q=q)

# @app.route('/product/<href>/<name>/<image>/<price>/<rating>/<keyword>')
# def product(href, name, image, price, rating, keyword = None):
#     # get the value from here
#     return render_template('product.html', name=name, link=href, image=image, price=price, rating=rating, keyword=keyword)

@app.route('/product/<index>/')
@app.route('/product/<index>/<keyword>')
def product(index, keyword = None):
    link = session['link'+str(index)]
    data = d[link]
    name = data.name
    image = data.image
    price = data.price
    rating = data.rating
    # name = session['name'+str(index)]
    # image = session['image'+str(index)]
    # price = session['price'+str(index)]
    # rating = session['rating'+str(index)]
    return render_template('product.html', name=name, link=link, image=image, price=price, rating=rating, keyword=keyword)

# onclick="{{ url_for('app.result') }}"

if __name__ == "__main__":
    app.run()