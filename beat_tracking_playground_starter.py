#!/usr/bin/env python
# coding: utf-8

import librosa 
import mir_eval 
import IPython.display as ipd
import matplotlib.pyplot as plt
import numpy as np
import scipy as scp 


# use for local code 
disco_fname = "disco.00000.wav"
# use for PrairieLearn 
# disco_fname = "/grade/serverFilesCourse/disco.00000.wav"
# use for local code 
metal_fname = "metal.00080.wav"
# use for PraireLearn 
# metal_fname = "/grade/serverFilesCourse/metal.00080.wav"


# load two example sound files from the GTZAN collection 
(disco,srate) = librosa.load(disco_fname)
ipd.Audio(disco, rate=srate)

(metal,srate) = librosa.load(metal_fname)
ipd.Audio(metal, rate=srate)


# use an empty path when working locally
ref_path = ""
# use for PraireLearn 
# ref_path = "/grade/serverFilesCourse/" 


# load ground truth (ref) beat and downbeat times. These
# annotations were created manually by human annotators 
with open(ref_path + "ref_beats_disco.txt", "r") as file1:
    ref_beats_disco = [float(f) for f in file1.readlines()]

with open(ref_path + "ref_beats_metal.txt", "r") as file2:
    ref_beats_metal = [float(f) for f in file2.readlines()]

with open(ref_path + "ref_downbeats_disco.txt", "r") as file1:
    ref_downbeats_disco = [float(f) for f in file1.readlines()]

with open(ref_path + "ref_downbeats_metal.txt", "r") as file2:
    ref_downbeats_metal = [float(f) for f in file2.readlines()]


print("\nSETUP") 
print("ref_beats_disco:", ref_beats_disco[0:10])
print("ref_beats_metal:", ref_beats_metal[0:10])
print("ref_downbeats_disco:", ref_downbeats_disco[0:10])
print("ref_downbeats_metal:", ref_downbeats_metal[0:10])


# Q1 Estimate the tempo and beat times in seconds for the disco and metal
# examples using librosa.beat.beat_track with default parameters. Set the
# input, sample rate and units appropriately. Calculate an estimate of
# the tempo (mean_tempo_bpm_disco, mean_tempo_bpm_metal) by taking
# the average of the differences between successive beat times and converting
# that to BPM (beats per minute). Notice that these estimates are
# different than the ones returned by librosa.beat.beat_track 


# Uncomment and complete the lines below 
# tempo_disco, est_beats_disco = 
# tempo_metal, est_beats_metal = 
# tempo_disco = tempo_disco[0]
# tempo_metal = tempo_metal[0] 

print("\nQUESTION 1\n")

# uncomment and complete 
# mean_tempo_bpm_disco = 
#print("Disco estimated tempos", tempo_disco, mean_tempo_bpm_disco)

# mean_tempo_bpm_metal = 
# print("Metal estimated tempos", tempo_metal, mean_tempo_bpm_metal)



# Q2 Create a click track using the librosa.clicks function using th
# estimated beat time for the disco and metal track. Use a click frequency
# of 600Hz and a click duration of 0.5. Mix the two generated click tracks
# with the corresponding input audio and listen to the result.


print("\nQUESTION 2")

# uncomment and complete 
#click_disco = 

# ipd.Audio(data=disco+click_disco, rate=srate)

# uncomment and complete 
# click_metal = 
                
# ipd.Audio(data=metal+click_metal, rate=srate)

print("\nQ2 Audio files for click tracks have been created \n ") 


print("\nQUESTION 3")
      

# Q3 Now let's create a more interesting click track
# by leveraging the reference downbeat and beat times
# Create a "bass drum" click track by using the reference downbeat times
# a click frequency of 400 and a click duration of 0.5 and
# create a "snare drum" click track by using the reference beat times
# and a click duration of 0.25 and listen to the corresponding
# audio mixed with the original audio tracks 

# uncomment and complete 
# click_bass_disco = 
# click_kick_disco = 
#ipd.Audio(data= disco + click_bass_disco + click_kick_disco, rate=srate)


