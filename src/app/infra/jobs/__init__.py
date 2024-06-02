from flask_apscheduler import APScheduler

from .create_social_media_record_job import create_social_media_record_job


def init_jobs():
    scheduler = APScheduler()

    scheduler.add_job(
        func=create_social_media_record_job,
        trigger="interval",
        minutes=1,
        id="Create Social Media Record Job",
    )

    scheduler.start()
