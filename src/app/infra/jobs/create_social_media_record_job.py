from os import getenv

from core.use_cases import create_social_media_record

developer_id = int(getenv("DEVELOPER_ID"))


def create_social_media_record_job():
    try:
        create_social_media_record.execute(developer_id)
        print("Social Media Record Created! ⏰")
    except Exception as exception:
        print(f"Create Social Media Record Job Error: {exception}")
