import databases
import sqlalchemy


# Postgres Database
DATABASE_URL = 'postgresql://usertest:usertest222@db/dbtest'
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    'py_users',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.String, primary_key=True),
    sqlalchemy.Column('username', sqlalchemy.String),
    sqlalchemy.Column('email', sqlalchemy.String),
    sqlalchemy.Column('password', sqlalchemy.String),
    sqlalchemy.Column('register_date', sqlalchemy.String),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL
)
metadata.create_all(engine)
