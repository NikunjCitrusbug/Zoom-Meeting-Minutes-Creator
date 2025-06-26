import sys

import requests
from pydub import AudioSegment

# Replace with your Deepgram API key
DEEPGRAM_API_KEY = "YOUR_API_KEY"

# Convert m4a to mp3
def convert_m4a_to_mp3(input_path, output_path):
    audio = AudioSegment.from_file(input_path, format="m4a")
    audio.export(output_path, format="mp3")
    return output_path

# Function to transcribe audio using Deepgram
def transcribe_audio(audio_file_path):
    url = "https://api.deepgram.com/v1/listen"
    headers = {
        "Authorization": f"Token {DEEPGRAM_API_KEY}"
    }

    
    with open(audio_file_path, "rb") as audio_file:
        response = requests.post(url, headers=headers, files={"file": audio_file})
        
    if response.status_code == 200:
        transcript = response.json().get("results", {}).get("channels", [])[0].get("alternatives", [])[0].get("transcript", "")
        return transcript
    else:
        print("Error:", response.json())
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python transcribe.py <audio_file_path.m4a>")
        sys.exit(1)

    m4a_path = sys.argv[1]
    mp3_path = m4a_path.replace(".m4a", ".mp3")

    print("Converting M4A to MP3...")
    convert_m4a_to_mp3(m4a_path, mp3_path)

    print("Sending MP3 to Deepgram for transcription...")
    transcription = transcribe_audio(mp3_path)

    if transcription:
        print("Transcription:")
        print(transcription)
    else:
        print("Transcription failed.")
