# Zoom Meeting Minutes Creator

This script allows you to automatically transcribe Zoom meeting audio files (in `.m4a` format) using the Deepgram Speech-to-Text API. It also converts `.m4a` files to `.mp3` format before transcription.

## Features

- Converts Zoom `.m4a` audio files to `.mp3`
- Sends audio to Deepgram for transcription
- Prints the transcribed text to the console

## Prerequisites

- Python 3.7+
- A Deepgram API Key. You can sign up and generate an API key at [Deepgram Console](https://console.deepgram.com/).

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/zoom-meeting-minutes-creator.git
   cd zoom-meeting-minutes-creator


2. **Install Dependencies:**

   It is recommended to use a virtual environment.

   ```bash
   pip install -r requirements.txt
   ```

   **Required Packages:**

   * `requests`
   * `pydub`

3. **Install FFmpeg (Required for pydub):**

   * **macOS (Homebrew):** `brew install ffmpeg`
   * **Ubuntu/Debian:** `sudo apt install ffmpeg`
   * **Windows:** Download from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html) and add to your system PATH

## Configuration

Open the script and replace the placeholder `YOUR_API_KEY` with your actual Deepgram API Key:

```python
DEEPGRAM_API_KEY = "YOUR_API_KEY"
```

## Usage

```bash
python app.py <audio_file_path.m4a>
```

### Example

```bash
python app.py meeting_audio.m4a
```

### Output

* The script converts `meeting_audio.m4a` to `meeting_audio.mp3`
* Sends the `.mp3` file to Deepgram
* Prints the transcribed text to the console

## Notes

* Ensure the `.m4a` audio file is clear for optimal transcription results.
* The Deepgram free tier has usage limits. Refer to [Deepgram Pricing](https://deepgram.com/pricing) for more details.

## Author

* [Nikunj Parmar](https://github.com/NikunjCitrusbug)


