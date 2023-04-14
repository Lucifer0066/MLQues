import os
from pydub import AudioSegment

# Set the directory where the MP3 files are located
input_dir = 'input/'

# Set the directory where the WAV files will be saved
output_dir = 'output/'

# Check if the output directory exists, if not create it
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop through each file in the input directory
for file_name in os.listdir(input_dir):
    if file_name.endswith('.mp3'):
        # Load the MP3 file
        mp3_path = os.path.join(input_dir, file_name)
        sound = AudioSegment.from_mp3(mp3_path)

        # Create the output file path and save the file
        wav_path = os.path.join(output_dir, file_name.replace('.mp3', '.wav'))
        sound.export(wav_path, format='wav')
