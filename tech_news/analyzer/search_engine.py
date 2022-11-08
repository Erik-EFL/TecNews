from datetime import datetime
from tech_news.database import search_news


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
    dict_news = search_news(
        {"tags": {"$elemMatch": {"$regex": tag, "$options": "i"}}})
    return [(news["title"], news["url"]) for news in dict_news]


# Requisito 9
def search_by_category(category):
    dict_news = search_news(
        {"category": {"$regex": category, "$options": "i"}})
    return [(news["title"], news["url"]) for news in dict_news]
