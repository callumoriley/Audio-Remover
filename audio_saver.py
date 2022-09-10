from PythonLoopback import record_buffer
import numpy as np
import simpleaudio as sa

recording_time = int(input("Enter the recording time in seconds: "))
filename = input("Enter the output file name (with .csv): ")
input("Press enter when you want to start recording")
print("Recording")

audio_buffer = record_buffer(recording_time)

print("Buffer recorded, saving data")
print(audio_buffer)
np.savetxt(filename, audio_buffer, delimiter=',')

print("Playing recorded audio")
play_obj = sa.play_buffer(audio_buffer, 2, 2, 48000)

# Used this as a reference for how to save numpy data to a file:
# https://machinelearningmastery.com/how-to-save-a-numpy-array-to-file-for-machine-learning/
