from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DataBase:
    def __init__(self):
        self.conn_str = 'clickhouse://default:@db:8123/default'
        self.engine = create_engine(self.conn_str)
        self.session = sessionmaker(bind=self.engine)

    def get_session(self):
        with self.session() as session:
            yield session


db = DataBase()
DATABASE = 'news_house'
