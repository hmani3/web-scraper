from flask import Blueprint, render_template, request
from .scraper import scraped

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/scrape', methods=['POST'])
def scrape():
     url = request.form['url']
     result = scraped(url)
    #  jobs = [
    #     {"title": "Software Engineer", "company": "TechCorp", "location": "Remote", "salary": "$100,000", "link": "https://example.com/job1"},
    #     {"title": "Data Scientist", "company": "Data Inc.", "location": "New York, NY", "salary": "$120,000", "link": "https://example.com/job2"},
    # ]
     return render_template('result.html', result=result)
