import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
# This option
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

url_info = {
    'base_url': "https://pedia.watcha.com/ko-KR/users",
    'user_identifier': "ZWpqMJnbKDvrk",
    'user_movie_ratings': "contents/movies/ratings",
    'user_followings': "followings"
}

target_url = {
    'ratings_url': f"{url_info['url_info']}/{url_info['user_identifier']}/{url_info['user_movie_ratings']}",
    'followings_url': f"{url_info['url_info']}/{url_info['user_identifier']}/{url_info['user_followings']}"
}

# web 사이트를 연다.

driver.get(target_url['followings_url'])
# 초기 body 요소 체크
body = driver.find_element(By.TAG_NAME, "body")

# 초기 스크롤 위치 기억
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # key down 이벤트
    body.send_keys(Keys.PAGE_DOWN)
    # 페이지가 렌더링 되는 시간동안 대기
    time.sleep(2)
    # 현재 스크롤 높이 체크
    new_height = driver.execute_script("return document.body.scrollHeight")
    if last_height == new_height:
        print("더 이상 페이지 다운할 내용이 없습니다.")
        break
    last_height = new_height

driver.quit()