# uncomment and complete 
# click_bass_metal = 
                   

# click_kick_metal = l


# ipd.Audio(data= metal+ click_bass_metal + click_kick_metal, rate=srate)
print("\nQ3 Audio files for click tracks have been created \n ") 


#Q4 A common stage in beat tracking algorithm is to perform onset
# detection. We have seen how the onset strength signal looks.
# You can get onsets detected by using librosa.onset_onset_detect
# Calculate the estimated onsets expressed in second (units='time')
# and then listen to them by using a click track 

# uncomment and complete 
# est_onsets_disco = 
# est_onsets_metal = 

# click_onsets_disco =                        
# ipd.Audio(data=disco+click_onsets_disco, rate=srate)

#click_onsets_metal = 
# ipd.Audio(data=metal+click_onsets_metal, rate=srate)




# Q5 Calculate the onset strength signal for the two examples
# using librosa.onset.onset_strength using as a aggregate np.median
# The top subplots shows the mel-spectrogram of the audio signal
# showing some of the spectral features that will be used
# to calculate the onset strength signal.

# At the bottom subplot plot the onset strength signal using
# the times array for the x-values and label it Onset Strength using 
# ax[1].plot. Then plot the estimated beats using ax[1].vlines
# with alpha 0.5, color red, and linestyle -- with a label of 
# Beats. Make two plots one for each example.  


hop_length = 512

# uncomment and complete 
# onset_env = 
              

fig, ax = plt.subplots(nrows=2, sharex=True)

# uncomment and onset_env is computed 
# times = librosa.times_like(onset_env, sr=srate, hop_length=hop_length)

M = librosa.feature.melspectrogram(y=metal, sr=srate, hop_length=hop_length)
librosa.display.specshow(librosa.power_to_db(M, ref=np.max),
                         y_axis='mel', x_axis='time', hop_length=hop_length,
                         ax=ax[0])
ax[0].label_outer()
ax[0].set(title='Mel spectrogram')

# Uncomment and complete 
# ax[1].plot 
# ax[1].vlines
  
# ax[1].legend()


# onset_env = 
              
hop_length = 512
fig, ax = plt.subplots(nrows=2, sharex=True)

# uncomment when onset_env is computed 
#times = librosa.times_like(onset_env, sr=srate, hop_length=hop_length)
M = librosa.feature.melspectrogram(y=metal, sr=srate, hop_length=hop_length)
librosa.display.specshow(librosa.power_to_db(M, ref=np.max),
                         y_axis='mel', x_axis='time', hop_length=hop_length,
                         ax=ax[0])
ax[0].label_outer()
ax[0].set(title='Mel spectrogram')

# Uncomment and complete 
# ax[1].plot
# ax[1].vlines
# ax[1].legend()

print("\nQ5 Plots have been created \n ") 





# Q6 Using librosa.feature.rms calculate the rms envelope of each example.
# Use a frame_length of 20248 and a hop_length of 512
# Take the difference between successive RMS values
# to get a simple onset strength signal which you
# can normalize to be between -1.0 and 1.0 by calling librosa.util.normalize.
# Then make a simple onset detector by thresholding values above 0.5
# to 1.0 and everything else to 0.0. Calculate the times corresponding
# to these onsets and plot them similalry to how the beats were plotted
# above (use RMS onset envelope and RMS onsets for the labels).
# Also generate a click track with the onsets, mix it with the original
# and listen to the resutls for both examples 




print("\nQUESTION 6\n") 

frame_length = 2048  
hop_length = 512

# uncomment and complete 
# rms_envelope_disco =

# take the difference between successive samples and then nornamlize
# using librosa.util.normalize  
# nrms_envelope_disco = 

# nrms_envelope_disco = librosa.util.normalize(np.diff(rms_envelope_disco))

fig, ax = plt.subplots(nrows=2, sharex=True)

