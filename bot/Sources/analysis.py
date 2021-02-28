from PIL import Image
import cv2
import math
import numpy as np
import my_image

def template_matching(template, img):
    template = my_image.ImageToArray(template)
    img = my_image.ImageToArray(img)

    # グレースケール化
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    threshold = 210
    ret, template = cv2.threshold(template, threshold, 255, cv2.THRESH_BINARY)
    ret, img = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)

    detector = cv2.AKAZE_create()
    
    # 特徴量の検出と特徴量ベクトルの計算
    kp1, des1 = detector.detectAndCompute(template, None)
    kp2, des2 = detector.detectAndCompute(img, None)

    template = cv2.drawKeypoints(template, kp1, None, flags=4)
    img = cv2.drawKeypoints(img, kp2, None, flags=4)

    # Brute-Force Matcherの生成
    bf = cv2.BFMatcher()

    # 特徴量ベクトル同士をBrute-Force＆KNNでマッチング
    matches = bf.knnMatch(des1, des2, k=2)

    # データを間引く
    ratio = 0.2
    good = []
    for m, n in matches:
        if m.distance < ratio * n.distance:
            good.append([m])

    result = cv2.drawMatchesKnn(template, kp1, img, kp2, good[:2], None, flags=2)

    cv2.imshow('sample', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return

def main():    
    template = Image.open('../Resources/Order/3.png')
    img = Image.open('../Resources/Test/test.png')
    template_matching(template, img)

if __name__ == "__main__":
    main()