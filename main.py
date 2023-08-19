from flask import Flask, render_template, url_for, request, redirect
import json

app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)

@app.route('/')
def index():
    return 'hi'

app.run(debug=True, host='0.0.0.0')