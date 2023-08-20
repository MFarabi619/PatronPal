from flask import Flask, render_template, url_for, request, redirect
import json

app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)

@app.route('/')
def dashboard():
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