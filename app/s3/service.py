from datetime import datetime

from app.pets import service as pet_service
from app.s3.client import S3client


def __create_image_file_name(file) -> str:
    image_file_name = f"{datetime.now().strftime('%m%d%Y%H%M%S')}.{file.filename.split('.')[1]}"
    return image_file_name


def upload_image(pet_id: int, file) -> str:
    pet = pet_service.get_pet_by_id(pet_id=pet_id)
    file.name = __create_image_file_name(file)
    pet.pet_photo = S3client().upload_file(file=file, pet_id=pet_id)
    return pet_service.save_pet(pet=pet)
