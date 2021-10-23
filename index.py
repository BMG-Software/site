
from articlerenderer import ArticleRenderer
from eldritchxboxarticles import EldritchXboxArticles


from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/projects')
def projects():

    eldritchXboxArticles = EldritchXboxArticles()
    content = eldritchXboxArticles.GetArticlesContent()
    return render_template("page_template.html", content=content)



if __name__ == "__main__":
    app.run()