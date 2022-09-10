# Audio-Remover
A program to remove known audio (like music) from a sample of audio.

## Requirements
- NumPy
- Simpleaudio
- PythonLoopback

## Usage
1. Using audio_saver.py, record a sample of the original audio (with known audio and other audio). Set the filename to original.csv and set the duration pretty low (I like 3 seconds)
2. Using audio_saver.py, record a sample of the known audio from a source. Set the filename to subtract.csv and set the duration lower than that of original.csv (I like 1 second)
3. Run the audio_remover.py script. Once it is done, it will play the final audio and save it as a CSV file to final.csv
4. Play the final.csv file with audio_player.py. Remember to set the number of channels to 1 (audio is initially recorded as stereo, but to make processing easier only one channel is used, and it only saves one final channel as of now)
