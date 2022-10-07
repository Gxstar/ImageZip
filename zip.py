import os
from PIL import Image
from PIL import ImageFile


def image_zip(file: str, out_file: str, t_size: int, step=2, quality=100):
    o_size = os.path.getsize(file) // 1024  # 返回文件大小，单位KB
    print(f'源文件大小为{o_size}KB，预期压缩到{t_size}KB。')
    if o_size <= t_size:
        print(f'已达到目标大小。')
        return Image.open(file)
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    while o_size > t_size:
        img = Image.open(file)
        img = img.convert('RGB')
        img.save(out_file, quality=quality)
        if quality - step < 0:
            break
        quality -= step
        o_size = os.path.getsize(out_file) // 1024
    print(f'文件大小：{o_size}KB')
    return img
