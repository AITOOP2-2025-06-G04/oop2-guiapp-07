# src/lecture05_core.py
import cv2
import os

def combine_google_and_capture(capture_img):
    """
    google.png の白を capture_img で置換する。戻り値は合成済み画像。
    """
    google_path = os.path.join("images", "google.png")
    google_img = cv2.imread(google_path)

    if google_img is None:
        raise FileNotFoundError(f"画像ファイルが見つかりません: {google_path}")

    g_height, g_width, _ = google_img.shape
    c_height, c_width, _ = capture_img.shape

    # 白色を置換
    for y in range(g_height):
        for x in range(g_width):
            b, g, r = google_img[y, x]
            if (b, g, r) == (255, 255, 255):
                google_img[y, x] = capture_img[y % c_height, x % c_width]

    return google_img
