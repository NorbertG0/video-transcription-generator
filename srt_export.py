import json
import srt
from datetime import timedelta

def get_srt(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    subtitles = []

    for i, segment in enumerate(data["transcription"], start=1):
        subtitles.append(
            srt.Subtitle(
                index=i,
                start=timedelta(seconds=segment["start"]),
                end=timedelta(seconds=segment["end"]),
                content=segment["text"].strip()
            )
        )

    with open("output.srt", "w", encoding="utf-8") as f:
        f.write(srt.compose(subtitles))