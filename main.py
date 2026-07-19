import os
import json
from datetime import datetime

from audio import mp4_to_wav
from download import download_clip
from transcription import get_transcription


url = input("Enter clip URL: ")
model = "medium" #tiny, small, medium, large


def delete_file(filename):
    if filename and os.path.exists(filename):
        os.remove(filename)


mp4_file = None
wav_file = None

try:
    mp4_file = download_clip(url)
    print(f"[INFO] Downloaded: {mp4_file}")

    wav_file = mp4_to_wav(mp4_file)
    print(f"[INFO] Converted: {wav_file}")

    transcription = get_transcription(wav_file, model)
    print("[INFO] Transcription finished")

    data = {
        "metadata": {
            "created_at": datetime.now().isoformat(),
            "model": model,
            "filename": wav_file,
        },
        "transcription": transcription
    }

    with open("transcription.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("[INFO] Saved JSON")


except Exception as e:
    print(f"[ERROR] {e}")


finally:
    delete_file(mp4_file)
    delete_file(wav_file)

    print("[INFO] Temporary files cleaned")