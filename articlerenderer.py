
from articleloader import ArticleLoader

from flask import render_template

class ArticleRenderer:

    def __init__(self) -> None:
        self.articleLoader = ArticleLoader()

    def RenderRequestedArticle(self, requestedArticle : str):
        self.articleLoader.CheckForNewArticles()
        html = self.articleLoader.GetArticleHTML(requestedArticle)
        return html

