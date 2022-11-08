from tech_news.database import search_news
# from datetime import datetime


# Requisito 6
def search_by_title(title):
    response = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(news["title"], news["url"]) for news in response]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""



# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
