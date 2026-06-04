from flask import Flask
from flask import render_template
from mistune import html
from werkzeug.middleware.proxy_fix import ProxyFix
from task_manager import Board, Column, Card

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

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
