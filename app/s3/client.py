import logging

import boto3
from botocore.exceptions import ClientError
from flask import current_app as app


class S3client(object):
    def __init__(self):
        self.s3_bucket_name = app.config.get('S3_BUCKET_NAME')
        self.aws_access_key_id = app.config.get('AWS_ACCESS_KEY_ID')
        self.aws_secret_access_key = app.config.get('AWS_SECRET_ACCESS_KEY')
        self.aws_region_name = app.config.get('AWS_REGION_NAME')
        self.client = boto3.client('s3',
                                   aws_access_key_id=self.aws_access_key_id,
                                   aws_secret_access_key=self.aws_secret_access_key)

    def upload_file(self, file, pet_id: int) -> str:
        print('s3_client')
        key = f"{pet_id}/{file.filename}"

        try:
            self.client.upload_fileobj(file, self.s3_bucket_name, key, ExtraArgs={'ACL': 'public-read'})
        except ClientError as error:
            logging.error(error)
            raise ClientError
        
        image_file_url = f'https://{self.s3_bucket_name}.s3.{self.aws_region_name}.amazonaws.com/{key}'


        return image_file_url
