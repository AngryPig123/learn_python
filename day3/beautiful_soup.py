from bs4 import BeautifulSoup
import requests

i = 1

study_post_list = []
while i <= 5:
    target_url = "https://www.inflearn.com"
    get = requests.get(f"{target_url}/community/studies?page={i}&order=recent")
    soup = BeautifulSoup(get.content, "html.parser")
    a_list = soup.find_all("a", "e-click-post")
    for a in a_list:
        study_post = {}
        h3_tag = a.find("h3")
        href_value = a.get('href')
        study_post["title"] = h3_tag.text.strip()
        study_post["url"] = f"{target_url}{href_value}"
        study_post_list.append(study_post)
    i = i + 1

print(len(study_post_list))
