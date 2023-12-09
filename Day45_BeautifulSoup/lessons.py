from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_page = response.text

soup = BeautifulSoup(yc_page, "html.parser")

rows = soup.find_all(name="span", class_="titleline")
article_links = []
article_texts = []

for article in rows:
    article_texts.append(article.select_one("a").getText())
    article_links.append(article.select_one("a").get("href"))

row_scores = soup.find_all(name="span",class_="score")
web_votes = []
for score in row_scores:
    num = int(score.getText().split()[0])
    web_votes.append(num)

print(article_texts)
print(article_links)
print(web_votes)

spot = web_votes.index(max(web_votes))
print(spot)
print(f"{article_texts[spot + 1]} {article_links[spot + 1]}\n{web_votes[spot]}")

# with open("website.html", encoding="utf8") as data:
#     contents = data.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.string)
#
# # print(soup.prettify())
# # print(soup.p)
#
# all_anchor_tags = soup.find_all(name="a")
#
# # print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     # print(tag.get("href"))
#     pass
#
# heading = soup.find(name="h1", id="name")
# # print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# section_heading = soup.select_one(selector="p a")
# # print(section_heading.name)
# # print(section_heading.text)
# # print(section_heading.get("class"))
#
# company_url = soup.select_one(selector="#name")
# print(company_url)
#
# heading2 = soup.select(".heading")
# print(heading2)