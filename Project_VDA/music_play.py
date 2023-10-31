import pygame
from pygame import mixer
from tkinter import *
import os


def play():
    def playsong():
        currentsong = playlist.get(ACTIVE)
        print(currentsong)
        mixer.music.load(currentsong)
        songstatus.set("Playing")
        mixer.music.play()

    def pausesong():
        songstatus.set("Paused")
        mixer.music.pause()

    def stopsong():
        songstatus.set("Stopped")
        mixer.music.stop()

    def resumesong():
        songstatus.set("Resuming")
        mixer.music.unpause()

    root = Tk()
    root.title('Mia Music Player (MMP)')
    mixer.init()
    songstatus = StringVar()
    songstatus.set("choosing")
    #playlist---------------
    playlist = Listbox(root,
                       selectmode=SINGLE,
                       bg="black",
                       fg="orange",
                       font=('arial', 15),
                       width=43)
    playlist.grid(columnspan=5)
    print("Please check your directory path(line 41)")
    os.chdir(r'C:\Users\Owner\Desktop\project_ai\local_music')

    songs = os.listdir()
    for s in songs:
        playlist.insert(END, s)
    playbtn = Button(root, text="PLAY", command=playsong)
    playbtn.config(font=('arial', 20), bg="green", fg="white", padx=3, pady=5)
    playbtn.grid(row=1, column=0)

    pausebtn = Button(root, text="PAUSE", command=pausesong)
    pausebtn.config(font=('arial', 20),
                    bg="orange",
                    fg="white",
                    padx=3,
                    pady=5)
    pausebtn.grid(row=1, column=1)

    stopbtn = Button(root, text="STOP", command=stopsong)
    stopbtn.config(font=('arial', 20), bg="red", fg="white", padx=3, pady=5)
    stopbtn.grid(row=1, column=2)

    Resumebtn = Button(root, text="RESUME", command=resumesong)
    Resumebtn.config(font=('arial', 20),
                     bg="white",
                     fg="green",
                     padx=3,
                     pady=5)
    Resumebtn.grid(row=1, column=3)

    mainloop()