from flask import Flask
from flask import render_template
from mistune import html

app = Flask(__name__)

def render_markdown(markdown):
	return html(markdown)

@app.route("/")
def index():
	with open('index.md', 'r') as file:
		content = file.read()
		html_content = render_markdown(content)
		return render_template('main_site.html', page_content=html_content)
		
@app.route("/portfolio")
def portfolio():
	with open('portfolio.md', 'r') as file:
		content = file.read()
		html_content = render_markdown(content)
		return render_template('main_site.html', page_content=html_content)
		
@app.route("/cool-games")
def cool_games():
	with open('cool_games.md', 'r') as file:
		content = file.read()
		html_content = render_markdown(content)
		return render_template('main_site.html', page_content=html_content)

@app.route("/test")
def test_page():
    return "a different test page"
