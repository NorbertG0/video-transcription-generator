import whisper

def get_transcription(filename, model):
    model = whisper.load_model(model)
    result = model.transcribe(filename, condition_on_previous_text=False)

    transcription = []

    for segment in result['segments']:
        start = segment['start']
        end = segment['end']
        text = segment['text'].strip()

        transcription.append(
            {
                'start': start,
                'end': end,
                'text': text
            }
        )

    return transcription