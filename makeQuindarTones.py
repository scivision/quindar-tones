#!/usr/bin/env python
"""
https://en.wikipedia.org/wiki/Quindar_tones
"""
from quindar_tones import genquindar,gentoneremote
from pynput.keyboard import Key, Listener
import pygame

def on_press(key):
    if key==Key.left:
        S0.play()
    elif key==Key.right:
        S1.play()
    elif key==Key.up:
        S.play()
    else:
        print(key)
    
def on_release(key):
    #print(key)
    if key == Key.esc:
        # Stop listener
        return False

if __name__ == '__main__':
    """
    https://pythonhosted.org/pynput/keyboard.html#reference
    """
    S0,S1 = genquindar()
    S = gentoneremote()
    
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()    
