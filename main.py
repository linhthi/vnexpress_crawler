from bs4 import BeautifulSoup
import requests
import json

categories = ['giao-duc', 'khoa-hoc', 'the-thao', 'kinh-doanh', 'suc-khoe', 'the-gioi', 
'giai-tri', 'du-lich', 'so-hoa', 'thoi-su', 'phap-luat']

for item in categories:

    url =  'https://vnexpress.net/{0}'.format(item)

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    # Fetch link of articles in a category
    link_categories = list(soup.find_all('h3', class_=["title_news", "title-news"]))
    # print(link_categories[0].prettify())

    link_articles = []
    for link in link_categories:
        link_articles.append(link.find('a')['href'])
    # print(len(link_articles))

    # Fetch content of articles
    articles = []
    for link in link_articles:
        article_page = BeautifulSoup(requests.get(link).content, 'html.parser')
        article_id = article_page.find('meta', {"name": 'its_id'})['content']
        article_author = article_page.find('meta', {"name": 'its_author'})['content']
        article_wordcount = article_page.find('meta', {"name": 'its_wordcount'})['content']
        article_updatetime = article_page.find('meta', {"name": 'article_updatetime'})['content']
        articel_publication = article_page.find('meta', {"name": 'its_publication'})['content']
        article_title = article_page.find('meta', {"name": 'its_title'})['content'].get_text()
        article_tags = article_page.find('meta', {"name": 'its_tag'})['content']
        article_content = ""
        article_contents = article_page.find_all('p', class_="Normal")
        for content in article_contents:
            article_content = article_content + " " + content.get_text()

        article = {
            "id": article_id,
            "title": article_title,
            "author": article_author,
            "updatetime": article_updatetime,
            "wordcount": article_wordcount,
            "publication": articel_publication,
            "tags": article_tags,
            "content": article_content
        }
        articles.append(article)

    print(len(articles))
    with open('./dataset_vnexpress/{0}.json'.format(item), "w") as file:
        json.dump(articles, file)





