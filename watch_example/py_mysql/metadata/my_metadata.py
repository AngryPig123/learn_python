from sqlalchemy import MetaData, Table, Column, Integer, String, DECIMAL, ForeignKey, Text

from watch_example.py_mysql.config.my_connector import engine

metadata = MetaData()  # 테이블 정보 객체

user_table = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(255), nullable=False),
    Column('identifier', String(255), nullable=False, unique=True)
)

user_movie_table = Table(
    'user_movie',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_identifier', ForeignKey('users.identifier'), nullable=False),
    Column('movie_name', String(255)),
    Column('image_url', Text),
    Column('star', String(255))
)

metadata.create_all(engine, tables=[user_table])
metadata.create_all(engine, tables=[user_movie_table])
