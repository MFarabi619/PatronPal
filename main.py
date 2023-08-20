from flask import Flask, render_template, url_for, request, redirect
import json
import requests

app_id = '3tjqahi5'

app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)

def get_kv_data(key):
    r = requests.get(f'https://keyvalue.immanuel.co/api/KeyVal/GetValue/{app_id}/{key}')
    return r.text


@app.route('/')
def dashboard():
    all_creators = get_kv_data('allcreators').split(',')
    with open(url_for('static', filename='data.json'), 'r') as f:
        cjson = json.loads(f.read())

    for creator in all_creators:
        creator_data = { 'creator': creator }
        all_ids = get_kv_data(creator).split(',')
        print(all_ids)

    return render_template('dashboard.html')


@app.route('/moreinfo')
def analytics():
    return render_template('moreinfo.html')


@app.route('/customize')
def customize():
    return render_template('customize.html')


@app.route('/history')
def history():
    return render_template('history.html')

app.run(debug=True, host='0.0.0.0')