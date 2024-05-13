# from melo.api import TTS
# from PyPDF2 import PdfReader

from minio import Minio

client = Minio("192.168.68.54:9002",
    access_key="3MKfP5xxrTjesMSB6Dlx",
    secret_key="J4njslXDFBsW5QF19QmHik9jqBONhmr7EUioBmq8",
    secure=False 
)

print("in here")
bucket_name = "s3bucket"
object_id = "KkAda-example.pdf" 


# List objects in the specified bucket
objects = client.list_objects(bucket_name)

local_file_path = "/Users/siyuanhe/code/"+object_id
# Search for the object with the specified object ID
for obj in objects:
    if obj.object_name == object_id:
        # Retrieve the object by its name (object_name) from MinIO
        response = client.fget_object(
            bucket_name,
            obj.object_name,
            local_file_path
        )
        print(f"File '{obj.object_name}' retrieved successfully and saved to '{local_file_path}'.")
        break  # Exit the loop once the object is found

else:
    print(f"Object with ID '{object_id}' not found in bucket '{bucket_name}'.")



# speed = 0.8
# device = 'cpu' # or cuda:0

# text = "我最近在学习machine learning，希望能够在未来的artificial intelligence领域有所建树。"
# model = TTS(language='ZH', device=device)
# speaker_ids = model.hps.data.spk2id

# output_path = 'test.wav'
# model.tts_to_file(text, speaker_ids['ZH'], output_path, speed=speed)
