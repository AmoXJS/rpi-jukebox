# Jeremy's Jukebox 2.0
# Author: Jeremy Lightsmith
# Copyright (c) 2015 Jeremy Lightsmith

import time
import sys

datadir = "/mnt/music"
# datadir = "../music"

from music import MusicPlayer
player = MusicPlayer(datadir + "/music")

print "Welcome to Jeremy's Jukebox 2.0"
print ''


from nfc import CardReader
reader = CardReader(datadir)

# from keyboard import KeyboardReader
# reader = KeyboardReader()


def up(event):
    print("up")

def right(event):
    print("right")

def down(event):
    print("down")

def left(event):
    print("left")

def enter(event):
    print("enter")

def quit(event):
    print("quit")
    sys.exit()

def card(event):
    player.play_song(event[1])

def stop(event):
    player.stop_song()

dispatch = {
    'up':up,
    'right':right,
    'down':down,
    'left':left,
    'enter':enter,
    'card':card,
    'stop':stop,
    'quit':quit}


while True:
    event = reader.read()

    dispatch[event[0]](event)


