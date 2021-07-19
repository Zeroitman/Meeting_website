import io
import os
from PIL import Image
from trainees.settings import STATICFILES_DIRS


def watermark_avatar(input_image_path):
    base_image = Image.open(input_image_path)
    watermark = Image.open(os.path.join(STATICFILES_DIRS[0], 'python.jpg'))
    base_image.paste(watermark, (0, 0))
    img_byte_arr = io.BytesIO()
    base_image.save(img_byte_arr, format='JPEG')
    return io.BytesIO(img_byte_arr.getvalue())

