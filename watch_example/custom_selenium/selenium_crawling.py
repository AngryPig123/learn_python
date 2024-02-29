import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from watch_example.py_mysql.model.my_model import UserDto, UserMovieDto

url_info = {
    'base_url': "https://pedia.watcha.com/ko-KR/users",
    'user_identifier': "ZWpqMJnbKDvrk",
    'user_movie_ratings': "contents/movies/ratings",
    'user_followings': "followings"
}

target_url = {
    'ratings_url': f"{url_info['base_url']}/{url_info['user_identifier']}/{url_info['user_movie_ratings']}",
    'followings_url': f"{url_info['base_url']}/{url_info['user_identifier']}/{url_info['user_followings']}"
}


def driver_supplier():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    return webdriver.Chrome(options=chrome_options)


def following_users():
    driver = driver_supplier()
    driver.maximize_window()
    driver.get(target_url['followings_url'])
    body = driver.find_element(By.TAG_NAME, "body")
    last_height = driver.execute_script("return document.body.scrollHeight")

    following_user_list = []

    while True:
        # key down 이벤트
        body.send_keys(Keys.PAGE_DOWN)
        # 페이지가 렌더링 되는 시간동안 대기
        time.sleep(2)
        # 현재 스크롤 높이 체크
        
        new_height = driver.execute_script("return document.body.scrollHeight")
        if last_height == new_height:
            break
        last_height = new_height

    profiles = driver.find_elements(By.CLASS_NAME, "eysnieg5")

    for profile in profiles:
        title = profile.find_element(By.TAG_NAME, "a")
        name = title.get_attribute("title")
        identifier = title.get_attribute("href").split("/")[-1]
        print(name, identifier)
        user_info = UserDto(
            name=name,
            identifier=identifier
        )
        following_user_list.append(user_info)

    driver.quit()
    return following_user_list


def user_movies(identifier):
    driver = driver_supplier()
    driver.maximize_window()
    new_user_identifier = identifier
    new_target_url = {
        'ratings_url': f"{url_info['base_url']}/{new_user_identifier}/{url_info['user_movie_ratings']}",
    }

    driver.get(new_target_url['ratings_url'])
    body = driver.find_element(By.TAG_NAME, "body")
    
    last_height = driver.execute_script("return document.body.scrollHeight")

    user_rating_list = []

    while True:
        # key down 이벤트
        body.send_keys(Keys.PAGE_DOWN)
        # 페이지가 렌더링 되는 시간동안 대기
        time.sleep(2)
        # 현재 스크롤 높이 체크
        new_height = driver.execute_script("return document.body.scrollHeight")
        if last_height == new_height:
            break
        last_height = new_height

    movies = driver.find_elements(By.CLASS_NAME, "ei3ci1h10")

    for movie in movies:
        a = movie.find_element(By.TAG_NAME, "a")
        movie_name = a.get_attribute("title")

        image = movie.find_element(By.TAG_NAME, "img")
        image_url = image.get_attribute("src")

        try:  # ToDO 점수 가져오는 부분 수정 필요.
            element = driver.find_element(
                By.CSS_SELECTOR,
                '.css-bsmapt-ContentRating-makeTypeFunction-createMediaQuery'
            )
            rating = element.text
            user_rating_list.append(
                UserMovieDto(
                    user_identifier=new_user_identifier,
                    movie_name=movie_name,
                    image_url=image_url,
                    star=rating
                )
            )
        except NoSuchElementException as ex1:
            try:
                element = driver.find_element(
                    By.CLASS_NAME, 'ei3ci1h5')
                text = element.text
                rating = float(text.split(' ')[2])
                user_rating_list.append(
                    UserMovieDto(
                        user_identifier=new_user_identifier,
                        movie_name=movie_name,
                        image_url=image_url,
                        star=rating
                    )
                )
            except NoSuchElementException as ex2:
                print("pass")

    driver.quit()
    return user_rating_list