# rms_est_onsets_disco = [] 
# for (i,r) in enumerate(nrms_envelope_disco): 
#   if (r >  0.5):
#    rms_est_onsets_disco.append(times[i])



# times = librosa.times_like(nrms_envelope_disco, sr=srate, hop_length=hop_length)

M = librosa.feature.melspectrogram(y=disco, sr=srate, hop_length=hop_length)
librosa.display.specshow(librosa.power_to_db(M, ref=np.max),
                         y_axis='mel', x_axis='time', hop_length=hop_length,
                         ax=ax[0])
ax[0].label_outer()
ax[0].set(title='Mel spectrogram')


rms_est_onsets_disco = []
# complete the code in this loop 
# for (i,r) in enumerate(nrms_envelope_disco): 
#    pass

# uncomment and complete the code below 
# ax[1].plot
# ax[1].vlines
# ax[1].legend()

# uncomment and complete 
# rms_envelope_metal

fig, ax = plt.subplots(nrows=2, sharex=True)


# take the difference between successive samples and then nornamlize
# using librosa.util.normalize  
# nrms_envelope_disco = 
# nrms_envelope_metal =

# uncomment and compelte 
# times = librosa.times_like(nrms_envelope_metal, sr=srate, hop_length=hop_length)


M = librosa.feature.melspectrogram(y=metal, sr=srate, hop_length=hop_length)
librosa.display.specshow(librosa.power_to_db(M, ref=np.max),
                         y_axis='mel', x_axis='time', hop_length=hop_length,
                         ax=ax[0])
ax[0].label_outer()
ax[0].set(title='Mel spectrogram')

rms_est_onsets_metal = []
# complete the code in this loop 
#for (i,r) in enumerate(nrms_envelope_metal): 
#    pass 

# uncomment and complete the code below 
# ax[1].plot
# ax[1].vlines
# ax[1].legend()


# click_freq 600 and duration 0.5 for the rms_est_onsets_disco 
#rms_est_clicks_disco = librosa.clicks(times=rms_est_onsets_disco, sr=srate, click_freq=600,
#                               click_duration=0.5, length=len(disco))

# click_freq 600 and duration 0.5 for the rms_est_onsets_metal 
#rms_est_clicks_metal = librosa.clicks(times=rms_est_onsets_metal, sr=srate, click_freq=600,
#                               click_duration=0.5, length=len(metal))


# ipd.Audio(data=disco + rms_est_clicks_disco, rate=srate)
# ipd.Audio(data=metal + rms_est_clicks_metal, rate=srate)

print("\nQ6 Plots and audio have been created \n ") 



#Q7 Evaluation: use mir_eval.beat.f_measure to calculate
# the f-measure using the ref_beats as ground truth for both
# the disco and metal examples. First confirm that using
# ref_beats as both ground truth and estimations results
# in an f-measure of 1.0. Then check the estimated_beats,
# estimated onsets as well as the rms estimated onsets for
# both disco and metal 


print ("F-measure Disco")

f_measure_ref_disco = mir_eval.beat.f_measure(np.array(ref_beats_disco), np.array(ref_beats_disco))
print("Reference            :",  f_measure_ref_disco)

# Uncommment and complete 

# f_measure_beats_disco = 
# print("Estimated beats      :", f_measure_beats_disco)

# f_measure_onsets_disco = 
# print("Estimated onsets     :", f_measure_onsets_disco)

# f_measure_ronsets_disco = 
# print("Rms estimated onsets :", f_measure_ronsets_disco)


print ("F-measure Metal") 
f_measure_ref_metal = mir_eval.beat.f_measure(np.array(ref_beats_metal), np.array(ref_beats_metal))
print("Reference            :",  f_measure_ref_metal)

# Uncomment and complete 

# f_measure_beats_metal = 
# print("Estimated beats      :", f_measure_beats_metal)

# f_measure_onsets_metal = 
# print("Estimated onsets     :", f_measure_onsets_metal)

# f_measure_ronsets_metal = 
# print("Rms estimated onsets :", f_measure_ronsets_metal)




