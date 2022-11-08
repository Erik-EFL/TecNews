from datetime import datetime
from tech_news.database import search_news
# from datetime import datetime


# Requisito 6
def search_by_title(title):
    response = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(news["title"], news["url"]) for news in response]


# Requisito 7
def search_by_date(date):
    try:
        news_date = datetime.strptime(date, "%Y-%m-%d")
        timestamp = news_date.strftime("%d/%m/%Y")
        news_dict = search_news({"timestamp": timestamp})
        return [(news["title"], news["url"]) for news in news_dict]
    except ValueError:
        raise (ValueError("Data inválida"))


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
