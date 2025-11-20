import ffmpeg
import time

output_file = 'audio.wav'

class sagyo1:
    def sagyo1(self, duration: int = 10):
        """duration秒間録音し、audio.wavに出力する。

        :param int duration: 録音する秒数.初期値:10
        :return: なし

        """
        
        try:
            (
                ffmpeg
                    .input(':0', format='avfoundation', t=duration) # macOSの例
                    .output(output_file, acodec='pcm_s16le', ar='44100', ac=1)
                    .run(overwrite_output=True)
            )

        except ffmpeg.Error as e:
                print(f"エラーが発生しました: {e.stderr.decode()}")
        except Exception as e:
            print(f"予期せぬエラー: {e}")