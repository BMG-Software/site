
from articleloader import ArticleLoader

class EldritchXboxArticles:

    def __init__(self) -> None:
        self.ELDRITCH_XBOX_ARTICLES_DIR = "./articles/eldritch_xbox_articles"
        self.ELDRITCH_XBOX_PAGE_TITLE = "<h1>Eldritch UWP/Xbox Port</h1></br></br>"
        self.article_loader = ArticleLoader(self.ELDRITCH_XBOX_ARTICLES_DIR)
        self.BuildArticleList()

    def BuildArticleList(self) -> None:
        self.articleHTML : dict = self.article_loader.GetArticleHTMLAll()

    def GetArticlesContent(self) -> str:
        content : str = self.ELDRITCH_XBOX_PAGE_TITLE
        for values in self.articleHTML.values():
            content += values
        return content