# src/lecture05_core.py
import cv2
import os

def combine_google_and_capture(capture_img):
    """
    google.png の白い部分に capture_img を貼り付ける（同サイズにリサイズ）
    """
    google_path = os.path.join("images", "google.png")
    google_img = cv2.imread(google_path)

    if google_img is None:
        raise FileNotFoundError(f"画像ファイルが見つかりません: {google_path}")

    g_height, g_width, _ = google_img.shape

    # ★ capture_img を google.png と同じサイズへリサイズ
    resized_capture = cv2.resize(capture_img, (g_width, g_height))

    # 白色の部分だけ置換
    white = (255, 255, 255)
    mask = (google_img == white).all(axis=2)

    # mask が True の場所を capture に置換
    google_img[mask] = resized_capture[mask]

    return google_img
