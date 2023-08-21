from celery import shared_task
from celery.utils.log import get_task_logger
import json
from manager.models import Program
logger = get_task_logger(__name__)
from datetime import timedelta
 
@shared_task(bind=True)
def program_schedule(self, data):
    id = int(json.loads(data))
    program = Program.objects.get(id=id)
    program.start_date = (program.start_date + timedelta(days=7))
    program.end_date = (program.end_date + timedelta(days=7))
    program.save()
    logger.info("Iv'e added first")
    return 'done'