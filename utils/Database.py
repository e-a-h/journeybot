from peewee import MySQLDatabase, Model, PrimaryKeyField, BigIntegerField, CharField, ForeignKeyField, AutoField, \
    TimestampField, SmallIntegerField

from utils import Configuration

connection = MySQLDatabase(Configuration.get_var("DATABASE_NAME"),
                           user=Configuration.get_var("DATABASE_USER"),
                           password=Configuration.get_var("DATABASE_PASS"),
                           host=Configuration.get_var("DATABASE_HOST"),
                           port=Configuration.get_var("DATABASE_PORT"), use_unicode=True, charset="utf8mb4")


def init():
    global connection
    connection.connect()
    # connection.create_tables([])
    connection.close()
