import os

class Sagyo3:
  """
  文字起こしされた文字列を保存する

  ----------
  引数
  text : str
      文字起こしされた文字列。

  出力
  audio.txt : テキストファイル
        名前が重複していたら、audio2,3..と増える
  """

  def __init__(self, text : str):
    """
    コンストラクタ
    text : str
        文字起こしされた文字列
    """
    self.text = text
  
  def outputTextFile(self):
    """
    テキストファイルを出力

    audio.txt : テキストファイル
        名前が重複していたら、audio2,3..と増える
        テキストファイルの内容は、インスタンス変数のtext（self.text）
    """

    filename = 'audio.txt' # 基本のファイル名

    # 1. ファイル名を「名前」と「拡張子」に分離
    # (例: name='output', ext='.txt')
    name, ext = os.path.splitext(filename)

    # 2. ファイル名の候補を決定
    filename_to_use = filename
    counter = 2

    # 3. ファイルが存在する限り、新しいファイル名を試す
    # (例: 'output2.txt', 'output3.txt', ...)
    while os.path.exists(filename_to_use):
        filename_to_use = f"{name}{counter}{ext}"
        counter += 1

    # 4. 存在が確認されなかったファイル名で書き込む
    try:
        with open(filename_to_use, 'w', encoding='utf-8') as f:
            f.write(self.text)
    
    # ファイル書き込み時のエラー
    except Exception as e:
        print(f"ファイルの書き込み中にエラーが発生しました: {e}")
    