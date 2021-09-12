
from articlerenderer import ArticleRenderer

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    ar = ArticleRenderer()
    return ar.RenderRequestedArticle('test.txt')

if __name__ == "__main__":
    app.run()