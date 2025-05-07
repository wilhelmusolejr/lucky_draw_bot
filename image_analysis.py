from PIL import Image, ImageChops

import numpy as np
import cv2
import mss
import pyautogui
import os
import time

def images_are_similar(img1, path2, tolerance=5):
    if isinstance(img1, np.ndarray):
        img1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))

    img2 = Image.open(path2)

    img1 = img1.convert('RGB')
    img2 = img2.convert('RGB')

    if img1.size != img2.size:
        print("Size mismatch")
        return False

    arr1 = np.array(img1).astype(int)
    arr2 = np.array(img2).astype(int)

    diff = np.abs(arr1 - arr2)

    max_diff = np.max(diff)
    print(f"Max pixel difference: {max_diff}")

    return max_diff <= tolerance

def get_screenshot():
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        sct_img = sct.grab(monitor)
        return Image.frombytes('RGB', sct_img.size, sct_img.rgb)

# time.sleep(2)
# screenshot = get_screenshot()
# isUserNew = images_are_similar(screenshot, "images\ign.bmp", tolerance=150)
# print(isUserNew)

