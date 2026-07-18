FROM python:3.12-slim
LABEL authors="ngajd"

RUN apt update && apt install -y ffmpeg

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install torch --index-url https://download.pytorch.org/whl/cpu

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]