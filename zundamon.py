import csv
import pathlib
import requests
import json
import wave
import sys
from pref import prefecture

# VOICEVOXのエンドポイント
BASE_URL = "http://localhost:50021"

# テキストを音声に変換する関数
def text_to_speech(text, speaker=3):
    # 音声合成用のクエリを作成
    query_payload = {"text": text, "speaker": speaker}
    query_response = requests.post(f"{BASE_URL}/audio_query", params=query_payload)
    query_data = query_response.json()

    # 音声合成
    synthesis_payload = {"speaker": speaker}
    synthesis_response = requests.post(
        f"{BASE_URL}/synthesis",
        headers={"Content-Type": "application/json"},
        params=synthesis_payload,
        data=json.dumps(query_data)
    )

    return synthesis_response.content[100:]

def main():
    for p in prefecture.values():
        audio = text_to_speech(p)
        save_mp3( audio, f"mp3/{p}.mp3")

def save_mp3(audio_data, output_path):
    import pydub
    from pydub import AudioSegment
    import io

    # Convert the raw audio data to an AudioSegment
    audio_segment = AudioSegment.from_raw(io.BytesIO(audio_data), sample_width=2, frame_rate=24000, channels=1)

    # Export the AudioSegment as an MP3 file
    audio_segment.export(output_path, format="mp3")


# WAVファイルとして保存する関数
def save_wav(audio_data, output_path):
    with wave.open(output_path, "wb") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(24000)
        wav_file.writeframes(audio_data)

# メイン処理
if __name__ == "__main__":
    main()
