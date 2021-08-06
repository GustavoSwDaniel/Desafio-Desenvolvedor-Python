from datetime import datetime


def __create_image_file_name(file) -> str:
    image_file_name = f"{datetime.now().strftime('%m%d%Y%H%M%S')}.{file.filename.split('.')[1]}"
    return image_file_name
