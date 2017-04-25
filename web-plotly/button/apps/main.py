# Flask などの必要なライブラリをインポートする
from flask import Flask, render_template, request, redirect, url_for

import json
import plotly
import plotly.graph_objs as go

app = Flask(__name__)
app.debug = True
counter = 0
Suki = 0
Bimyo = 0
Kirai = 0

@app.route('/')
def index():
    title = "ようこそ"
    return render_template('index.html',
                           title=title)

# /post にアクセスしたときの処理
@app.route('/post', methods=['GET', 'POST'])
def post():
    title = "こんにちは"
    if request.method == 'POST':
        # リクエストフォームから「名前」を取得して
        name = request.form['name']
        # index.html をレンダリングする
        return render_template('index.html',
                               name=name, title=title)
    else:
        # エラーなどでリダイレクトしたい場合はこんな感じで
        return redirect(url_for('index'))

# /get にアクセスしたときの処理
@app.route('/get', methods=['GET', 'POST'])
def get():
    title = "こんにちは"
    global counter
    global Suki
    global Bimyo
    global Kirai
    counter += 1
    if request.method == 'GET':
        # リクエストフォームから「fun」を取得して
        howlike = request.args.get('fun', '')
        print(howlike)
        if howlike == 'Y':
            Suki += 1
        elif howlike == 'X':
            Bimyo += 1
        elif howlike == 'N':
            Kirai += 1

        graphs = [
            dict(
                data=[
                    dict(
                        labels=['Suki', 'Bmyo', 'Kirai'],
                        values=[Suki, Bimyo, Kirai],
                        type='pie'
                    ),
                ],
                layout=dict(
                    title='We love Microsoft'
                )
            )
        ]
        # Add "ids" to each of the graphs to pass up to the client
        # for templating
        ids = ['graph-{}'.format(i) for i, _ in enumerate(graphs)]

        # Convert the figures to JSON
        # PlotlyJSONEncoder appropriately converts pandas, datetime, etc
        # objects to their JSON equivalents
        graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

        # index.html をレンダリングする
        return render_template('index.html',
                               howlike=howlike,
                               ids=ids,
                               graphJSON=graphJSON,
                               counter=counter, 
                               title=title)
    else:
        # エラーなどでリダイレクトしたい場合はこんな感じで
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
