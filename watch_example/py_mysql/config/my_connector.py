from sqlalchemy import create_engine

# MySQL 연결 정보
db_username = 'root'
db_password = 'root'
db_host = '127.0.0.1'
db_port = '3306'  # MySQL의 기본 포트는 3306입니다.
db_name = 'python'

db_url = f"mysql+pymysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = create_engine(db_url)

