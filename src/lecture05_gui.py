import sys
import cv2
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMessageBox
from PySide6.QtGui import QPixmap, QImage

from my_module.K24115.lecture05_camera_image_capture import MyVideoCapture
from src.lecture05_core import combine_google_and_capture


class Lecture05App(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lecture05 GUI Application")
        self.setGeometry(300, 200, 500, 600)

        self.capture_img = None

        # --- GUI部品 ---
        self.label_capture = QLabel("ここにカメラ画像が表示されます")
        self.label_combined = QLabel("ここに合成画像が表示されます")

        self.btn_capture = QPushButton("カメラ画像を取得")
        self.btn_combine = QPushButton("合成して表示＆保存")

        self.btn_capture.clicked.connect(self.capture_image)
        self.btn_combine.clicked.connect(self.combine_images)

        # --- レイアウト ---
        layout = QVBoxLayout()
        layout.addWidget(self.label_capture)
        layout.addWidget(self.btn_capture)
        layout.addWidget(self.label_combined)
        layout.addWidget(self.btn_combine)
        self.setLayout(layout)

    # -----------------------
    # カメラ画像の取得
    # -----------------------
    def capture_image(self):
        app = MyVideoCapture()
        app.run()
        img = app.get_img()

        if img is None:
            QMessageBox.warning(self, "エラー", "カメラ画像が取得できませんでした。")
            return

        self.capture_img = img

        # GUI に画像表示
        self.label_capture.setPixmap(self.cv_to_pixmap(img))

    # -----------------------
    # 画像合成
    # -----------------------
    def combine_images(self):
        if self.capture_img is None:
            QMessageBox.warning(self, "エラー", "先にカメラ画像を取得してください。")
            return

        try:
            combined = combine_google_and_capture(self.capture_img)
        except Exception as e:
            QMessageBox.critical(self, "エラー", str(e))
            return

        # GUIに表示
        self.label_combined.setPixmap(self.cv_to_pixmap(combined))

        # 保存も実施
        output_path = "lecture05_01_gui_output.png"
        cv2.imwrite(output_path, combined)

        QMessageBox.information(self, "保存完了", f"画像を保存しました：\n{output_path}")

    # -----------------------
    # OpenCV画像を QPixmap に変換
    # -----------------------
    def cv_to_pixmap(self, cv_img):
        h, w, ch = cv_img.shape
        bytes_per_line = ch * w
        qimg = QImage(cv_img.data, w, h, bytes_per_line, QImage.Format_BGR888)
        pix = QPixmap.fromImage(qimg).scaled(320, 240)
        return pix


def run_gui():
    app = QApplication(sys.argv)
    window = Lecture05App()
    window.show()
    sys.exit(app.exec())
