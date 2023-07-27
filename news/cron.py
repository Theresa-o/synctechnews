from django_cron import CronJobBase, Schedule
from .helpers import fetch_cronjob_news_items


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 5
    RETRY_AFTER_FAILURE_MINS = 5
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS, retry_after_failure_mins=RETRY_AFTER_FAILURE_MINS)
    code = 'news.my_cron_job'

    #fetches cronjob
    def do(self):
        fetch_cronjob_news_items()