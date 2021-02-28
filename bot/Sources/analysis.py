import cv2
from PIL import Image
from io import BytesIO 
import numpy as np
import tempfile
import requests
import os

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
    img = img.convert('RGB')
    img = np.asarray(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

# 画像を表示
def show(img):
    cv2.imshow('sample', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    img = cv2.imread('D:\Sourcetree\Koshoka\Resources\Order\order_001.png')
    show(img)

if __name__ == "__main__":
    main()