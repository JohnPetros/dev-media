from .sqlite import sqlite_database

from .models import DeveloperModel, SocialMediaRecordModel


class Peewee:
    def __init__(self) -> None:
        try:
            sqlite_database.connect()
            sqlite_database.create_tables([DeveloperModel, SocialMediaRecordModel])
            sqlite_database.execute_sql("DELETE FROM developers")
            sqlite_database.execute_sql(
                """
                INSERT INTO developers
                (name, github_username, twitter_username, instagram_username, youtube_channel, avatar_url)
                VALUES
                (
                'Filipe Deschamps',
                'filipedeschamps',
                'FilipeDeschamps',
                'filipedeschamps',
                'filipedeschamps',
                'https://avatars.githubusercontent.com/u/4248081?v=4'
                ),
                (
                'Gustavo Guanabara',
                'gustavoguanabara',
                'guanabara',
                'gustavoguanabara',
                'cursoemvideo',
                'https://pbs.twimg.com/profile_images/961605799830347776/Oy9Amu3w_400x400.jpg'
                ),
                (
                'Fábio Akita',
                'akitaonrails',
                'AkitaOnRails',
                'akitaonrails',
                'akitando',
                'https://pbs.twimg.com/profile_images/1362924757537193990/HhJV6tZe_400x400.jpg'
                );
                """
            )
            sqlite_database.commit()
        except Exception as exception:
            print(exception)
            sqlite_database.close()
