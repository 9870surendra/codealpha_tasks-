# Task 2 - CodeAlpha Backend - URL Shortener
from flask import Flask, request, redirect
app = Flask(__name__)
urls = {}
@app.route('/shorten', methods=['POST'])
def shorten():
    data = request.get_json()
    short = str(len(urls)+1)
    urls[short] = data['url']
    return {"short_url": short}
@app.route('/<short>')
def go(short):
    return redirect(urls.get(short, "/"))
if __name__ == '__main__':
    app.run()
