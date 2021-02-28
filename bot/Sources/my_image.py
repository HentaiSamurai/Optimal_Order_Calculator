import os
from io import BytesIO 
import numpy as np
import tempfile
from PIL import Image
import cv2
import requests

def ImageToArray(img):
    cv_img = img.convert('RGB')
    cv_img = np.asarray(cv_img)
    cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
    return cv_img

# Web上の画像を読み込み
def imread_web(url, timeout = 10):
    res = requests.get(url, timeout=timeout)
    img = None

    if res.status_code != 200:
        e = Exception("HTTP status: " + res.statsu_code)
        raise e

    content_type = res.headers["content-type"]
    if 'image' not in content_type:
        e = Exception("Content-Type: " + content_type)
        raise e

    img = Image.open(BytesIO(res.content))
    return img

# 画像を表示
def show(img):
    img = ImageToArray(img)
    cv2.imshow('sample', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 画像を分割
def split(img, col_count, row_count):
    img_w, img_h = img.size
    res_w = int(img_w / col_count)
    res_h = int(img_h / row_count)
    splits = list()
    print(img.size, res_w, res_h)

    for r in range(row_count):
        for c in range(col_count):
            x = c * res_w
            y = r * res_h
            print((x, y, x + res_w, y + res_h))
            splits.append(img.crop((x, y, x + res_w, y + res_h)))
    return splits