import os
import time
import logging

from celery import Celery
from PyPDF2 import PdfReader
import time




celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")

# Configure Celery logging
logger = logging.getLogger(__name__)

reader = PdfReader("/Users/siyuanhe/code/files/example.pdf")

@celery.task(name="create_task")
def create_task(task_type):
    # time.sleep(int(task_type) * 10)
    logger.info(f"Task started")
    for pageNum in range(10, 11):
        page = reader.pages[pageNum].extract_text().replace('-\n', '')
        page = page.replace('\n', '')
        logger.info(page)    
    return True
