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
    print(r.text[1:-1])
    return r.text[1:-1]


@app.route('/')
def dashboard():
    all_creators = get_kv_data('allcreators').split(',')
    with open('static/data.json', 'r') as f:
        cjson = json.loads(f.read())

    for creator in all_creators:
        print(creator)
        all_ids = get_kv_data(creator).split(',')
        all_ids = [e for e in all_ids if e != '']
        print(all_ids)
        cjson['watch'][creator] = {}
        for id in all_ids:
            cjson['watch'][creator][id] = int(get_kv_data(id))
    
    with open('static/data.json', 'w+') as f:
        f.truncate(0)
        f.write(json.dumps(cjson, indent=4))

    watch_data = {}

    tot_sec = 0

    for creator in cjson['watch']:
        watch_data[creator] = 0
        for id in cjson['watch'][creator]:
            watch_data[creator] += cjson['watch'][creator][id]
        if watch_data[creator] == 0:
            del watch_data[creator]
        else:
            tot_sec += watch_data[creator]
        
        
    for creator in watch_data:
        watch_data[creator] = round(watch_data[creator] / tot_sec * 15, 2)

    print(watch_data)

    return render_template('dashboard.html', watch_data=watch_data)


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