#!/usr/bin/env python
"""
https://en.wikipedia.org/wiki/Quindar_tones
"""
from pynput.keyboard import Key, Listener
import numpy as np
import pygame

def genquindar():
    f0 = 2525 # [Hz]  key-down tone "start PTT"
    f1 = 2475 # [Hz]  key-up tone "stop PTT"
    T = 0.25 # [s] duration of each tone is equal.
    fs = 8000 #[Hz]
    
    t = np.arange(0,T,1/fs)
    s0 = (np.sin(2*np.pi*f0*t)*16384).astype(np.int16)
    s1 = (np.sin(2*np.pi*f1*t)*16384).astype(np.int16)
    # %%
    pygame.mixer.pre_init(fs, size=-16, channels=1, buffer=512)
    pygame.mixer.init()
    S0 = pygame.sndarray.make_sound(s0)
    S1 = pygame.sndarray.make_sound(s1)
    
    return S0,S1

def gentoneremote():
    # Motorola tone remote simulation
    f0 = 2175 # [Hz]
    f1 = 1950 # [Hz]
    T = 0.10 # [s]
    fs = 8000 # Hz
    t = np.arange(0,T,1/fs)
    
    s = np.concatenate(((np.sin(2*np.pi*f0*t)*16384).astype(np.int16),
                       (np.sin(2*np.pi*f1*t)*16384).astype(np.int16)))
    
    # %%
    pygame.mixer.pre_init(fs, size=-16, channels=1, buffer=512)
    pygame.mixer.init()
    S = pygame.sndarray.make_sound(s)

    return S    
# %%

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