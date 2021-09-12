
from articleloader import ArticleLoader

from flask import render_template

class ArticleRenderer:

    def __init__(self) -> None:
        self.articleLoader = ArticleLoader()
        self.articleLoader.WatchForArticleChanges()

    def RenderRequestedArticle(self, requestedArticle : str):
        html = self.articleLoader.GetArticleHTML(requestedArticle)
        return render_template(html)

