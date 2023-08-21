# from django.db.models.signals import post_save,pre_save,post_delete
# from django.dispatch import receiver
# from django_celery_beat.models import PeriodicTask, CrontabSchedule
# from manager.models import Program
# import json
# from django.utils import timezone

# @receiver(post_save, sender=Program)
# def create_program_crontab(sender, instance, created, **kwargs):
#     if created:
#         schedule = CrontabSchedule.objects.create(hour=instance.end_date.hour, minute=instance.end_date.minute,day_of_month =instance.end_date.day,month_of_year = instance.end_date.month)
#         task,created_task = PeriodicTask.objects.update_or_create(crontab=schedule,name=f'program{instance.id}_scheduler',task='notify.tasks.program_schedule',args=json.dumps((f'{instance.id}',)))


# @receiver(post_delete, sender=Program)
# def delete_program_crontab(sender, instance, **kwargs):
#     if PeriodicTask.objects.filter(name=f'program{instance.id}_scheduler').exists():
#       PeriodicTask.objects.get(name=f'program{instance.id}_scheduler').delete()

