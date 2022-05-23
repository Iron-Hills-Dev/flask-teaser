from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from sqlalchemy_utils import database_exists, create_database
from testcontainers.postgres import PostgresContainer

_base_ = declarative_base()


class Test(_base_):
    __tablename__ = "test"
    id = Column(Integer, primary_key=True)


with PostgresContainer("postgres:14.2") as db:
    url = db.get_connection_url()
    engine = create_engine(url)
    if not database_exists(url):
        create_database(url)

    _base_.metadata.create_all(engine)
    with Session(engine) as session:
        session.add(Test(id=1))
        session.commit()
        tests = session.query(Test)
        print(tests[0].id)
