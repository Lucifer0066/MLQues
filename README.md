# MLQues

1. The script starts by importing the required libraries, including os and pydub.
2. It sets the input and output directories using the input_dir and output_dir variables.
3. It checks if the output directory exists and creates it if it doesn't.
4. It loops through each file in the input directory and checks if it has a .mp3 extension.
5. If it does, it loads the file using the AudioSegment.from_mp3 method and converts it to WAV format using the export method.
6. It creates the output file path by replacing the .mp3 extension with .wav.
7. Finally, it saves the WAV file in the output directory.
