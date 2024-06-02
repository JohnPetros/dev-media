from .postgresql import postgresql_database


class Peewee:
    def connect(self):
        try:
            postgresql_database.connect()
        except Exception as exception:
            print(exception)
            postgresql_database.close()
