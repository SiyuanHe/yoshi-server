import os
import logging
import time

from celery import Celery
from PyPDF2 import PdfReader
from melo.api import TTS
from minio import Minio



celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")

# Speed is adjustable
speed = 1.0
device = 'cpu' # or cuda:0

text = "How about management? Do you enjoy managing people? Do you enjoy making engineering processes more efficient?"
model = TTS(language='EN', device=device)
speaker_ids = model.hps.data.spk2id


# Configure Celery logging
logger = logging.getLogger(__name__)
reader = PdfReader("example.pdf")
bucket_name = "s3bucket"



client = Minio("192.168.68.54:9002",
    access_key="3MKfP5xxrTjesMSB6Dlx",
    secret_key="J4njslXDFBsW5QF19QmHik9jqBONhmr7EUioBmq8",
    secure=False 
)
objects = client.list_objects(bucket_name)

@celery.task(name="create_task")
def create_task(fileName):
    # time.sleep(int(task_type) * 10)
    logger.info(f"Task started" + fileName)
    objects = client.list_objects(bucket_name)

    local_file_path = "/Users/siyuanhe/code/"+fileName
    # Search for the object with the specified object ID
    for obj in objects:
        if obj.object_name == fileName:
            # Retrieve the object by its name (object_name) from MinIO
            response = client.fget_object(
                bucket_name,
                obj.object_name,
                local_file_path
            )
            print(f"File '{obj.object_name}' retrieved successfully and saved to '{local_file_path}'.")
            # text=""
            for pageNum in range(10, 11):
                page = reader.pages[pageNum].extract_text().replace('-\n', '')
                page = page.replace('\n', '')
                text = page
                logger.info(page)    
            logger.info("tts start")
            output_path = fileName + '.wav'
            model.tts_to_file(text, speaker_ids['EN-US'], output_path, speed=speed)
            logger.info("tts done")
            return True
            break  # Exit the loop once the object is found

    else:
        print(f"Object with ID '{object_id}' not found in bucket '{bucket_name}'.")



    # text=""
    # for pageNum in range(10, 11):
    #     page = reader.pages[pageNum].extract_text().replace('-\n', '')
    #     page = page.replace('\n', '')
    #     text = page
    #     logger.info(page)    
    # logger.info("tts start")
    # output_path = 'test.wav'
    # model.tts_to_file(text, speaker_ids['EN-US'], output_path, speed=speed)
    # logger.info("tts done")
    return True
