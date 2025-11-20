import numpy as np
import cv2
import os
import sys

# --- プロジェクトルートをパスに追加してモジュールを見つけやすくする ---
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from my_module.K24074.lecture05_camera_image_capture import MyVideoCapture



def lecture05_01():
    """google.png の白色部分をカメラ画像で置換し、新しい画像を保存する"""
    # --- Step 1: カメラキャプチャ ---
    app = MyVideoCapture()
    app.run()  # カメラ映像を表示し、'q'キーで撮影終了
    capture_img = app.get_img()

    if capture_img is None:
        print("カメラ画像が取得できませんでした。プログラムを終了します。")
        return

    # --- Step 2: Google検索画面画像を読み込み ---
    google_path = os.path.join("images", "google.png")
    google_img = cv2.imread(google_path)

    if google_img is None:
        print(f"画像ファイルが見つかりません: {google_path}")
        return

    # --- Step 3: 画像サイズ情報を取得 ---
    g_height, g_width, _ = google_img.shape
    c_height, c_width, _ = capture_img.shape
    print(f"Google画像サイズ: {g_width}x{g_height}, カメラ画像サイズ: {c_width}x{c_height}")

    # --- Step 4: 白色部分をキャプチャ画像で置換 ---
    for y in range(g_height):
        for x in range(g_width):
            b, g, r = google_img[y, x]
            if (b, g, r) == (255, 255, 255):
                google_img[y, x] = capture_img[y % c_height, x % c_width]

    # --- Step 5: 加工後の画像を保存 ---
    output_path = f"lecture05_01_K24074.png"
    cv2.imwrite(output_path, google_img)
    print(f"加工後の画像を保存しました → {output_path}")


if __name__ == "__main__":
    lecture05_01()
