from pydub import AudioSegment
from spleeter.separator import Separator
import os

# Path to the directory containing video files
video_directory = '/videos'

print("Starting...")

if not os.path.exists(video_directory):
    print(f"Directory {video_directory} does not exist.")
else:
    if not os.listdir(video_directory):
        print(f"Directory {video_directory} is empty.")

print(os.listdir(video_directory))

# Iterate through video files
for filename in os.listdir(video_directory):
    print(filename)
    if filename.endswith((".mp4", ".mkv", ".m4v", ".webm")):
        filename = filename.replace(".mp4", ".mp3").replace(".mkv", ".mp3")
        video_path = os.path.join(video_directory, filename)

        # Convert video to audio
        audio = AudioSegment.from_file(video_path)
        audio_path = video_path.replace(".mp4", ".wav").replace(".mkv", ".wav").replace(".m4v", ".wav").replace(".webm", ".wav")
        audio.export(audio_path, format="wav")

        # Separate voice using Spleeter
        separator = Separator('spleeter:2stems')
        separator.separate_to_file(audio_path, '/output')

        # Load the voice file
        voice_path = os.path.join('/output', filename)
        voice_audio = AudioSegment.from_wav(voice_path)

        # Ensure the file size is less than 10MB.
        # If it's larger, you may want to reduce the quality or split the file.
        # Here, we'll just export it at a lower sample width to make it smaller.
        if len(voice_audio.raw_data) > 10 * 1024 * 1024:
            voice_audio.export(voice_path, format="mp3", sample_width=1)
