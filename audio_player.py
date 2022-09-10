import numpy as np
import simpleaudio as sa

num_channels = int(input("Enter the number of channels of the source audio: "))
filename = input("Enter the input file name (with .csv): ")
audio_data = np.loadtxt(filename, delimiter=',').astype(int)

print(audio_data)

input("Press enter to start playing audio")

play_obj = sa.play_buffer(audio_data, num_channels, 2, 48000)
