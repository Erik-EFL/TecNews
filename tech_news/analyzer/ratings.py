from tech_news.database import find_news


# Requisito 10
def top_5_news():
    news_list = find_news()
    better_rating = sorted(
        news_list, key=lambda news: (-news["comments_count"], news["title"]))

    return [(news["title"], news["url"]) for news in better_rating[:5]]


# Requisito 11
def top_5_categories():
    news_list = find_news()
    categories = {}
    for news in news_list:
        if news["category"] in categories:
            categories[news["category"]] += 1
        else:
            categories[news["category"]] = 1

    better_rating = sorted(
        categories.items(), key=lambda category: (-category[1], category[0]))

    return [category[0] for category in better_rating[:5]]
