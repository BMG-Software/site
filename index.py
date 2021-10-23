
from articlerenderer import ArticleRenderer
from eldritchxboxarticles import EldritchXboxArticles


from flask import Flask
from flask import render_template

app = Flask(__name__, static_folder='static')

@app.route('/')
@app.route('/index')
def index():
    return render_template("page_template.html", content="<h1>Welcome!</h1>")


@app.route('/eldritch_xbox')
def projects():
    eldritchXboxArticles = EldritchXboxArticles()
    content = eldritchXboxArticles.GetArticlesContent()
    return render_template("page_template.html", content=content)


@app.route('/about')
def about():
    return render_template("page_template.html", content="<h1>About!</h1>")


@app.route('/contact')
def contact():
    return render_template("page_template.html", content="<h1>Contact!</h1>")


if __name__ == "__main__":
    app.run()