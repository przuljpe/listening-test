from just_playback import Playback
import os
import random
import time

audio_files = os.listdir("audio")
playback = Playback()

# Change sample_length to change how long a sample is played in seconds
sample_length = 15

played_songs = []

while len(played_songs) != len(audio_files):
    print("Next Song")
    cur_idx = random.randint(0, len(audio_files)-1)
    while cur_idx in played_songs:
        cur_idx = random.randint(0, len(audio_files)-1)
    
    cur_song = audio_files[cur_idx]
    song_details = cur_song.split("-")
    artist = song_details[0].lower()
    title = song_details[1][:-4].lower()
    file = os.path.join("audio", cur_song)
    try:
        playback.load_file(file)
    except:
        print(file)
    playback.play()
    playback.seek(random.random()*(playback.duration-sample_length))

    time.sleep(sample_length)
    playback.stop()
    guess_title = input("What is the title?\n").lower()
    guess_artist = input("Who is/are the artist(s)?\n").lower()

    if guess_title == title and guess_artist == artist:
        print("Correct!\n")
        played_songs.append(cur_idx)
    else:
        print("Incorrect", artist, title, "Your guesses:", guess_artist, guess_title, "\n")
    