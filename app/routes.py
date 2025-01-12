from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)

@main.route('/home')
def home():
    return render_template('index.html')

# @main.route('/scrape', methods=['POST'])
# def scrape():
#     url = request.form['url']
#     news = scrape_news(url)
#     return render_template('results.html', news=news)
