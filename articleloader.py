
from os import listdir
from os.path import isfile, join, getmtime
import threading
from markdown import markdown

class ArticleLoader:

    def __init__(self) -> None:
        self.ARTICLES_DIR = '.\\articles'
        self.CHECK_INTERVAL = 30.0 # Seconds
        self.articleInfo = {}
        self.articleHTML = {}

    def GetArticleHTML(self, articleFilename : str) -> str:
        try:
            return self.articleHTML[articleFilename]
        except:
            return ''

    def MarkdownArticleToHTML(self, articleFilename : str) -> str:
        articleMarkdownText = ''
        with open(articleFilename, 'r') as articleFile:
            for line in articleFile.readlines():
                articleMarkdownText += line
        return markdown(articleMarkdownText)

    def LoadArticles(self, articlesDir : str) -> dict:
        articleInfo = {}
        articleNames = [f for f in listdir(articlesDir) if isfile(join(articlesDir, f))]
        for articleName in articleNames:
            articleInfo[articleName] = getmtime(join(articlesDir, articleName))        
        return articleInfo

    def CheckForAdditions(self, latestArticles : dict) -> list:
        toAdd = []
        # Check for additions to the dir or updates to articles
        for articleName, lastModified in latestArticles.items():
            if articleName in self.articleInfo.keys():
                if lastModified > self.articleInfo[articleName]:
                    toAdd.append(articleName)
            else:
                toAdd.append(articleName)

        return toAdd

    def CheckForDeletions(self, latestArticles : dict) -> list:
        toDelete = []
        # Check for article deletions
        for articleName in self.articleInfo.keys():
            if articleName not in latestArticles.keys():
                # Article has been removed
                toDelete.append(articleName)

        return toDelete

    def WatchForArticleChanges(self) -> None:
        threading.Timer(self.CHECK_INTERVAL, self.WatchForArticleChanges).start()
        latestArticles = self.LoadArticles(self.ARTICLES_DIR)
        toAdd = self.CheckForAdditions(latestArticles)
        if len(toAdd) > 0:
            for f in toAdd:
                self.articleHTML[f] = self.MarkdownArticleToHTML(self.ARTICLES_DIR + "\\" + f)
        toDelete = self.CheckForDeletions(latestArticles)
        if len(toDelete) > 0:
            for f in toDelete:
                print(f)
        self.articleInfo = latestArticles
        return self.articleHTML
        

if __name__ == "__main__":
    al = ArticleLoader()

    al.WatchForArticleChanges()
    