from flask import Flask, render_template, request, redirect
from get_comments import Data, get_keywords, get_links

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        q = request.form['search']
        return redirect(f'/search/{q}')
    return render_template('index.html')

@app.route('/search/', methods=['GET', 'POST'])
@app.route('/search/<q>', methods=['GET', 'POST'])
def search(q = None):
    if request.method == 'POST':
        q = request.form['search']
        return redirect(f'/search/{q}')
    datalist = get_links(q)
    print(len(datalist))
    return render_template('search.html', datalist=datalist, q=q)

@app.route('/product/')
def product(q):
    pass

# onclick="{{ url_for('app.result') }}"

if __name__ == "__main__":
    app.run()