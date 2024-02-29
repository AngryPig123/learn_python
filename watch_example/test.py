from sqlalchemy import select, insert

from watch_example.custom_selenium.selenium_crawling import following_users, user_movies
from watch_example.py_mysql.config.my_connector import engine

from watch_example.py_mysql.metadata.my_metadata import user_table, user_movie_table
from watch_example.py_mysql.model.my_model import UserDto, UserMovieDto


def execute_helper(args):
    conn = engine.connect()
    _result = conn.execute(args)
    conn.commit()
    conn.close()
    return _result


def insert_user(user_data: UserDto):
    stmt = insert(user_table).values(name=user_data.name, identifier=user_data.identifier)
    execute_helper(stmt)


def insert_user_movies(user_movie: UserMovieDto):
    stmt = insert(user_movie_table).values(
        user_identifier=user_movie.user_identifier,
        movie_name=user_movie.movie_name,
        image_url=user_movie.image_url,
        star=user_movie.star
    )
    execute_helper(stmt)


# following_list = following_users()
#
# for user in following_list:
#     insert_user(user)
#

id_list = select(user_table.c.identifier).select_from(user_table)
rows = execute_helper(id_list)

for row in rows:
    user_id = row[0]
    print(user_id)
    user_movie_list = user_movies(user_id)
    for _list in user_movie_list:
        insert_user_movies(_list)
