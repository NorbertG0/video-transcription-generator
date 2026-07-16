import subprocess

def mp4_to_wav(file_name):
    output = file_name.rsplit(".", 1)[0] + ".wav"

    subprocess.run([
        "ffmpeg",
        "-i", file_name,
        "-vn",
        "-ac", "1",
        "-ar", "16000",
        "-af", "highpass=f=200,lowpass=f=3000",
        output
    ])

    return output
