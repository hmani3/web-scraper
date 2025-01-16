from flask import Blueprint, render_template, request
from .scraper import scrape_news

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/scrape', methods=['POST'])
def scrape():
     url = request.form['url']
     news = scrape_news(url)
     return render_template('result.html', news=news)
