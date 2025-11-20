import numpy as np
import cv2


class MyVideoCapture:
    """
    Webカメラから映像を取得し、中心にターゲットマークを描画して表示するクラス。
    """

    DELAY: int = 100  # 100ms間隔でフレーム更新

    def __init__(self) -> None:
        """Webカメラを初期化"""
        self.cap: cv2.VideoCapture = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.captured_img: np.ndarray | None = None

    def run(self) -> None:
        """カメラ映像を表示し、'q'キーで撮影終了"""
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("カメラ映像の取得に失敗しました。")
                break

            img = np.copy(frame)

            # 中心に赤いターゲットマークを描画
            rows, cols, _ = img.shape
            center = (cols // 2, rows // 2)
            color = (0, 0, 255)
            thickness = 3
            cv2.circle(img, center, 30, color, thickness)
            cv2.circle(img, center, 60, color, thickness)
            cv2.line(img, (center[0] - 80, center[1]), (center[0] + 80, center[1]), color, thickness)
            cv2.line(img, (center[0], center[1] - 80), (center[0], center[1] + 80), color, thickness)

            # 左右反転して表示
            img = cv2.flip(img, 1)
            cv2.imshow("Camera (press 'q' to capture)", img)

            # qキーで撮影終了
            if cv2.waitKey(self.DELAY) & 0xFF == ord("q"):
                self.captured_img = frame
                break

    def get_img(self) -> np.ndarray | None:
        """最後にキャプチャされた画像を返す"""
        return self.captured_img

    def __del__(self) -> None:
        """終了処理"""
        if hasattr(self, "cap") and self.cap.isOpened():
            self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    app = MyVideoCapture()
    app.run()
    img = app.get_img()

    if img is not None:
        print("キャプチャ成功:", img.shape)
    else:
        print("キャプチャに失敗しました。")
