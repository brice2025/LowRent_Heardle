import tkinter as tk
from tkinter.filedialog import askdirectory
import os
from pygame import mixer
import random
import threading


state = None
playlist_bookmark = None

##########
# ToDo
##########
# final state play song add progress bar
# add volume bar (decided don't care, use system vol)


# create Tk object and set attrs
canvas = tk.Tk()
canvas.title("Low-Rent Heardle Training")
canvas.geometry("500x200")
canvas.config(bg='black')

# where to locate the music
rootpath = tk.filedialog.askdirectory()

# create the music player
mixer.init()


## Features I decided I didn't actually care about
#volume = tk.Scale(canvas, from_=0, to=100, orient='vertical')
#volume.pack(pady=15, padx=15, side='right')

# image files for the buttons
next_img = tk.PhotoImage(file="next_img.png")
play_img = tk.PhotoImage(file="play_img.png")
stop_img = tk.PhotoImage(file="stop_img.png")

# generate shuffled playlist and set playlist_bookmark to 0
if state == None:
    files = os.listdir(rootpath)

    #filter out any subfolders in the music folder
    music_files_only = []
    for file in files:
        path = os.path.join(rootpath, file)
        if not os.path.isdir(path):
            music_files_only.append(file)
    random.shuffle(music_files_only)
    #print(files)                       #(debugging)
    playlist_bookmark = 0
    #print(files[playlist_bookmark])    #(debugging)

##########
# Funcs
##########

def play():
    global state, playlist_bookmark
    if state == 0:
        mixer.music.load(rootpath + "\\" + music_files_only[playlist_bookmark])
        #print(music_files_only)                        #debug
        #print(music_files_only[playlist_bookmark])     #debug
        state = 1
        timer = threading.Timer(1, stop)
        mixer.music.play()
        timer.start()
        label.config(text="Guess 1 of 6")
        revealbutton.pack(pady=15, in_=top, side='left')
    elif state == 1:
        timer = threading.Timer(1, stop)
        mixer.music.play()
        timer.start()
        label.config(text="Guess 1 of 6")
    elif state == 2:
        timer = threading.Timer(2, stop)
        mixer.music.play()
        timer.start()
        label.config(text="Guess 2 of 6")
    elif state == 3:
        timer = threading.Timer(4, stop)
        mixer.music.play()
        timer.start()
        label.config(text="Guess 3 of 6")
    elif state == 4:
        timer = threading.Timer(7, stop)
        mixer.music.play()
        timer.start()
        label.config(text="Guess 4 of 6")
    elif state == 5:
        timer = threading.Timer(11, stop)
        mixer.music.play()
        timer.start()
        label.config(text="Guess 5 of 6")
    elif state == 6:
        timer = threading.Timer(16, stop)
        mixer.music.play()
        timer.start()
        label.config(text="Guess 6 of 6")
    elif state == 7:
        #play full song
        mixer.music.play()
        # reveal name and artist
        label.config(text=music_files_only[playlist_bookmark])
        revealbutton.pack_forget()
        if playlist_bookmark >= len(music_files_only) - 1:
            random.shuffle(music_files_only)
            playlist_bookmark = 0
        else:
            playlist_bookmark += 1

    #mixer.music.play()
    click_change(1)

def stop():
    """stops music, calls click_change"""
    mixer.music.stop()
    click_change(0)

def click_change(play_state):
    """change play button to stop and visa versa,
    play_state = 0 is playing, user clicks stop, remove stop button put in play"""
    if play_state == 0:
        playbutton.pack(pady=15, in_=top, side='right')
        stopbutton.pack_forget()
    else:
        stopbutton.pack(pady=15, in_=top, side='right')
        playbutton.pack_forget()

def next_state():
    global state
    if state == 7:
        state = 0
        play()
    else:
        state += 1
        play()


def reveal():
    """skip remaining guesses on current song, go directly to state 7 reveal and play"""
    global state
    state = 7
    play()

# displays the guess # and song - artist at end
label = tk.Label(canvas, text='', bg='black', fg='yellow', font=('poppins', 14))
label.pack(pady= 15)

top = tk.Frame(canvas, bg='black')
top.pack(padx=10, pady=5, anchor='center')


##########
# Buttons
##########

playbutton = tk.Button(canvas, text='Play', image=play_img, bg='black', borderwidth=0, command=play)
if state == None:
    playbutton.pack(pady=15, in_=top, side='left')
    state = 0
#
stopbutton = tk.Button(canvas, text="Stop", image=stop_img, bg='black', borderwidth=0, command=stop)
#
nextbutton = tk.Button(canvas, text="Skip", image=next_img, bg='black', borderwidth=0, command=next_state)
nextbutton.pack(pady=15, in_=top, side='left')
#
revealbutton = tk.Button(canvas, text="Reveal Answer", bg='yellow', borderwidth=0, command=reveal)


canvas.mainloop()

