from flask import Flask, render_template, request, redirect
from data import getAllData

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
    datalist = getAllData(q)
    return render_template('search.html', datalist=datalist, q=q)

@app.route('/product/')
def product(q):
    pass

# onclick="{{ url_for('app.result') }}"

if __name__ == "__main__":
    app.run()