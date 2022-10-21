import os
from PIL import Image
from PIL import ImageFile

# 防止图片损坏
ImageFile.LOAD_TRUNCATED_IMAGES = True


def image_zip(file: str, out_file: str, t_h: int, t_w: int, t_size: int, t_dpi: int, step=2, quality=100):
    img = Image.open(file)
    if t_h == 0:
        t_h = img.height
    if t_w == 0:
        t_w = img.width
    img = img.resize((t_w, t_h))
    img.convert('RGB')
    if t_dpi != 0:
        img.save(out_file, dpi=(t_dpi, t_dpi), quality=quality)
    else:
        img.save(out_file, quality=quality)
    if t_size == 0:
        t_size = os.path.getsize(out_file) // 1024
    o_size = os.path.getsize(out_file) // 1024  # 返回文件大小，单位KB
    print(f'源文件大小为{o_size}KB，预期压缩到{t_size}KB。')
    if o_size <= t_size:
        print(f'已达到目标大小。')
        img.convert('RGB')
        if t_dpi != 0:
            img.save(out_file, dpi=(t_dpi, t_dpi), quality=quality)
        else:
            img.save(out_file, quality=quality)
        return 1
    while o_size > t_size:
        img = img.convert('RGB')
        if t_dpi != 0:
            img.save(out_file, dpi=(t_dpi, t_dpi), quality=quality)
        else:
            img.save(out_file, quality=quality)
        if quality - step < 0:
            break
        quality -= step
        o_size = os.path.getsize(out_file) // 1024
    print(f'文件大小：{o_size}KB')
    return 1
