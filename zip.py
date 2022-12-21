from os.path import getsize

import piexif
from PIL import Image
from PIL import ImageFile
import piexif as pi

# 防止图片损坏
ImageFile.LOAD_TRUNCATED_IMAGES = True


def image_zip(file: str, out_file: str, t_h: int, t_w: int, t_size: int, t_dpi: int, step=2, quality=100):
    img = Image.open(file)
    try:
        exif = piexif.load(img.info['exif'])
        exif['Exif'][41729] = b'1'
        exif_bytes = piexif.dump(exif)
    except Exception as re:
        exif_bytes = piexif.dump({})
        print(re)
    img_type = img.format
    out_file = out_file + '_r.' + img_type
    if t_h == 0:
        t_h = img.height
    if t_w == 0:
        t_w = img.width
    img = img.resize((t_w, t_h))
    # if t_dpi != 0:
    #     img.save(out_file, dpi=(t_dpi, t_dpi), quality=quality, exif=exif_bytes)
    # else:
    #     img.save(out_file, quality=quality, exif=exif_bytes)
    if t_size == 0:
        t_size = getsize(out_file) // 1024
    o_size = getsize(file) // 1024  # 返回文件大小，单位KB
    if o_size <= t_size:
        if t_dpi != 0:
            img.save(out_file, dpi=(t_dpi, t_dpi), quality=quality, exif=exif_bytes)
        else:
            img.save(out_file, quality=quality, exif=exif_bytes)
        return 1
    while o_size > t_size:
        if t_dpi != 0:
            img.save(out_file, dpi=(t_dpi, t_dpi), quality=quality, exif=exif_bytes)
        else:
            img.save(out_file, quality=quality, exif=exif_bytes)
        if quality - step < 0:
            break
        quality -= step
        o_size = getsize(out_file) // 1024
    return 1
