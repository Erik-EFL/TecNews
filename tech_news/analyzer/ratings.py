from tech_news.database import find_news


# Requisito 10
def top_5_news():
    news_list = find_news()
    better_rating = sorted(
        news_list, key=lambda news: (-news["comments_count"], news["title"]))

    return [(news["title"], news["url"]) for news in better_rating[:5]]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
