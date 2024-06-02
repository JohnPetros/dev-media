from .peewee import Peewee
from .peewee.repositories import DevelopersRepository, SocialMediaRecordsRepository

developers_repository = DevelopersRepository()
social_media_records_repository = SocialMediaRecordsRepository()


def init_database():
    peewee = Peewee()
    peewee.connect()
