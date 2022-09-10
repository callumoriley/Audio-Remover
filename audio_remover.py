import numpy as np
import simpleaudio as sa

def rms(np_arr): # https://stackoverflow.com/questions/40963659/root-mean-square-of-a-function-in-python
    return np.sqrt(np.mean(np_arr**2))

# load the recorded audio streams (generate them with audio_saver.py)
original_raw = np.loadtxt('original.csv', delimiter=',').astype(int) # audio to be subtracted from
subtract_raw = np.loadtxt('subtract.csv', delimiter=',').astype(int) # audio to subtract

original = original_raw[:, 0] # get one channel of each audio stream
subtract = subtract_raw[:, 0]

min_rms = 10000000000
min_index = -1

range_top = original.size - subtract.size # note: original audio should be larger than subtract audio
print("CURRENT_ITERATION/ITERATIONS PERCENT_COMPLETE MIN_RMS MIN_INDEX")
for i in range(0, range_top):
    print("                                                                                      ", end="\r")
    print(f"{i}/{range_top} {100*i/range_top:.2f}% {min_rms:.2f} {min_index}", end="\r")
    subtract_padded = np.concatenate(
        [np.zeros(i),
        subtract,
        np.zeros(original.size - i - subtract.size)]) # create a padded version of the subtract array so it can be subtracted from the original

    diff_arr = original - subtract_padded # subtract the two arrays
    current_rms = rms(diff_arr)
    if current_rms < min_rms: # if the overall amplitude is low, then make this the spot to stop (when the amplitude is the lowest, the audios will have cancelled each other out)
        min_rms = current_rms
        min_index = i

final_audio = original - np.concatenate(
    [np.zeros(min_index),
    subtract,
    np.zeros(original.size - min_index - subtract.size)]) # create final audio

play_obj = sa.play_buffer(final_audio.astype(int), 1, 2, 48000) # play final audio
np.savetxt('final.csv', final_audio, delimiter=',') # save final audio to CSV file (play with audio_player.py)
    
