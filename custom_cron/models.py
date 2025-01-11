from django.db import models
from django_cron.models import CronJobLog as OriginalCronJobLog

class CronJobLog(OriginalCronJobLog):
    # No need to define indexes here
    pass


