from .postgresql import postgresql_database
from .models import DeveloperModel, SocialMediaRecordModel


class Peewee:
    def connect(self):
        try:
            postgresql_database.connect()
            postgresql_database.create_tables([DeveloperModel, SocialMediaRecordModel])
            postgresql_database.execute_sql("DELETE FROM developers")
            postgresql_database.execute_sql(
                """
               INSERT INTO developers 
                (
                    id, 
                    name, 
                    github_username, 
                    twitter_username, 
                    instagram_username, 
                    youtube_channel, 
                    avatar_url
                ) 
                VALUES 
                (
                    1,
                    'Felipe Deschamps',
                    'filipedeschamps',
                    'FilipeDeschamps',
                    'filipedeschamps',
                    'filipedeschamps',
                    'https://avatars.githubusercontent.com/u/4248081?v=4'
                ),
                (
                    2,
                    'Gustavo Guanabara',
                    'gustavoguanabara',
                    'guanabara',
                    'gustavoguanabara',
                    'cursoemvideo',
                    'https://pbs.twimg.com/profile_images/961605799830347776/Oy9Amu3w_400x400.jpg'
                ),
                (
                    3,
                    'Fábio Akita',
                    'akitaonrails',
                    'AkitaOnRails',
                    'akitaonrails',
                    'akitando',
                    'https://pbs.twimg.com/profile_images/1362924757537193990/HhJV6tZe_400x400.jpg'
                );

                """
            )

        except Exception as exception:
            print(exception)
            postgresql_database.close()
