import requests
from ratelimiter import RateLimiter
from parsel import Selector
from tech_news.database import create_news


def get_news(news_selector, comments):
    return {
        "url": news_selector.css("link[rel=canonical]::attr(href)").get(),
        "title": news_selector.css("h1.entry-title::text").get().strip(),
        "timestamp": news_selector.css("li.meta-date::text").get(),
        "writer": news_selector.css("a.url.fn.n::text").get(),
        "comments_count": int(comments) if comments else 0,
        "summary": "".join(
            news_selector.css(
                "div.entry-content > p:nth-of-type(1) *::text"
            ).getall()
        ).strip(),
        "tags": news_selector.css("a[rel=tag]::text").getall(),
        "category": news_selector.css("span.label::text").get(),
    }


# Requisito 1
@RateLimiter(max_calls=1, period=1)
def fetch(url: str, wait: int = 3) -> str:
    try:
        headers = {"user-agent": "Fake user-agent"}
        response = requests.get(url, timeout=wait, headers=headers)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content: str):
    novidades = Selector(text=html_content)
    return novidades.css("a.cs-overlay-link::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    next_page = Selector(text=html_content)
    return next_page.css("a.next.page-numbers::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    comments = selector.css(
        "div.post-comments.post-comments-simple h5.title-block::text"
    ).re_first(r"\d+")
    return get_news(selector, comments)


# Requisito 5
def get_tech_news(amount):
    news_list = []
    url = fetch("https://blog.betrybe.com/")
    news_url_list = []

    while len(news_url_list) < amount:
        news_url_list.extend(scrape_novidades(url))
        if len(news_url_list) < amount:
            url = fetch(scrape_next_page_link(url))

    for news_url in news_url_list[:amount]:
        response = fetch(news_url)
        news_list.append(scrape_noticia(response))

    create_news(news_list)
    return news_list
